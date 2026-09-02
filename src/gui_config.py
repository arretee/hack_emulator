import pygame
# Constatns Values
        
# -------------------------------------------- Window --------------------------------------------
WINDOW_SIZE = (1280, 720)
WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW_SIZE
WINDOW_TITLE = "Hack Computer Emulator"

WINDOW_FPS = 120


# --------------------------------------------- Fonts ---------------------------------------------


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
COLOR_WINDOW_BACKGROUND = "#12141a"



# --------------------------------------------- Widgets --------------------------------------------
PANEL_GAP = 20
EMPTY = None

EMULATOR_SCREEN_SIZE = (512, 256)
EMULATOR_SCREEN_WIDTH, EMULATOR_SCREEN_HEIGHT = EMULATOR_SCREEN_SIZE

# Panel Registers
PANEL_REGISTERS_POS = (PANEL_GAP + EMULATOR_SCREEN_WIDTH + PANEL_GAP + PANEL_GAP, 0)
PANEL_REGISTERS_SIZE = (450, 256)
PANEL_REGISTERS_TABLE_SIZE = (4, 4)

PANEL_REGISTERS_TITLE = "Registers"
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

PANEL_REGISTERS_A_ROW = 0
PANEL_REGISTERS_D_ROW = 1
PANEL_REGISTERS_M_ROW = 2
PANEL_REGISTERS_PC_ROW = 3

PANEL_REGISTERS_COLS_RATIOS = [
    4, 5, 6, 16
]
PANEL_REGISTERS_GAPS = (10, 10)


