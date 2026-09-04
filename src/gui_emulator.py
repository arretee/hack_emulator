import pygame
import sys

from src.hack_computer import HackComputer
from src.gui_config import *

from src.binary_functions import convert_bin_to_dec, convert_dec_to_bin


from src.gui_panel import Panel


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
        
        
        # Create panels
        self.panels = pygame.sprite.Group()
        self.create_panels()
        
        
        # Variables
        self.gui_speed = DEFALUT_GUI_SPEED
        self.exit_status = False
        
        
    def create_panels(self):
        """
        Method creates panels for the gui
        """
        self.panel_registers = Panel(
            pos = PANEL_REGISTERS_POS,
            size = PANEL_REGISTERS_SIZE,
            
            text_lable = PANEL_REGISTERS_TITLE,
            font_lable = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_REGISTERS_TITLE_FONT_SIZE),
            pos_lable = PANEL_REGISTERS_TITLE_POS,
            
            
            table_size = PANEL_REGISTERS_TABLE_SIZE,
            table_data = PANEL_REGISTERS_DATA_SAMPLE,
            table_colors = PANEL_REGISTERS_COLORS,
            font_data = pygame.font.SysFont(PANEL_TEXT_FONT, PANEL_REGISTERS_TEXT_FONT_SIZE),
            
            table_ratios_cols = PANEL_REGISTERS_COLS_RATIOS,

            table_gaps = PANEL_REGISTERS_GAPS,
            
            
            
            groups = [self.panels]            
        )
        
        
        self.panel_ram = Panel(
            pos = PANEL_RAM_POS,
            size = PANEL_RAM_SIZE,
            text_lable = PANEL_RAM_TITLE,
            font_lable = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_RAM_TITLE_FONT_SIZE),
            pos_lable = PANEL_RAM_TITLE_POS,
            
            table_size= PANEL_RAM_TABLE_SIZE,
            table_data= PANEL_RAM_DATA_SAMPLE,
            table_colors= PANEL_RAM_COLORS,
            font_data= pygame.font.SysFont(PANEL_TEXT_FONT, PANEL_RAM_TEXT_FONT_SIZE),
        
        
            table_ratios_cols= PANEL_RAM_COLS_RATIOS,
            
            table_gaps= PANEL_RAM_GAPS,
            
            groups=[self.panels]
        )


    def update(self):
        """ 
            Update the state of an emulator
        """
        self.panel_registers.update_data(self.registers_panel_data())
        self.panel_ram.update_data(self.ram_panel_data())
        
        
        self.panels.update()        
        
        
    def registers_panel_data(self):
        """
            Method create data for registers panel
            
            
            :return: returns matrix of strings by size of the panel registers with relevent data to state of hack computer
        """
        
        data = [["" for _ in range(self.panel_registers.table_size[1])] for __ in range(self.panel_registers.table_size[0])]
        
        
        for row in range(self.panel_registers.table_size[0]):
            if row == 0:
                value = convert_bin_to_dec(self.hack_computer.cpu.register_a)
            
            elif row == 1:
                value = convert_bin_to_dec(self.hack_computer.cpu.register_d)
                
            elif row == 2:
                value = convert_bin_to_dec(self.hack_computer.RAM[self.hack_computer.addressM])
            
            elif row == 3:
                value = self.hack_computer.pc
                
            else:
                value = 0
                
                    
            
            for col in range(self.panel_registers.table_size[1]):
                if col == 0:
                    data[row][col] = PANEL_REGISTERS_DATA_SAMPLE[row][col]
                    
                if col == 1:
                    data[row][col] = str(value)
                
                if col == 2:
                    data[row][col] = hex(value)
                    
                if col == 3:
                    data[row][col] = "".join([str(bit) for bit in convert_dec_to_bin(value)])
                
                else:
                    data[row][col] = str(value)
                    

        
        return data
        

    def ram_panel_data(self):
        """
            Method create data for ram panel
            
            :return: returns matrix of strings by size of the panel ram with relevent data to state of hack computer
        """
        
        data = [["" for _ in range(self.panel_ram.table_size[1])] for __ in range(self.panel_ram.table_size[0])]
        
        for row in range(self.panel_ram.table_size[0]):
            for col in range(self.panel_ram.table_size[1]):
                if col == 0:
                    data[row][col] = str(row)
                
                elif col == 1:
                    data[row][col] = get_ram_name(row)
                
                elif col == 2:
                    data[row][col] = str(convert_bin_to_dec(self.hack_computer.RAM[row]))
                    
                elif col == 3:
                    data[row][col] = str(hex(convert_bin_to_dec(self.hack_computer.RAM[row])))
                    
                elif col == 4:
                    data[row][col] = "".join([str(x) for x in self.hack_computer.RAM[row]])
                    
                    
        return data
                                
            

        
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
                return


    def run(self):
        # Work on events
        self.events_handler()
        
        # Update all widgets 
        self.update()
            
        # Fill background
        self.window.fill(COLOR_WINDOW_BACKGROUND)
        
        # Draw objects
        self.panels.draw(self.window)

        # timeout for fps
        self.clock.tick(WINDOW_FPS)

        # Update dispaly
        pygame.display.update()




