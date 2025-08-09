import pygame 
OFFSET_NEIGHBOR = [(0,0) , (0,1) , (0,-1) , (1,0) , (1,1) , (1,-1) , (-1,0) , (-1,1) ,(-1,-1)]
PHYSICS_TILE = {"grass" , "stone"}
class Tilemap : 
    def __init__(self,Test , tile_size=16) : 
        self.game = Test
        self.tile_size = tile_size 
        self.tilemap = {}
        self.offgrid_tiles = []
        for i in range(10) : 
            self.tilemap[str(3 + i) + ";10"] = {"type" : "grass" , "variant" : 1 , "pos" : (3 + i , 10)}
            self.tilemap["10;"+ str(5+i)] = {"type" : "stone"  , "variant" : 1 , "pos": (10 , 5 + i)} 
    
    def tile_around(self , pos) : 
        tiles = []
        tiles_loc = (int(pos[0] // self.tile_size ) , int(pos[1] // self.tile_size))
        for offset in OFFSET_NEIGHBOR : 
            check_loc = (str(tiles_loc[0] + offset[0]) + ";" + str(tiles_loc[1] + offset[1]) )
            if check_loc in self.tilemap : 
                tiles.append(self.tilemap[check_loc])
        return tiles
        
    def physics_tile_around(self , pos) : 
        rect = []
        for tile in self.tile_around(pos) : 
            if tile["type"] in PHYSICS_TILE : 
                rect.append(pygame.Rect(tile["pos"][0] * self.tile_size , tile["pos"][1] * self.tile_size , self.tile_size , self.tile_size))
        return rect 



    def render(self ,surface , offset=(0,0)):
        for tile in self.offgrid_tiles : 
            surface.blit(self.game.assets[tile["type"]][tile["pos"]] , (tile["pos"][0] - offset[0] ,tile["pos"][1] - offset[1]))
        for loc in self.tilemap :
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile["type"]][tile["variant"]] , (tile["pos"][0] * self.tile_size - offset[0], tile["pos"][1] * self.tile_size - offset[1]))