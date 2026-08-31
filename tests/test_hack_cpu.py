import pytest
from src.hack_cpu import HackCPU

# Helper functions to construct binary instruction arrays
def get_comp_bits(mnemonic: str) -> tuple[int, list[int]]:
    comp_map = {
        # a=0 (A-register ops)
        "0":     (0, [1, 0, 1, 0, 1, 0]),
        "1":     (0, [1, 1, 1, 1, 1, 1]),
        "-1":    (0, [1, 1, 1, 0, 1, 0]),
        "D":     (0, [0, 0, 1, 1, 0, 0]),
        "A":     (0, [1, 1, 0, 0, 0, 0]),
        "!D":    (0, [0, 0, 1, 1, 0, 1]),
        "!A":    (0, [1, 1, 0, 0, 0, 1]),
        "-D":    (0, [0, 0, 1, 1, 1, 1]),
        "-A":    (0, [1, 1, 0, 0, 1, 1]),
        "D+1":   (0, [0, 1, 1, 1, 1, 1]),
        "A+1":   (0, [1, 1, 0, 1, 1, 1]),
        "D-1":   (0, [0, 0, 1, 1, 1, 0]),
        "A-1":   (0, [1, 1, 0, 0, 1, 0]),
        "D+A":   (0, [0, 0, 0, 0, 1, 0]),
        "D-A":   (0, [0, 1, 0, 0, 1, 1]),
        "A-D":   (0, [0, 0, 0, 1, 1, 1]),
        "D&A":   (0, [0, 0, 0, 0, 0, 0]),
        "D|A":   (0, [0, 1, 0, 1, 0, 1]),
        # a=1 (M-memory ops)
        "M":     (1, [1, 1, 0, 0, 0, 0]),
        "!M":    (1, [1, 1, 0, 0, 0, 1]),
        "-M":    (1, [1, 1, 0, 0, 1, 1]),
        "M+1":   (1, [1, 1, 0, 1, 1, 1]),
        "M-1":   (1, [1, 1, 0, 0, 1, 0]),
        "D+M":   (1, [0, 0, 0, 0, 1, 0]),
        "D-M":   (1, [0, 1, 0, 0, 1, 1]),
        "M-D":   (1, [0, 0, 0, 1, 1, 1]),
        "D&M":   (1, [0, 0, 0, 0, 0, 0]),
        "D|M":   (1, [0, 1, 0, 1, 0, 1]),
    }
    return comp_map[mnemonic]

def get_dest_bits(mnemonic: str) -> list[int]:
    return [
        1 if "A" in mnemonic else 0,
        1 if "D" in mnemonic else 0,
        1 if "M" in mnemonic else 0,
    ]

def get_jump_bits(mnemonic: str) -> list[int]:
    jump_map = {
        "NULL": [0, 0, 0],
        "JGT":  [0, 0, 1],
        "JEQ":  [0, 1, 0],
        "JGE":  [0, 1, 1],
        "JLT":  [1, 0, 0],
        "JNE":  [1, 0, 1],
        "JLE":  [1, 1, 0],
        "JMP":  [1, 1, 1],
    }
    return jump_map[mnemonic]

def make_a_instr(value: int) -> list[int]:
    bits = [int(b) for b in f"{value & 0x7FFF:015b}"]
    return [0] + bits

def make_c_instr(comp: str, dest: str = "", jump: str = "NULL") -> list[int]:
    a_bit, comp_bits = get_comp_bits(comp)
    dest_bits = get_dest_bits(dest)
    jump_bits = get_jump_bits(jump)
    return [1, 1, 1, a_bit] + comp_bits + dest_bits + jump_bits


