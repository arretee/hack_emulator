from src.binary_functions import *
from src.hack_cpu import *

class HackEmulator:
    def __init__(self):
        pass


    def run(self):
        pass

if __name__ == "__main__":
    cpu = HackCPU()

    cpu.register_a = convert_dec_to_bin(500)
    cpu.register_d = convert_dec_to_bin(-5)
    cpu.pc = 10
    instruction = [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]

    outM, writeM, addressM, pc = cpu.execute_instruction(instruction, convert_dec_to_bin(0), False)


