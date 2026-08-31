from src.hack_cpu import HackCPU
from src.config import * 


class HackComputer:
    def __init__(self):
        self.cpu = HackCPU()

        self.pc = 0

        self.RAM = [0 for i in range(RAM_SIZE)]
        self.ROM = [[0 for j in range(16)] for i in range(ROM_SIZE)]