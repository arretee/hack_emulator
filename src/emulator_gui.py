import pygame


from src.hack_computer import HackComputer
from src.gui_config import *


from src.gui_panel import Panel


class EmulatorGUI:
    def __init__(self, hack_computer: HackComputer):
        # Pygame init
        pygame.init()

        # Create window
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        
        
        # Create panels and widgets
        self.panel_registers = Panel(
            pos = (552, 20),
            size = (450, 256),
            table_size = (4, 4),
            font= None,
            title = "Registers",
            data = [[0 for j in range(4)] for i in range(4)]
        )
        

        # Variables
        self.exit_status = False

    def update(self):
        self.panel_registers.update()
        
        
    def cover_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                self.exit_status = True
                return

    def run(self):
        # Work on events
        self.cover_events()
            
        # Fill background
        self.window.fill(COLOR_WINDOW_BACKGROUND)
        
        # Draw objects
        self.panel_registers.draw(self.window)


        self.clock.tick(WINDOW_FPS)

        pygame.display.update()




