import pygame

from gui_config import *

class Panel(pygame.sprite.Sprite):
    def __init__(self, pos: list[int], size: list[int],  table_size: list[int], font: pygame.Font, title:str, data:list[list[str]]):
        """ Panel init function creating panel

        Args:
            pos (list[int]): (x, y) position of topleft of the panel
            size (list[int]): (width, height) of panel
            table_size (list[int]): (row, col) of table inside the panel
            font (pygame.Font): Pygame font for text
            title (str): panel title
            data (list[list[str]]): data to fill with the panel table.
        """
        super().__init__()
        
        # Position and size
        self.pos = pos
        self.size = size
        
        # Text
        self.font = font
        self.title = title
        
        self.table_size = table_size
        self.data = data
        
        
        # Setup pygame and sprite
        self.image = pygame.Surface(self.size) 
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.image.fill(COLOR_PANEL_BACKGROUND)
        
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    