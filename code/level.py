import pygame
from settings import *
from tiles import Tile

class Level:
    def __init__(self,level_data,surface):
        
        # Level Setup
        self.display_surface = surface
        self.level_setup(level_data)
        self.world_shift = 0

    def level_setup(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        