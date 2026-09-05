# -------------------------------------------- Hack Computer Constants --------------------------------------------
RAM_SIZE = 24577
ROM_SIZE = 32768
REGISTER_SIZE = 16

SCREEN_REGISTERS_NUM = 8192

R0 = 0
R1 = 1
R2 = 2
R3 = 3
R4 = 4
R5 = 5
R6 = 6
R7 = 7
R8 = 8
R9 = 9
R10 = 10
R11 = 11
R12 = 12
R13 = 13
R14 = 14
R15 = 15
SCREEN = 16384
KBD = 24756
    


# -------------------------------------------- Binary Constatnts --------------------------------------------
MAX_POSITIVE_VALUE = pow(2, 15) - 1

BINARY_ONE = [0] * 15 + [1]
BINARY_MINUS_ONE = [1] * 16
BINARY_ZERO = [0] * 16


# -------------------------------------------- Hack CPU constants --------------------------------------------
# COMP__ = [a, c, c, c, c, c, c]
# a = 0
COMP_0 =            [0, 1, 0, 1, 0, 1, 0]
COMP_1 =            [0, 1, 1, 1, 1, 1, 1]
COMP_MINUS_1 =      [0, 1, 1, 1, 0, 1, 0]
COMP_D =            [0, 0, 0, 1, 1, 0, 0]
COMP_A =            [0, 1, 1, 0, 0, 0, 0]
COMP_NOT_D =        [0, 0, 0, 1, 1, 0, 1]
COMP_NOT_A =        [0, 1, 1, 0, 0, 0, 1]
COMP_MINUS_D =      [0, 0, 0, 1, 1, 1, 1]
COMP_MINUS_A =      [0, 1, 1, 0, 0, 1, 1]
COMP_D_PLUS_ONE =   [0, 0, 1, 1, 1, 1, 1]
COMP_A_PLUS_ONE =   [0, 1, 1, 0, 1, 1, 1]
COMP_D_MINUS_ONE =  [0, 0, 0, 1, 1, 1, 0]
COMP_A_MINUS_ONE =  [0, 1, 1, 0, 0, 1, 0]
COMP_D_PLUS_A =     [0, 0, 0, 0, 0, 1, 0]
COMP_D_MINUS_A =    [0, 0, 1, 0, 0, 1, 1]
COMP_A_MINUS_D =    [0, 0, 0, 0, 1, 1, 1]
COMP_D_AND_A =      [0, 0, 0, 0, 0, 0, 0]
COMP_D_OR_A =       [0, 0, 1, 0, 1, 0, 1]

# a = 1
COMP_M =            [1, 1, 1, 0, 0, 0, 0]
COMP_NOT_M =        [1, 1, 1, 0, 0, 0, 1]
COMP_MINUS_M =      [1, 1, 1, 0, 0, 1, 1]
COMP_M_PLUS_ONE =   [1, 1, 1, 0, 1, 1, 1]
COMP_M_MINUS_ONE =  [1, 1, 1, 0, 0, 1, 0]
COMP_D_PLUS_M =     [1, 0, 0, 0, 0, 1, 0]
COMP_D_MINUS_M =    [1, 0, 1, 0, 0, 1, 1]
COMP_M_MINUS_D =    [1, 0, 0, 0, 1, 1, 1]
COMP_D_AND_M =      [1, 0, 0, 0, 0, 0, 0]
COMP_D_OR_M =       [1, 0, 1, 0, 1, 0, 1]



# Jumps configure 
# jmp = [j, j ,j]
JUMP_NULL = [0, 0, 0]
JUMP_JGT  = [0, 0, 1]
JUMP_JEQ  = [0, 1, 0]
JUMP_JGE  = [0, 1, 1]
JUMP_JLT  = [1, 0, 0]
JUMP_JNE  = [1, 0, 1]
JUMP_JLE  = [1, 1, 0]
JUMP_JMP  = [1, 1, 1]








# -------------------------------------------- Disassemle Functions --------------------------------------------
from src.binary_functions import convert_bin_to_dec

