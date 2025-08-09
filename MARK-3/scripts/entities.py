import pygame 

class PhysicsEntity:
    def __init__(self, game , e_type , pos , size):
        self.game = game
        self.size = size 
        self.type = e_type 
        self.pos = list(pos)
        self.velocity = [0, 0]
        self.collision = {"right" : False , "left" : False , "down" : False , "up" : False}

    def rect(self): 
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)): 
        self.collision = {"right": False , "left" : False , "down" : False , "up" : False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for tile in tilemap.physics_tile_around(self.pos) :
            if entity_rect.colliderect(tile):
                if frame_movement[0] > 0 : 
                    entity_rect.right = tile.left 
                    self.collision["right"] = True
                if frame_movement[1] < 0 : 
                    entity_rect.left = tile.right
                    self.collision["left"] = True
                self.pos[0] = entity_rect.x
        self.pos[1] += frame_movement[1]

        entity_rect = self.rect() 
        for tile in tilemap.physics_tile_around(self.pos) :
            if entity_rect.colliderect(tile) :
                if frame_movement[1] > 0 :
                    entity_rect.bottom = tile.top 
                    self.collision["down"] = True
                if frame_movement[1] < 0 :
                    entity_rect.top = tile.bottom 
                    self.collision["up"] = True
                self.pos[1] = entity_rect.y
        self.velocity[1] = min(4 , self.velocity[1] + 0.1)
        if self.collision["up"] or self.collision["down"] : 
            self.velocity[1] = 0

    def render(self, surface , offset=(0,0)):
        surface.blit(self.game.assets["Player"], (self.pos[0] - offset[0] , self.pos[1] - offset[1]))
