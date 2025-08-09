import sys 
import pygame 
from scripts.entities import PhysicsEntity
from scripts.utilities import load_image , load_images
from scripts.tilemap import Tilemap
class Game : 
    def __init__(self) : 
        pygame.init()
        self.screen = pygame.display.set_mode((640 , 480))
        self.display = pygame.Surface((320 , 240))
        pygame.display.set_caption("Ninja Game")
        self.clock = pygame.time.Clock()
        self.movement = [False , False]
        self.player = PhysicsEntity(self , "Player" , (50,50)  , (8,15))
        self.assets = {
            "Player" : load_image("entities/player.png"),
            "decor" : load_images("tiles/decor"),
            "grass" : load_images("tiles/grass"),
            "large_decor" : load_images("tiles/large_decor"),
            "spawners" : load_images("tiles/spawners"),
            "stone" : load_images("tiles/stone"),
            "background" : load_image("background.png")
        }
        self.tilemap = Tilemap(self, tile_size=16)
        self.scroll = [0,0]
    def run(self): 
        while True :
            self.display.blit(self.assets["background"] , (0,0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2  - self.scroll[0]) // 30 
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) // 30
            scroll_render = (int(self.scroll[0]),int(self.scroll[1]))

            self.tilemap.render(self.display , offset=scroll_render)
            self.player.update(self.tilemap , (self.movement[0] - self.movement[1] , 0))
            self.player.render(self.display , offset=scroll_render )


            for event in pygame.event.get() : 
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT : 
                        self.movement[0] = True 
                    if event.key == pygame.K_LEFT :
                        self.movement[1] = True
                    if event.key == pygame.K_UP : 
                        self.player.velocity[1] -= 3
                if event.type == pygame.KEYUP : 
                    if event.key == pygame.K_RIGHT :
                        self.movement[0] = False 
                    if event.key == pygame.K_LEFT : 
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display , self.screen.get_size()) , (0,0))
            self.clock.tick(60)
            pygame.display.update() 

Game().run()