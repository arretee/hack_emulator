import pygame
import sys

from src.hack_computer import HackComputer
from src.gui_config import *


from src.gui_panel import PanelRegisters


class GuiEmulator:
    """
        Gui Emulator of an Hack Computer
    """
    def __init__(self, hack_computer: HackComputer):
        """
        Args:
            hack_computer (HackComputer): HackComputer unit
        """
        # Pygame init
        pygame.init()
        
        self.hack_computer = hack_computer

        # Create window
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        
        
        # Create panels and widgets
        self.panel_registers = PanelRegisters(
            pos = PANEL_REGISTERS_POS,
            size = PANEL_REGISTERS_SIZE,
            table_size = PANEL_REGISTERS_TABLE_SIZE,
            font= pygame.font.SysFont("monospace", 15),
            title = "Registers",
            data = [["0" for j in range(4)] for i in range(4)],
            gaps = PANEL_REGISTERS_GAPS,
            cols_ratios=PANEL_REGISTERS_COLS_RATIOS
        )
        

        # Variables
        self.exit_status = False

    def update(self):
        """ 
            Update the state of an emulator
        """
        self.panel_registers.update()
        
        
    def events_handler(self):
        """
            Function cover events handling for gui emulator
            Must be called every frame for correct work
        """
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self.exit_status = True
                return

    def run(self):
        # Work on events
        self.events_handler()
        
        # Update all widgets 
        self.update()
            
        # Fill background
        self.window.fill(COLOR_WINDOW_BACKGROUND)
        
        # Draw objects
        self.panel_registers.draw(self.window)

        # timeout for fps
        self.clock.tick(WINDOW_FPS)

        # Update dispaly
        pygame.display.update()




