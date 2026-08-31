MAX_POSITIVE_VALUE = pow(2, 15) - 1

RAM_SIZE = 24577
ROM_SIZE = 32768

BINARY_ONE = [0] * 15 + [1]
BINARY_MINUS_ONE = [1] * 16
BINARY_ZERO = [0] * 16

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







