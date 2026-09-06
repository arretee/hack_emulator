from src.hack.hack_cpu import HackCPU
from src.hack.hack_config import * 
from src.hack.binary_functions import convert_bin_to_dec, convert_dec_to_bin


class HackComputer:
    def __init__(self, path, registers_r):
        """
        Args:
            path (str): path to file to load into an hack ROM
            registers_r (list of ints): list of integers for some number of regiseters.
        """

        # CPU
        self.cpu = HackCPU()

        # Memory
        self.RAM = [[0 for j in range(REGISTER_SIZE)] for i in range(RAM_SIZE)]     # EVERY CELL - BINARY 
        self.ROM = [[0 for j in range(REGISTER_SIZE)] for i in range(ROM_SIZE)]     # EVERY CELL - BINARY
        

        # Saved given registers

        # Cpu variables
        self.pc: int = 0
        self.addressM: int = 0
        
        
        
        
        # Apply given data
        self.path = path
        self.registers_r = registers_r
        
        for r in range(len(self.registers_r)):
            self.RAM[r] = convert_dec_to_bin(self.registers_r[r])
            
        self.load_instructions(path)




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
        if self.pc >= ROM_SIZE:
            raise ValueError("Program Counter exited ROM.")

        if writeM:
            self.RAM[self.addressM] = outM
            
    def update_kbd(self, value: int) -> None:
        """Method to set kbd value

        Args:
            value (int): int value of KBD
        """
        
        self.RAM[KBD] = convert_dec_to_bin(value)
        
        
                    
    def manul_reset(self) -> None:
        """
            Manual reset for hack pc
            ROM is not touched
        """
        self.cpu = HackCPU()
        
        self.RAM = [[0 for j in range(REGISTER_SIZE)] for i in range(RAM_SIZE)]     # EVERY CELL - BINARY 
        self.pc: int = 0
        self.addressM: int = 0
        
        # Reset the registers to given data
        for r in range(len(self.registers_r)):
            self.RAM[r] = convert_dec_to_bin(self.registers_r[r])
        

        