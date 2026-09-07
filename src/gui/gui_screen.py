import pygame

from src.gui.config import * 

from src.hack.hack_config import REGISTER_SIZE, SCREEN_REGISTERS_NUM
from src.hack.hack_computer import HackComputer

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
        bit_num = 0
        for register in range(SCREEN_REGISTERS_NUM):
            for bit in self.hack_computer.RAM[SCREEN + register]:
                if bit:
                    self.image.set_at((bit_num % self.size[0], bit_num // self.size[0]), COLOR_SCREEN_BLACK)
                    
                bit_num += 1
                
            
                    
                    
    
    
    
    
        
        