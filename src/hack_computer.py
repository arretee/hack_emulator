from src.hack_cpu import HackCPU
from src.hack_config import * 


class HackComputer:
    def __init__(self):

        # CPU
        self.cpu = HackCPU()

        # Memory
        self.RAM = [0 for i in range(RAM_SIZE)]
        self.ROM = [[0 for j in range(16)] for i in range(ROM_SIZE)]

        # Cpu variables
        self.pc = 0
        self.addressM = 0




    def load_instructions(self, file_path: str) -> None:
        with open(file_path) as file:
            self.ROM = [[int(bit) for bit in line.rstrip()] for line in file]

        self.pc = 0


    def execute_command(self) -> None:
        outM, writeM, self.addressM, pc = self.cpu.execute_instruction(self.ROM[self.pc], self.RAM[self.addressM], False)

        self.pc = pc

        if writeM:
            print(f"Adress {self.addressM} = ", outM)
            print()
            self.RAM[self.addressM] = outM

        