# Format: (areg, dreg, start_pc, reset, instruction, inM, exp_outM, exp_writeM, exp_addressM, exp_pc, exp_areg, exp_dreg, test_name)
test_data = [
    # --------------------------------------------------------------------------
    # 1. A-Instruction & Reset
    # --------------------------------------------------------------------------
    (0,  0, 0,  False, make_a_instr(21845), 0, 0, False, 21845, 1, 21845, 0, "A-Instruction: @21845"),
    (10, 0, 42, True,  make_a_instr(10),    0, 0, False, 10,    0, 10,    0, "Reset flag: PC goes to 0"),

    # --------------------------------------------------------------------------
    # 2. C-Instruction Computations (a=0)
    # --------------------------------------------------------------------------
    (10, 20, 0, False, make_c_instr("0"),      0, 0,    False, 10, 1, 10, 20, "COMP: 0"),
    (10, 20, 0, False, make_c_instr("1"),      0, 1,    False, 10, 1, 10, 20, "COMP: 1"),
    (10, 20, 0, False, make_c_instr("-1"),     0, -1,   False, 10, 1, 10, 20, "COMP: -1"),
    (10, 42, 0, False, make_c_instr("D"),      0, 42,   False, 10, 1, 10, 42, "COMP: D"),
    (20, 10, 0, False, make_c_instr("A"),      0, 20,   False, 20, 1, 20, 10, "COMP: A"),
    (10, 0,  0, False, make_c_instr("!D"),     0, -1,   False, 10, 1, 10, 0,  "COMP: !D"),
    (0,  10, 0, False, make_c_instr("!A"),     0, -1,   False, 0,  1, 0,  10, "COMP: !A"),
    (10, 5,  0, False, make_c_instr("-D"),     0, -5,   False, 10, 1, 10, 5,  "COMP: -D"),
    (15, 10, 0, False, make_c_instr("-A"),     0, -15,  False, 15, 1, 15, 10, "COMP: -A"),
    (10, 5,  0, False, make_c_instr("D+1"),   0, 6,    False, 10, 1, 10, 5,  "COMP: D+1"),
    (15, 10, 0, False, make_c_instr("A+1"),   0, 16,   False, 15, 1, 15, 10, "COMP: A+1"),
    (10, 5,  0, False, make_c_instr("D-1"),   0, 4,    False, 10, 1, 10, 5,  "COMP: D-1"),
    (15, 10, 0, False, make_c_instr("A-1"),   0, 14,   False, 15, 1, 15, 10, "COMP: A-1"),
    (20, 10, 0, False, make_c_instr("D+A"),   0, 30,   False, 20, 1, 20, 10, "COMP: D+A"),

    # areg, dreg, start_pc, reset, instruction, inM, exp_outM, exp_writeM, exp_addressM, exp_pc, exp_areg, exp_dreg, test_name
    (10, 30, 0, False, make_c_instr("D-A"),   0, 20,   False, 10, 1, 10, 30, "COMP: D-A"),
    (30, 10, 0, False, make_c_instr("A-D"),   0, 20,   False, 30, 1, 30, 10, "COMP: A-D"),
    (0x0F0F, 0x00FF, 0, False, make_c_instr("D&A"), 0, 0x000F, False, 0x0F0F, 1, 0x0F0F, 0x00FF, "COMP: D&A"),
    (0x0F00, 0x00FF, 0, False, make_c_instr("D|A"), 0, 0x0FFF, False, 0x0F00, 1, 0x0F00, 0x00FF, "COMP: D|A"),

    # --------------------------------------------------------------------------
    # 3. C-Instruction Computations (a=1)
    # --------------------------------------------------------------------------
    (99, 10, 0, False, make_c_instr("M"),     50, 50,  False, 99, 1, 99, 10, "COMP: M"),
    (99, 10, 0, False, make_c_instr("!M"),    0,  -1,  False, 99, 1, 99, 10, "COMP: !M"),
    (99, 10, 0, False, make_c_instr("-M"),    15, -15, False, 99, 1, 99, 10, "COMP: -M"),
    (99, 10, 0, False, make_c_instr("M+1"),  15, 16,  False, 99, 1, 99, 10, "COMP: M+1"),
    (99, 10, 0, False, make_c_instr("M-1"),  15, 14,  False, 99, 1, 99, 10, "COMP: M-1"),
    (99, 10, 0, False, make_c_instr("D+M"),  20, 30,  False, 99, 1, 99, 10, "COMP: D+M"),
    (99, 30, 0, False, make_c_instr("D-M"),  10, 20,  False, 99, 1, 99, 30, "COMP: D-M"),
    (99, 10, 0, False, make_c_instr("M-D"),  30, 20,  False, 99, 1, 99, 10, "COMP: M-D"),
    (99, 0x00FF, 0, False, make_c_instr("D&M"), 0x0F0F, 0x000F, False, 99, 1, 99, 0x00FF, "COMP: D&M"),
    (99, 0x00FF, 0, False, make_c_instr("D|M"), 0x0F00, 0x0FFF, False, 99, 1, 99, 0x00FF, "COMP: D|M"),

    # --------------------------------------------------------------------------
    # 4. Destinations
    # --------------------------------------------------------------------------
    (100, 200, 0, False, make_c_instr("D+1", dest=""),    0, 201, False, 100, 1, 100, 200, "DEST: None"),
    (100, 200, 0, False, make_c_instr("D+1", dest="M"),   0, 201, True,  100, 1, 100, 200, "DEST: M"),
    (100, 200, 0, False, make_c_instr("D+1", dest="D"),   0, 201, False, 100, 1, 100, 201, "DEST: D"),
    (100, 200, 0, False, make_c_instr("D+1", dest="DM"),  0, 201, True,  100, 1, 100, 201, "DEST: DM"),
    (100, 200, 0, False, make_c_instr("D+1", dest="A"),   0, 201, False, 201, 1, 201, 200, "DEST: A"),
    (100, 200, 0, False, make_c_instr("D+1", dest="AM"),  0, 201, True,  201, 1, 201, 200, "DEST: AM"),
    (100, 200, 0, False, make_c_instr("D+1", dest="AD"),  0, 201, False, 201, 1, 201, 201, "DEST: AD"),
    (100, 200, 0, False, make_c_instr("D+1", dest="ADM"), 0, 201, True,  201, 1, 201, 201, "DEST: ADM"),

    # --------------------------------------------------------------------------
    # 5. Jumps
    # --------------------------------------------------------------------------
    (500, 1,  10, False, make_c_instr("D", jump="JGT"), 0, 1,  False, 500, 500, 500, 1,  "JUMP: JGT success"),
    (500, 0,  10, False, make_c_instr("D", jump="JGT"), 0, 0,  False, 500, 11,  500, 0,  "JUMP: JGT fail (0)"),
    (500, -1, 10, False, make_c_instr("D", jump="JGT"), 0, -1, False, 500, 11,  500, -1, "JUMP: JGT fail (-1)"),
    (500, 0,  10, False, make_c_instr("D", jump="JEQ"), 0, 0,  False, 500, 500, 500, 0,  "JUMP: JEQ success"),
    (500, 5,  10, False, make_c_instr("D", jump="JEQ"), 0, 5,  False, 500, 11,  500, 5,  "JUMP: JEQ fail"),
    (500, 0,  10, False, make_c_instr("D", jump="JGE"), 0, 0,  False, 500, 500, 500, 0,  "JUMP: JGE success (0)"),
    (500, 1,  10, False, make_c_instr("D", jump="JGE"), 0, 1,  False, 500, 500, 500, 1,  "JUMP: JGE success (1)"),
    (500, -1, 10, False, make_c_instr("D", jump="JGE"), 0, -1, False, 500, 11,  500, -1, "JUMP: JGE fail"),
    (500, -5, 10, False, make_c_instr("D", jump="JLT"), 0, -5, False, 500, 500, 500, -5, "JUMP: JLT success"),
    (500, 0,  10, False, make_c_instr("D", jump="JLT"), 0, 0,  False, 500, 11,  500, 0,  "JUMP: JLT fail"),
    (500, -1, 10, False, make_c_instr("D", jump="JNE"), 0, -1, False, 500, 500, 500, -1, "JUMP: JNE success"),
    (500, 0,  10, False, make_c_instr("D", jump="JNE"), 0, 0,  False, 500, 11,  500, 0,  "JUMP: JNE fail"),
    (500, 0,  10, False, make_c_instr("D", jump="JLE"), 0, 0,  False, 500, 500, 500, 0,  "JUMP: JLE success (0)"),
    (500, -1, 10, False, make_c_instr("D", jump="JLE"), 0, -1, False, 500, 500, 500, -1, "JUMP: JLE success (-1)"),
    (500, 1,  10, False, make_c_instr("D", jump="JLE"), 0, 1,  False, 500, 11,  500, 1,  "JUMP: JLE fail"),
    (500, -5, 10, False, make_c_instr("D", jump="JMP"), 0, -5, False, 500, 500, 500, -5, "JUMP: JMP success"),
]


@pytest.mark.parametrize(
    "areg, dreg, start_pc, reset, instruction, inM, exp_outM, exp_writeM, exp_addressM, exp_pc, exp_areg, exp_dreg, test_name",
    test_data,
)
def test_cpu(
    areg, dreg, start_pc, reset, instruction, inM, exp_outM, exp_writeM, exp_addressM, exp_pc, exp_areg, exp_dreg, test_name
):
    cpu = HackCPU()

    cpu.register_a = areg
    cpu.register_d = dreg
    cpu.pc = start_pc

    outM, writeM, addressM, pc = cpu.execute_instruction(instruction, inM, reset)

    assert outM == exp_outM, "Assert outM: " + test_name
    assert writeM == exp_writeM, "Assert writeM: " + test_name
    assert addressM == exp_addressM, "Assert addressM: " + test_name
    assert pc == exp_pc, "Assert pc: " + test_name
    assert cpu.register_a == exp_areg, "Assert register_a: " + test_name
    assert cpu.register_d == exp_dreg, "Assert register_d: " + test_name