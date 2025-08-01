import pygame, os, random
from os.path import join

pygame.init()
pygame.display.set_caption("Platformer Game")

WIDTH, HEIGHT = 900, 600
FPS = 60
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_VELOCITY = -15

window = pygame.display.set_mode((WIDTH, HEIGHT))

# === Load Assets ===
def load_sprite_sheet(folder, width, height, direction=False):
    images = []
    path = join("assets", folder)
    for file in sorted(os.listdir(path)):
        image = pygame.image.load(join(path, file)).convert_alpha()
        if direction:
            images.append({"right": image, "left": pygame.transform.flip(image, True, False)})
        else:
            images.append(image)
    return images

def load_fruits():
    path = join("assets", "items", "Fruits")
    return [pygame.image.load(join(path, fruit)).convert_alpha() for fruit in os.listdir(path)]

def load_traps():
    trap_images = []
    trap_types = ["Arrow", "Fire", "Spike Head", "Spiked Ball"]
    for t in trap_types:
        trap_path = join("assets", "traps", t)
        for file in sorted(os.listdir(trap_path)):
            trap_images.append(pygame.image.load(join(trap_path, file)).convert_alpha())
    return trap_images

# === Load Assets Once ===
# ...existing code...

# === Load Assets Once ===
player_sprites = load_sprite_sheet("MainCharacters/MaskDude", 32, 32 , direction=True)
background = pygame.image.load(join("assets", "Background", "Blue.png")).convert()
block_img = pygame.image.load(join("assets", "Terrain", "Terrain (32x32).png")).convert_alpha()
fruit_imgs = load_fruits()
trap_imgs = load_traps()

# ...existing code...

# === Classes ===
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = player_sprites
        self.index = 0
        self.image = self.images[self.index]["right"]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400
        self.vel_y = 0
        self.facing = "right"
        self.on_ground = False

    def update(self, keys):
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
            self.facing = "left"
        elif keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED
            self.facing = "right"

        self.rect.x += dx
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index][self.facing]

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_VELOCITY

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

# === Setup ===
player = Player()
player_group = pygame.sprite.Group(player)

fruit_group = pygame.sprite.Group()
for _ in range(5):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    fruit = Fruit(x, y, random.choice(fruit_imgs))
    fruit_group.add(fruit)

trap_group = pygame.sprite.Group()
for _ in range(4):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(HEIGHT//2, HEIGHT - 64)
    trap = Trap(x, y, random.choice(trap_imgs))
    trap_group.add(trap)

# === Main Loop ===
clock = pygame.time.Clock()
run = True
score = 0
font = pygame.font.SysFont("arial", 24)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.jump()

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check for fruit collision
    collected = pygame.sprite.spritecollide(player, fruit_group, dokill=True)
    score += len(collected)

    # Check for trap collision
    if pygame.sprite.spritecollideany(player, trap_group):
        print("You hit a trap! Game Over.")
        run = False

    # === Drawing ===
    window.blit(background, (0, 0))
    player_group.draw(window)
    fruit_group.draw(window)
    trap_group.draw(window)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