def get_comp_by_sublist(sublist: list) -> str:
    """ Function converts sublit of a c c c c c c from hack instruction to string comp

    Args:
        sublist (list): part of instruction that creates comp [a, c, c, c, c, c, c]

    Returns:
        str: str comp
    """
    if sublist == [0, 1, 0, 1, 0, 1, 0]: return "0"
    if sublist == [0, 1, 1, 1, 1, 1, 1]: return "1"
    if sublist == [0, 1, 1, 1, 0, 1, 0]: return "-1"
    if sublist == [0, 0, 0, 1, 1, 0, 0]: return "D"
    if sublist == [0, 1, 1, 0, 0, 0, 0]: return "A"
    if sublist == [0, 0, 0, 1, 1, 0, 1]: return "!D"
    if sublist == [0, 1, 1, 0, 0, 0, 1]: return "!A"
    if sublist == [0, 0, 0, 1, 1, 1, 1]: return "-D"
    if sublist == [0, 1, 1, 0, 0, 1, 1]: return "-A"
    if sublist == [0, 0, 1, 1, 1, 1, 1]: return "D+1"
    if sublist == [0, 1, 1, 0, 1, 1, 1]: return "A+1"
    if sublist == [0, 0, 0, 1, 1, 1, 0]: return "D-1"
    if sublist == [0, 1, 1, 0, 0, 1, 0]: return "A-1"
    if sublist == [0, 0, 0, 0, 0, 1, 0]: return "D+A"
    if sublist == [0, 0, 1, 0, 0, 1, 1]: return "D-A"
    if sublist == [0, 0, 0, 0, 1, 1, 1]: return "A-D"
    if sublist == [0, 0, 0, 0, 0, 0, 0]: return "D&A"
    if sublist == [0, 0, 1, 0, 1, 0, 1]: return "D|A"
    if sublist == [1, 1, 1, 0, 0, 0, 0]: return "M"
    if sublist == [1, 1, 1, 0, 0, 0, 1]: return "!M"
    if sublist == [1, 1, 1, 0, 0, 1, 1]: return "-M"
    if sublist == [1, 1, 1, 0, 1, 1, 1]: return "M+1"
    if sublist == [1, 1, 1, 0, 0, 1, 0]: return "M-1"
    if sublist == [1, 0, 0, 0, 0, 1, 0]: return "D+M"
    if sublist == [1, 0, 1, 0, 0, 1, 1]: return "D-M"
    if sublist == [1, 0, 0, 0, 1, 1, 1]: return "M-D"
    if sublist == [1, 0, 0, 0, 0, 0, 0]: return "D&M"
    if sublist == [1, 0, 1, 0, 1, 0, 1]: return "D|A"

def get_jump_by_sublist(sublist: list) -> str:
    """ Function converts sublit of [j, j, j] from hack instruction to string jump

    Args:
        sublist (list): part of instruction that creates jump [j, j, j]

    Returns:
        str: str jump
    """
    
    if sublist == [0, 0, 0]: return ""
    if sublist == [0, 0, 1]: return "JGT"
    if sublist == [0, 1, 0]: return "JEQ"
    if sublist == [0, 1, 1]: return "JGE"
    if sublist == [1, 0, 0]: return "JLG"
    if sublist == [1, 0, 1]: return "JNE"
    if sublist == [1, 1, 0]: return "JLE"
    if sublist == [1, 1, 1]: return "JMP"

    
def dissasemble_A_instruction(instruction: list) -> str:
    """ Function dissasebles the A hack instruction from binary to str

    Args:
        instruction (list): instruction from 16 bits
    """


    return "@" + str(convert_bin_to_dec(instruction))

def dissasemble_C_instruction(instruction: list) -> str:
    """ Function dissasebles the C hack instruction from binary to str

    Args:
        instruction (list): instruction from 16 bits
    """
    
    dest = ""    
    
    # Dest 
    if instruction[10] == 1:
        dest += "A"
        
    if instruction[11] == 1:
        dest += "D"
        
    if instruction[12] == 1:
        dest += "M"
        
    if dest != "":
        dest += "="
        
    comp = get_comp_by_sublist(instruction[3:10])
    jump = get_jump_by_sublist(instruction[13:16])
    
    if jump != "":
        jump = ";" + jump
        
    return dest + comp + jump
 
def disassemble_instruction(instruction: list) -> str:
    """ Function dissasebles hack instruction from binary to str

    Args:
        instruction (list): instruction from 16 bits
    """

    if instruction[0]:
        return dissasemble_C_instruction(instruction)
    
    else:
        return dissasemble_A_instruction(instruction)   