from src.config import *
from src.binary_functions import * 


class HackCPU:
    def __init__(self):
        # Registers
        self.register_a = 0
        self.register_d = 0

        self.alu_out = 0

        self.pc = 0


    def execute_instruction(self, instruction: list, inM: int, reset: bool) -> list:
        """
            Method is executing any HACK instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value.
            :param reset: reset status.

            :return: outM: int(Out Memory value), writeM: bool(Write into a memory status), addressM: int (Address to writeM), PC: int(Program counter)
        """

        if reset:
            outM, writeM, addressM, pc = self.execute_instruction(instruction, inM, False)
            return [0, False, addressM, 0]


        if instruction[0] == 0:
            return self.execute_A_instruction(instruction, inM)

        else: 
            return self.execute_C_instruction(instruction, inM)


    def execute_A_instruction(self, instruction: list, inM: int) -> list:
        """
            Method is executing HACK A instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value.

            :return: outM: int(Out Memory value), writeM: bool(Write into a memory status), addressM: int (Address to writeM), PC: int(Program counter)
        """

        reg_a = self.register_a


        self.register_a = convert_bin_to_dec([0] + instruction[1:])
        self.pc += 1


        return [reg_a, False, self.register_a, self.pc]


    def execute_C_instruction(self, instruction: list, inM: int):
        """
            Method is executing HACK C instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value.

            
            :return: outM: int(Out Memory value), writeM: bool(Write into a memory status), addressM: int (Address to write in Memory), PC: int(Program counter)
        """


        # Execute COMP command.
        comp = instruction[3:10]    
        self.alu_out = self.get_alu_out(comp, inM)    


        # Find zr and ng Flags
        zr = self.alu_out == 0
        ng = self.alu_out < 0


        # Calculate Jump for pc counter 
        jmp_status = self.get_jmp_status(instruction[13:], zr, ng)

        if jmp_status == True:
            self.pc = self.register_a
        else: 
            self.pc += 1


        # Calculate dest
        dest_a, dest_d, dest_m = self.get_dest(instruction[10: 13])

        if dest_a:
            self.register_a = self.alu_out

        if dest_d:
            self.register_d = self.alu_out

        return [self.alu_out, dest_m, self.register_a, self.pc]


    def get_alu_out(self, comp: list, inM: int):
        """
            Method gots and "a c c c c c c" part of HACK instruction, inM value, and returns alu output.'

            :param comp: part of an istruction that related to alu output. [a, c, c, c, c, c, c]
            :param inM: inM value. 
        """

        if comp == COMP_0:
            self.alu_out = 0

        elif comp == COMP_1:
            self.alu_out = 1

        elif comp == COMP_MINUS_1:
            self.alu_out = -1

        elif comp == COMP_D:
            self.alu_out = self.register_d

        elif comp == COMP_A:
            self.alu_out = self.register_a

        elif comp == COMP_NOT_D:
            self.alu_out = convert_bin_to_dec(Not16(convert_dec_to_bin(self.register_d)))

        elif comp == COMP_NOT_A:
            self.alu_out = convert_bin_to_dec(Not16(convert_dec_to_bin(self.register_a)))

        elif comp == COMP_MINUS_D:
            self.alu_out = -self.register_d

        elif comp == COMP_MINUS_A:
            self.alu_out = -self.register_a

        elif comp == COMP_D_PLUS_ONE:
            new_bin = convert_dec_to_bin(self.register_d)
            new_bin = Add16(new_bin, BINARY_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_A_PLUS_ONE:
            new_bin = convert_dec_to_bin(self.register_a)
            new_bin = Add16(new_bin, BINARY_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_D_MINUS_ONE:
            new_bin = convert_dec_to_bin(self.register_d)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_A_MINUS_ONE:
            new_bin = convert_dec_to_bin(self.register_a)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_D_PLUS_A:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_a = convert_dec_to_bin(self.register_a)

            self.alu_out = convert_bin_to_dec(Add16(bin_d, bin_a))

        elif comp == COMP_D_MINUS_A:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_a = Not16(convert_dec_to_bin(self.register_a))

            self.alu_out = convert_bin_to_dec(Add16(bin_d, bin_a)) + 1

        elif comp == COMP_A_MINUS_D:
            bin_d = Not16(convert_dec_to_bin(self.register_d))
            bin_a = convert_dec_to_bin(self.register_a)

            self.alu_out = convert_bin_to_dec(Add16(bin_a, bin_d)) + 1

        elif comp == COMP_D_AND_A:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_a = convert_dec_to_bin(self.register_a)

            self.alu_out = convert_bin_to_dec(And16(bin_a, bin_d)) + 1

        elif comp == COMP_D_OR_A:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_a = convert_dec_to_bin(self.register_a)

            self.alu_out = convert_bin_to_dec(Or16(bin_a, bin_d)) + 1

        elif comp == COMP_M:
            self.alu_out = inM

        elif comp == COMP_NOT_M:
            self.alu_out = convert_bin_to_dec(Not16(convert_dec_to_bin(inM)))

        elif comp == COMP_MINUS_M:
            self.alu_out = -inM

        elif comp == COMP_M_PLUS_ONE:
            new_bin = convert_dec_to_bin(inM)
            new_bin = Add16(new_bin, BINARY_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_M_MINUS_ONE:
            new_bin = convert_dec_to_bin(inM)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = convert_bin_to_dec(new_bin)

        elif comp == COMP_D_PLUS_M:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_m = convert_dec_to_bin(inM)

            self.alu_out = convert_bin_to_dec(Add16(bin_d, bin_m))

        elif comp == COMP_D_MINUS_M:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_m = Not16(convert_dec_to_bin(inM))

            self.alu_out = convert_bin_to_dec(Add16(bin_d, bin_m)) + 1

        elif comp == COMP_M_MINUS_D:
            bin_d = Not16(convert_dec_to_bin(self.register_d))
            bin_m = convert_dec_to_bin(inM)

            self.alu_out = convert_bin_to_dec(Add16(bin_m, bin_d)) + 1

        elif comp == COMP_D_AND_M:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_m = convert_dec_to_bin(inM)

            self.alu_out = convert_bin_to_dec(And16(bin_m, bin_d)) + 1

        elif comp == COMP_D_OR_M:
            bin_d = convert_dec_to_bin(self.register_d)
            bin_m = convert_dec_to_bin(inM)

            self.alu_out = convert_bin_to_dec(Or16(bin_m, bin_d)) + 1

        else:
            raise ValueError("Hack CPU error, instruction COMP not found! instruction: " + str(instruction))


        return self.alu_out


    def get_jmp_status(self, jmp: list, zr: bool, ng: bool):
        """
            Function for calculating jmp status. 

            :param jmp: list -> [j, j, j] from instruction
            :param zr: bool that represents alu_out == 0
            :param ng: bool that represents alu_out < 0

            :return: jump status, bool
        """
        jmp_status = False

        if jmp == JUMP_NULL:
            jmp_status = False

        elif jmp == JUMP_JGT:
            jmp_status = not ng and not zr

        elif jmp == JUMP_JEQ:
            jmp_status = zr

        elif jmp == JUMP_JGE:
            jmp_status = not ng

        elif jmp == JUMP_JLT:
            jmp_status = ng

        elif jmp == JUMP_JNE:
            jmp_status = not zr

        elif jmp == JUMP_JLE:
            jmp_status = ng or zr

        elif jmp == JUMP_JMP:
            jmp_status = True

        return jmp_status


    def get_dest(self, dest: list) -> list:
        """
            Function to get the dest bools from instruction d part.
            
            :param dest: sub list from instruction that represents dest [d, d, d]

            :return: list of 3 bool values -> [writeA, writeD, writeM]
        """
        writeA = bool(dest[0])
        writeD = bool(dest[1])
        writeM = bool(dest[2])

        return writeA, writeD, writeM


    def reset(self):
        """
            Method to reset an CPU.

            :return: nones
        
        """
        self.register_a = 0
        self.register_d = 0

        self.alu_out = 0
        self.pc = 0
    