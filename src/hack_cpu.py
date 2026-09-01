from src.hack_config import *
from src.binary_functions import * 


class HackCPU:
    def __init__(self):
        # Registers
        self.register_a = [0] * REGISTER_SIZE
        self.register_d = [0] * REGISTER_SIZE

        self.alu_out = [0] * REGISTER_SIZE

        self.pc = 0


    def execute_instruction(self, instruction: list, inM: list, reset: bool) -> list[list, bool, int, int]:
        """
            Method is executing any HACK instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value represented in binary list.
            :param reset: reset status.

            :return:    outM: list(Out Memory valuerepresented in binary list), 
                        writeM: bool(Write into a memory status), 
                        addressM: int (Address to writeM: int), 
                        PC: int(Program counter)
        """

        if reset:
            outM, writeM, addressM, pc = self.execute_instruction(instruction, inM, False)
            self.pc = 0
            return [outM, writeM, addressM, self.pc]


        if instruction[0] == 0:
            return self.execute_A_instruction(instruction, inM)

        else: 
            return self.execute_C_instruction(instruction, inM)


    def execute_A_instruction(self, instruction: list, inM: list) -> list[list, bool, int, int]:
        """
            Method is executing HACK A instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value represented in binary list.

            :return:    outM: list(Out Memory valuerepresented in binary list), 
                        writeM: bool(Write into a memory status), 
                        addressM: int (Address to writeM: int), 
                        PC: int(Program counter)
        """



        self.register_a = [0] + instruction[1:]
        self.pc += 1


        return [[0] * REGISTER_SIZE, False, convert_bin_to_dec(self.register_a), self.pc]


    def execute_C_instruction(self, instruction: list, inM: list) -> list[list, bool, int, int]:
        """
            Method is executing HACK C instruction on cpu

            :param instruction: list by size of 16 with only 1 and 0 representing an HACK instruction binary.
            :param inM: in memory value represented in binary list.

            
            :return:    outM: list(Out Memory valuerepresented in binary list), 
            writeM: bool(Write into a memory status), 
            addressM: int (Address to writeM: int), 
            PC: int(Program counter)
        """


        # Execute COMP command.
        comp = instruction[3:10]    
        self.alu_out = self.get_alu_out(comp, inM)    
        alu_out_dec = convert_bin_to_dec(self.alu_out)


        # Find zr and ng Flags
        zr = alu_out_dec == 0
        ng = alu_out_dec < 0


        # Calculate Jump for pc counter 
        jmp_status = self.get_jmp_status(instruction[13:], zr, ng)

        if jmp_status == True:
            self.pc = convert_bin_to_dec(self.register_a)
        else: 
            self.pc += 1


        # Calculate dest
        dest_a, dest_d, dest_m = self.get_dest(instruction[10: 13])

        if dest_a:
            self.register_a = self.alu_out.copy()

        if dest_d:
            self.register_d = self.alu_out.copy()

        return [self.alu_out.copy(), dest_m, convert_bin_to_dec(self.register_a), self.pc]


    def get_alu_out(self, comp: list, inM: list) -> list:
        """
            Method gots and "a c c c c c c" part of HACK instruction, inM value, and returns alu output.'

            :param comp: part of an istruction that related to alu output. [a, c, c, c, c, c, c]
            :param inM: inM value represented in binary. 

            :return: returns alu output -> in binary representation
        """

        if comp == COMP_0:
            self.alu_out = BINARY_ZERO.copy()

        elif comp == COMP_1:
            self.alu_out = BINARY_ONE.copy()

        elif comp == COMP_MINUS_1:
            self.alu_out = BINARY_MINUS_ONE.copy()

        elif comp == COMP_D:
            self.alu_out = self.register_d.copy()

        elif comp == COMP_A:
            self.alu_out = self.register_a.copy()

        elif comp == COMP_NOT_D:
            self.alu_out = Not16(self.register_d)

        elif comp == COMP_NOT_A:
            self.alu_out = Not16(self.register_a)

        elif comp == COMP_MINUS_D:
            self.alu_out = Not16(Add16(self.register_d, BINARY_MINUS_ONE))

        elif comp == COMP_MINUS_A:
            self.alu_out = Not16(Add16(self.register_a, BINARY_MINUS_ONE))

        elif comp == COMP_D_PLUS_ONE:
            # x + 1 = !(!x + 111...1)
            new_bin = Not16(self.register_d)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = Not16(new_bin)

        elif comp == COMP_A_PLUS_ONE:
            # x + 1 = !(!x + 111...1)
            new_bin = Not16(self.register_a)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = Not16(new_bin)

        elif comp == COMP_D_MINUS_ONE:
            self.alu_out = Add16(self.register_d, BINARY_MINUS_ONE)

        elif comp == COMP_A_MINUS_ONE:
            self.alu_out = Add16(self.register_a, BINARY_MINUS_ONE)


        elif comp == COMP_D_PLUS_A:
            self.alu_out = Add16(self.register_d, self.register_a)

        elif comp == COMP_D_MINUS_A:
            # x - y = !(!x + y)
            self.alu_out = Not16(Add16(Not16(self.register_d), self.register_a))

        elif comp == COMP_A_MINUS_D:
            # x - y = !(!x + y)
            self.alu_out = Not16(Add16(Not16(self.register_a), self.register_d))


        elif comp == COMP_D_AND_A:
            self.alu_out = And16(self.register_d, self.register_a)

        elif comp == COMP_D_OR_A:
            self.alu_out = Or16(self.register_d, self.register_a)


        elif comp == COMP_M:
            self.alu_out = inM.copy()

        elif comp == COMP_NOT_M:
            self.alu_out = Not16(inM)

        elif comp == COMP_MINUS_M:
            self.alu_out = Not16(Add16(inM, BINARY_MINUS_ONE))

        elif comp == COMP_M_PLUS_ONE:
            # x + 1 = !(!x + 111...1)
            new_bin = Not16(inM)
            new_bin = Add16(new_bin, BINARY_MINUS_ONE)

            self.alu_out = Not16(new_bin)

        elif comp == COMP_M_MINUS_ONE:
            self.alu_out = Add16(inM, BINARY_MINUS_ONE)

        elif comp == COMP_D_PLUS_M:
            self.alu_out = Add16(self.register_d, inM)

        elif comp == COMP_D_MINUS_M:
            # x - y = !(!x + y)
            self.alu_out = Not16(Add16(Not16(self.register_d), inM))

        elif comp == COMP_M_MINUS_D:
            self.alu_out = Not16(Add16(Not16(inM), self.register_d))

        elif comp == COMP_D_AND_M:
            self.alu_out = And16(inM, self.register_d)

        elif comp == COMP_D_OR_M:
            self.alu_out = Or16(inM, self.register_d)

        else:
            raise ValueError("Hack CPU error, instruction COMP not found! instruction: " + str(comp))


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
        self.register_a = [0] * REGISTER_SIZE
        self.register_d = [0] * REGISTER_SIZE

        self.alu_out = [0] * REGISTER_SIZE
        self.pc = 0
     