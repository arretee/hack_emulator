import time

from src.hack_computer import HackComputer
from src.hack_config import *

from src.binary_functions import convert_bin_to_dec, convert_dec_to_bin
from src.gui_emulator import GuiEmulator


class HackEmulator:
    def __init__(self):
        
        self.hack_pc = HackComputer()
        self.gui = GuiEmulator(self.hack_pc)
        
        
        self.hack_pc.RAM[0] = convert_dec_to_bin(5)
        self.hack_pc.RAM[1] = convert_dec_to_bin(20)
        
        
        self.hack_pc.load_instructions("hack_codes/Mult.hack")

    def run(self):
        while True:
            self.gui.run()
            
            self.hack_pc.execute_command()
            
            time.sleep((MAX_GUI_SPEED - self.gui.gui_speed) / 1000)
            
            

if __name__ == "__main__":
    emulartor = HackEmulator()  
    emulartor.run()