import time
import argparse
import pygame

# Hack computer imports
from src.hack.hack_computer import HackComputer
from src.hack.hack_config import MAX_POSITIVE_VALUE
from src.hack.binary_functions import convert_bin_to_dec, convert_dec_to_bin

# Gui imports 
from src.gui.emulator import GuiEmulator
from src.gui.config import MAX_GUI_SPEED


class HackEmulator:
    def __init__(self):
         # ----- Get Flags -----
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--path", help = "Path to .hack file to load into a hack pc", default = None, type = str)
        registers = [0 for i in range(16)]
        for i in range(16):
            parser.add_argument(f"--R{i}", help = f"Value to insert into an R{i} register(range: -{MAX_POSITIVE_VALUE + 1} - {MAX_POSITIVE_VALUE})", default=0, type = int)
        
        
        args = parser.parse_args()
        registers[0] = args.R0
        registers[1] = args.R1
        registers[2] = args.R2
        registers[3] = args.R3
        registers[4] = args.R4
        registers[5] = args.R5
        registers[6] = args.R6
        registers[7] = args.R7
        registers[8] = args.R8
        registers[9] = args.R9
        registers[10] = args.R10
        registers[11] = args.R11
        registers[12] = args.R12
        registers[13] = args.R13
        registers[14] = args.R14
        registers[15] = args.R15
        
        # init pygame
        pygame.init()
        self.time = 0
        
        # Create hack pc
        self.hack_pc = HackComputer(args.path, registers)
        self.gui = GuiEmulator(self.hack_pc)
        
    
    def timer(self):
        """Method for time control itterations

        :return: True if timer is passed, false otherwise
        """
        # If timer is passed -> update time for next iteration and return True
        if (self.gui.gui_speed - MAX_GUI_SPEED == 0) or ( pygame.time.get_ticks() // (MAX_GUI_SPEED - self.gui.gui_speed) != self.time):
            if self.gui.gui_speed - MAX_GUI_SPEED == 0:
                self.time = pygame.time.get_ticks()
            else:
                self.time = pygame.time.get_ticks() // (MAX_GUI_SPEED - self.gui.gui_speed)
                
            return True
            
        # If not -> update time for next iteration 
        if self.gui.gui_speed - MAX_GUI_SPEED == 0:
            self.time = pygame.time.get_ticks()
        else:
            self.time = pygame.time.get_ticks() // (MAX_GUI_SPEED - self.gui.gui_speed)
                
        return False
        
        
    def run(self):
        self.time = 0
        while True:
            self.gui.run()
            
            if self.timer() and self.gui.run_hack_computer:
                self.hack_pc.execute_command()
                    
                
            
            

if __name__ == "__main__":
    emulartor = HackEmulator()  
    emulartor.run()