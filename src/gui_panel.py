import pygame
from copy import deepcopy

from src.gui_config import *
from src.gui_classes import TextSprite

class Panel(pygame.sprite.Sprite):
    def __init__(self, 
                pos: list[int, int], 
                size: list[int, int], 
                  
                text_lable: str, 
                font_lable: pygame.font.Font,
                
                table_size: list[int, int], 
                table_data: list,
                font_data: pygame.font.Font, 

                title_color: str = COLOR_TEXT_TITLE,
                pos_lable: list[int, int] = [0, 0],  
                
                
                table_colors: list = None,
                                 
                table_ratios_cols: list = None,
                table_ratios_rows: list = None,
                table_gaps: list[int, int] = [0, 0],
                
                panel_background_color: str = COLOR_PANEL_BACKGROUND,
                selected_row: int = -1,
                selected_row_background_color: str = COLOR_PANEL_CHOOSE_ROW,
                
                groups: list[pygame.sprite.Group] = []
            ):
        super().__init__(groups)

        # Cover default values 
        if table_ratios_rows is None:
            table_ratios_rows = [1 for _ in range(table_size[0])]
        
        if table_ratios_cols is None:
            table_ratios_cols = [1 for _ in range(table_size[1])]
            
        if table_colors is None:
            self.table_colors = [[COLOR_TEXT_DEFAULT for _ in range(table_size[1])] for __ in range(table_size[0])]
        else:
            self.table_colors = table_colors
        
        # Panel variables
        self.pos = pos
        self.width, self.height = size        
        
        self.bg_color = panel_background_color
        self.selecter_row = -1
        self.selcted_row_color = selected_row_background_color
        
        # Pygame variables  
        self.texts_group = pygame.sprite.Group()    # Stores all the Text Tiles for table
        self.image = pygame.Surface(size) 
        self.rect = self.image.get_rect(topleft = pos)
        
        
        
        # Lable
        self.label_text = text_lable
        self.lable = TextSprite(
            text_lable,
            font_lable,
            title_color,
            pos_lable,
            
            groups = self.texts_group
        )
        
        # Table Vars
        self.table = [[None for __ in range(table_size[1])] for _ in range(table_size[0])]
        self.table_size = table_size
        self.create_table(
            table_data, 
            font_data, 
            table_ratios_rows, 
            table_ratios_cols,
            self.table_colors, 
            table_gaps,
        )
        
        
    def update_data(self, data, colors = None):
        """Function is updating the Table data to given new data

        Args:
            data (matrix of strings): matrix of string by the size of panel talbe each string is a value in table.
            colors(matrix of strings): matrix of string by the size of panel talbe each string represent hex color.
        """
        
        
        for row in range(self.table_size[0]):
            for col in range(self.table_size[1]):
                
                text = data[row][col]
                color = colors[row][col] if colors is not None else self.table_colors[row][col]
                
                self.table[row][col].change_text(text, color)
        
        
    def update(self):
        self.image.fill(self.bg_color)
        
        self.texts_group.draw(self.image)
    
    
    def create_table(self, data, font, table_ratios_rows, table_ratios_cols, table_colors, table_gaps):
        """ Private method to create table from data at class init.

        Args:
            data (list of list of strings): matrix that represents table with strings
            font (pygame font): pygame font for the table
            table_ratios_cols (list of int): ratios between each col size. for example [5, 10] -> the table cols will be like |"....."|".........."|
            table_ratios_rows (list of int): ratios between each row size. for example [5, 10] -> the table rows will be like |"....."|".........."| (verticaly)
            table_colors (matrix of strings):  matrix where each string is hex color "#000000"
            table_gaps (list of 2 ints): [row_gaps, col_gaps] - distance between rows and colos
        """
        
        # Calculate table size (panel_width - gap * (cols + 1), panel_height - title.bottom - gap * (rows + 1))
        width = self.width - table_gaps[1] * (self.table_size[1] + 1)
        height = self.height - self.lable.rect.bottom - table_gaps[0] * (self.table_size[0] + 1)
        
        
        # Caclulate sizes of each row and col
        rows_ratios_sum = sum(table_ratios_rows)
        rows_size_per_unit = height / rows_ratios_sum
        rows_sizes = [int(rows_size_per_unit * ratio) for ratio in table_ratios_rows]
        
        cols_ratios_sum = sum(table_ratios_cols)
        cols_size_per_unit = width / cols_ratios_sum
        cols_sizes = [int(cols_size_per_unit * ratio) for ratio in table_ratios_cols]
        
        
        # Calculate positions for each text
        positions = []
        for row in range(self.table_size[0]):
            for col in range(self.table_size[1]):
                pos = [
                    (col + 1) * table_gaps[1] + sum(cols_sizes[0: col]), 
                    self.lable.rect.bottom + (row + 1) * table_gaps[0] + sum(rows_sizes[0: row])
                ]
        
                self.table[row][col] = TextSprite(
                    text = data[row][col],
                    font = font, 
                    color = table_colors[row][col],
                    pos= pos,
                    
                    groups = self.texts_group
                )