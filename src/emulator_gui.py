import pygame


from src.hack_computer import HackComputer
from src.gui_config import *


class EmulatorGUI:
    def __init__(self, hack_computer: HackComputer):
        # Pygame init
        pygame.init()

        # Create window
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        # Variables
        self.exit_status = False



    def run(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                self.exit_status = True
                return

        self.clock.tick(WINDOW_FPS)

        self.window.fill(COLOR_WINDOW_BACKGROUND)
        pygame.display.update()




