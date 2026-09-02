from src.hack_computer import HackComputer
from src.hack_config import *
from src.binary_functions import *
from src.emulator_gui import *

class HackEmulator:
    def __init__(self):
        self.hack_pc = HackComputer()
        self.gui = EmulatorGUI(self.hack_pc)

    def run(self):
        while not self.gui.exit_status:
            self.gui.run()

if __name__ == "__main__":
    emulartor = HackEmulator()  
    emulartor.run()