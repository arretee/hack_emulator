from src.hack_computer import HackComputer
from src.config import * 
from src.binary_functions import * 

from time import sleep

hack_computer = HackComputer()
hack_computer.load_instructions("hack_codes/Mult.hack")

hack_computer.RAM[R0] = 8
hack_computer.RAM[R1] = 10


while True:
    hack_computer.execute_command()

    for i in range(16):
        print(f"R{i}: ", hack_computer.RAM[i])



