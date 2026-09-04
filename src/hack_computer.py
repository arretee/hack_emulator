from src.hack_cpu import HackCPU
from src.hack_config import * 


class HackComputer:
    def __init__(self):

        # CPU
        self.cpu = HackCPU()

        # Memory
        self.RAM = [[0 for j in range(REGISTER_SIZE)] for i in range(RAM_SIZE)]     # EVERY CELL - BINARY 
        self.ROM = [[0 for j in range(REGISTER_SIZE)] for i in range(ROM_SIZE)]     # EVERY CELL - BINARY

        # Cpu variables
        self.pc: int = 0
        self.addressM: int = 0




    def load_instructions(self, file_path: str) -> None:
        """Funtion loads instructions from file into ROM memory of HackComputer

        Args:
            file_path (str): file path to load instructions from. Must be .hack file
        """
        with open(file_path) as file:
            for index, line in enumerate(file):
                self.ROM[index] = [int(bit) for bit in line.rstrip()]
           

        self.pc = 0


    def execute_command(self) -> None:
        """
            Function executes command from an next ROM address that is stored in self.pc.
        """
        outM, writeM, self.addressM, pc = self.cpu.execute_instruction(self.ROM[self.pc].copy(), self.RAM[self.addressM].copy(), False)

        self.pc = pc

        if writeM:
            self.RAM[self.addressM] = outM

        