import pygame
from copy import deepcopy

from src.gui_config import *
from src.gui_classes import TextSprite

class Panel(pygame.sprite.Sprite):
    def __init__(self, 
                pos: list[int, int], 
                size: list[int, int], 
                  
                text_title: str, 
                font_title: pygame.font.Font,
                
                table_size: list[int, int], 
                table_data: list,
                font_data: pygame.font.Font, 

                title_color: str = COLOR_TEXT_TITLE,
                pos_title: list[int, int] = [0, 0],  
                
                
                table_colors: list = None,
                                 
                table_ratios_cols: list = None,
                table_ratios_rows: list = None,
                table_gaps: list[int, int] = [0, 0],
                
                panel_background_color: str = COLOR_PANEL_BACKGROUND,
                panel_border_color: str = COLOR_PANEL_BORDER,
                
                groups: list[pygame.sprite.Group] = []
            ):
        """
        Class panel to represent data in tables for pygame

        :param pos: position of an panel (topleft corner)
        :type pos: list[int, int]
        :param size: size of an panel [width, height]
        :type size: list[int, int]
        :param text_title: title of an panel
        :type text_title: str
        :param font_title: title font
        :type font_title: pygame.font.Font
        :param table_size: table size that panel will represent (rows, cols)
        :type table_size: list[int, int]
        :param table_data: matrix by size of table size that filled width string for each table place
        :type table_data: matrix
        :param font_data: font for table values
        :type font_data: pygame.font.Font
        :param title_color: color for title, string hex, example: "#ffffff", defaults to COLOR_TEXT_TITLE
        :type title_color: str, optional
        :param pos_title: position of title on panel, defaults to [0, 0]
        :type pos_title: list[int, int], optional
        :param table_colors: matrix of colors for each matrix place, defaults to COLOR_TEXT_DEFAULT for each
        :type table_colors: list, optional
        :param table_ratios_cols: size ratios between table cols [2, 1] -> |xx|x| , defaults to each seted to one
        :type table_ratios_cols: list, optional
        :param table_ratios_rows: size ratios between table rows [2, 1] -> |xx|x| , defaults to each seted to one
        :type table_ratios_rows: list, optional
        :param table_gaps: gaps between table values, defaults to [0, 0]
        :type table_gaps: list[int, int], optional
        :param panel_background_color: bg color of panel, defaults to COLOR_PANEL_BACKGROUND
        :type panel_background_color: str, optional
        :param panel_border_color: border of panel color, defaults to COLOR_PANEL_BORDER
        :type panel_border_color: str, optional
        :param groups: groups to add the object in, defaults to []
        :type groups: list[pygame.sprite.Group], optional
        """
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
        
        # Pygame variables  
        self.texts_group = pygame.sprite.Group()    # Stores all the Text Tiles for table
        self.image = pygame.Surface(size) 
        self.rect = self.image.get_rect(topleft = pos)
        
        
        
        # title
        self.title_text = text_title
        self.title = TextSprite(
            text_title,
            font_title,
            title_color,
            pos_title,
            
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
        height = self.height - self.title.rect.bottom - table_gaps[0] * (self.table_size[0] + 1)
        
        
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
                    self.title.rect.bottom + (row + 1) * table_gaps[0] + sum(rows_sizes[0: row])
                ]
        
                self.table[row][col] = TextSprite(
                    text = data[row][col],
                    font = font, 
                    color = table_colors[row][col],
                    pos= pos,
                    
                    groups = self.texts_group
                )