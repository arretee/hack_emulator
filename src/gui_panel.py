import pygame
from copy import deepcopy

from src.gui_config import *

class Panel(pygame.sprite.Sprite):
    def __init__(self, pos: list[int, int], size: list[int, int],  table_size: list[int, int], font: pygame.Font, title:str, data:list[list[str]]):
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
        self.data = deepcopy(data)
        
        
        # Setup pygame and sprite
        self.image = pygame.Surface(self.size) 
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.image.fill(COLOR_PANEL_BACKGROUND)
        
    def update(self):
        self.image.fill(COLOR_PANEL_BACKGROUND)

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

class PanelRegisters(Panel):
    def __init__(self, pos: list[int, int], size: list[int, int],  table_size: list[int, int], font: pygame.Font, title:str, data:list[list[str]], gaps: list[int, int], cols_ratios: list):
        """ Panel init function creating PanelRegisters.
            Panel scheme:
                Registers
                    A   Dec     Hex     Binary
                    D   Dec     Hex     Binary
                    M   Dec     Hex     Binary
                    PC  Dec     Hex     Binary

        Args:
            pos (list[int]): (x, y) position of topleft of the panel
            size (list[int]): (width, height) of panel
            table_size (list[int]): (row, col) of table inside the panel
            font (pygame.Font): Pygame font for text
            title (str): panel title
            data (list[list[str]]): data to fill with the panel table.
            gaps: gaps between rows and coloms 
            cols_ratios: list of size ration between cols
        """
        
        super().__init__(pos, size, table_size, font, title, data)
        
        self.gaps = gaps
        self.ratios = cols_ratios
        
        
        self.titleTile = None
        
        self.table = [[EMPTY for i in range(table_size[1])] for j in range(table_size[0])]
        self.group = pygame.sprite.Group()
        
        
        self.create_table()
        
        
    def create_table(self):
        """
            PanelRegisters inner method to init the table of data
        """
        # width = self.size[0] - self.titleTile.rect.width - self.gaps[1] * (self.table_size[1] + 1)
        # height = self.size[1] - self.titleTile.rect.height - self.gaps[0] * (self.table_size[0] + 1)
        
        width = self.size[0] - self.gaps[1] * (self.table_size[1] + 1)
        height = self.size[1] - self.gaps[0] * (self.table_size[0] + 1)
        
        
        cols_ratios_sum = sum(self.ratios)
        cols_ratio_unit = width / cols_ratios_sum
        
        col_sizes = [int(cols_ratio_unit * col) for col in self.ratios]
        row_sizes = [int(height / self.table_size[0])] * self.table_size[0]
        
        
        # Create  
        for row in range(self.table_size[0]):
            for col in range(self.table_size[1]):
                color = PANEL_REGISTERS_COLORS[row][col]
                text = PANEL_REGISTERS_DATA_SAMPLE[row][col]
                
                pos = [
                    (row + 1) * self.gaps[0] + sum(row_sizes[0:row + 1]),
                    (col + 1) * self.gaps[1] + sum(col_sizes[0:col + 1]),
                ]
                
                print(text, color, pos)                  
                
                
    def update(self):
        super().update()
    

                
                    
    def draw(self, screen):
        """draws the pannel on the screen

        Args:
            screen (pygame surface): surface to draw on
        """
        super().draw(screen)
        
        