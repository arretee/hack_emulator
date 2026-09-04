import pygame

from src.hack_config import R0, R15, SCREEN, KBD

# Constatns Values
        
# -------------------------------------------- Window --------------------------------------------
WINDOW_SIZE = (1280, 720)
WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW_SIZE
WINDOW_TITLE = "Hack Computer Emulator"

WINDOW_FPS = 120


# --------------------------------------------- Fonts ---------------------------------------------


# --------------------------------------------- GUI ---------------------------------------------
MAX_GUI_SPEED = 1000
DEFALUT_GUI_SPEED = 500
MIN_GUI_SPEED = 10

# -------------------------------------------- Colors --------------------------------------------
COLOR_TEXT_TITLE = "#7a8294" 
COLOR_TEXT_DEFAULT = "#bcc0c8"
COLOR_TEXT_YELLOW = "#dc9949" 
COLOR_TEXT_BLUE = "#64b4e6"
COLOR_TEXT_GREEN = "#71bc83"
COLOR_TEXT_RED = "#800020"

COLOR_SCREEN_DEFAULT = "#ffffff"
COLOR_SCREEN_BLACK = "#000000"

COLOR_PANEL_BACKGROUND = "#343c4e"
COLOR_PANEL_BORDER= "#ffffff"
COLOR_PANEL_CHOOSE_ROW = "#ffffff"

COLOR_WINDOW_BACKGROUND = "#12141a"



# --------------------------------------------- Widgets --------------------------------------------
PANEL_GAP = 20
EMPTY = None

EMULATOR_SCREEN_SIZE = (512, 256)
EMULATOR_SCREEN_WIDTH, EMULATOR_SCREEN_HEIGHT = EMULATOR_SCREEN_SIZE


PANEL_TITLE_FONT = "David"
PANEL_TEXT_FONT = "Arial"


# Panel Registers
PANEL_REGISTERS_POS = (PANEL_GAP + EMULATOR_SCREEN_WIDTH + PANEL_GAP, PANEL_GAP)
PANEL_REGISTERS_SIZE = (450, 256)
PANEL_REGISTERS_TABLE_SIZE = (4, 4)

PANEL_REGISTERS_TITLE = "Registers"
PANEL_REGISTERS_TITLE_FONT_SIZE = 35
PANEL_REGISTERS_TITLE_POS = (10, 10)

PANEL_REGISTERS_TEXT_FONT_SIZE = 15

PANEL_REGISTERS_DATA_SAMPLE = [
    ["A",  "0", "0x0000", "0" * 16],
    ["D",  "0", "0x0000", "0" * 16],
    ["M",  "0", "0x0000", "0" * 16],
    ["PC", "0", "0x0000", "0" * 16],
]
PANEL_REGISTERS_COLORS = [
    [COLOR_TEXT_TITLE, COLOR_TEXT_BLUE, COLOR_TEXT_BLUE, COLOR_TEXT_BLUE],
    [COLOR_TEXT_TITLE, COLOR_TEXT_BLUE, COLOR_TEXT_BLUE, COLOR_TEXT_BLUE],
    [COLOR_TEXT_TITLE, COLOR_TEXT_YELLOW, COLOR_TEXT_YELLOW, COLOR_TEXT_YELLOW],
    [COLOR_TEXT_TITLE, COLOR_TEXT_DEFAULT, COLOR_TEXT_DEFAULT, COLOR_TEXT_DEFAULT],
]

PANEL_REGISTERS_COLS_RATIOS = [
    4, 5, 6, 16
]

PANEL_REGISTERS_GAPS = (15, 30)


# Panel RAM 
def get_ram_name(address: int):
    """
        Function to get ram name if exists
    """
    if 0 <= address <= 15:
        return f"R{address}"
    
    elif SCREEN <= address < KBD:
        return f"Screen {address - SCREEN}"
    
    elif address == KBD:
        return "KBD"
    
    return ""       

PANEL_RAM_SIZE = (
    512,
    WINDOW_HEIGHT - PANEL_GAP * 3 - EMULATOR_SCREEN_HEIGHT
)

PANEL_RAM_POS = (
    PANEL_GAP,
    PANEL_GAP * 2 + EMULATOR_SCREEN_HEIGHT
)

PANEL_RAM_TABLE_SIZE = (16, 5)

PANEL_RAM_TITLE = "RAM"
PANEL_RAM_TITLE_FONT_SIZE = 35
PANEL_RAM_TITLE_POS = (10, 10)

PANEL_RAM_TEXT_FONT_SIZE = 15

PANEL_RAM_DATA_SAMPLE = [
    [str(i), get_ram_name(i), "0", "0x0", "0" * 16] for i in range(PANEL_RAM_TABLE_SIZE[0])
]
PANEL_RAM_COLORS = [
    [COLOR_TEXT_DEFAULT for _ in range(PANEL_RAM_SIZE[1])] for __ in range(PANEL_RAM_SIZE[0])
]
PANEL_RAM_COLS_RATIOS = [
    5, 10, 5, 6, 16
]

PANEL_RAM_GAPS = (10, 10)


# Panel ROM
PANEL_ROM_SIZE = (
    350,
    WINDOW_HEIGHT - PANEL_GAP * 3 - PANEL_REGISTERS_SIZE[1]
)

PANEL_ROM_POS = (
    PANEL_GAP + EMULATOR_SCREEN_WIDTH + PANEL_GAP,
    PANEL_GAP * 2 + PANEL_REGISTERS_SIZE[1]
)

PANEL_ROM_TABLE_SIZE = (20, 3)

PANEL_ROM_TITLE = "ROM {disassemble live}"
PANEL_ROM_TITLE_FONT_SIZE = 35
PANEL_ROM_TITLE_POS = (10, 10)

PANEL_ROM_TEXT_FONT_SIZE = 15

PANEL_ROM_DATA_SAMPLE = [
    ["0", "0000000000000000", ""] for _ in range(PANEL_ROM_SIZE[0])
]
PANEL_ROM_COLORS = [
    [COLOR_TEXT_DEFAULT for _ in range(PANEL_ROM_TABLE_SIZE[1])] for __ in range(PANEL_ROM_SIZE[0])
]
PANEL_ROM_COLS_RATIOS = [5, 16, 8]

PANEL_ROM_GAPS = (10, 10)
