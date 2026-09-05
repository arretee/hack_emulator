import pygame

from src.gui_config import * 

from src.hack_config import REGISTER_SIZE, SCREEN_REGISTERS_NUM
from src.hack_computer import HackComputer

class GuiScreen(pygame.sprite.Sprite):
    """
        Class represents pygame object to draw an Hack Computer screen
    """
    
    def __init__(self, pos, hack_computer: HackComputer, groups:list = []):
        """
        Args:
            pos (list[int, int]): [x, y] of screen topleft corner
            hack_computer (HackComputer): pointer to hack_computer 
            groups (list): list of groups to add sprite to
        """
        super().__init__(groups)
        
        self.pos = pos
        self.size = EMULATOR_SCREEN_SIZE
        
        self.hack_computer = hack_computer
        
        
        
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        
        
    def update(self):
        """
            Method updates the screen
        """
        self.image.fill(COLOR_SCREEN_DEFAULT)
        
        # For each pixel check RAM bit
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                bit_num = row * REGISTER_SIZE + col
                
                ram_register = bit_num // REGISTER_SIZE
                register_pixel = bit_num % REGISTER_SIZE
                
                if self.hack_computer.RAM[SCREEN + ram_register][register_pixel]:
                    self.image.set_at((row, col), COLOR_SCREEN_BLACK)
    
    
    
    
        
        