import pygame
import sys

from src.gui_panel import Panel
from src.gui_screen import GuiScreen
from src.gui_config import *


from src.binary_functions import convert_bin_to_dec, convert_dec_to_bin
from src.hack_computer import HackComputer
import src.hack_config


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
        
        # Create Screen
        self.screen = GuiScreen((PANEL_GAP, PANEL_GAP), self.hack_computer)
        
        # Variables
        self.gui_speed = DEFALUT_GUI_SPEED
        self.exit_status = False
        
        self.current_file = "Mult.hack"
        
        self.run_hack_computer = False
        
        
    def create_panels(self):
        """
        Method creates panels for the gui
        """
        self.panel_registers = Panel(
            pos = PANEL_REGISTERS_POS,
            size = PANEL_REGISTERS_SIZE,
            
            text_title = PANEL_REGISTERS_TITLE,
            font_title = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_REGISTERS_TITLE_FONT_SIZE),
            pos_title = PANEL_REGISTERS_TITLE_POS,
            
            
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
            text_title = PANEL_RAM_TITLE,
            font_title = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_RAM_TITLE_FONT_SIZE),
            pos_title = PANEL_RAM_TITLE_POS,
            
            table_size= PANEL_RAM_TABLE_SIZE,
            table_data= PANEL_RAM_DATA_SAMPLE,
            table_colors= PANEL_RAM_COLORS,
            font_data= pygame.font.SysFont(PANEL_TEXT_FONT, PANEL_RAM_TEXT_FONT_SIZE),
        
        
            table_ratios_cols= PANEL_RAM_COLS_RATIOS,
            
            table_gaps= PANEL_RAM_GAPS,
            
            groups=[self.panels]
        )

        self.panel_rom = Panel(
            pos = PANEL_ROM_POS,
            size = PANEL_ROM_SIZE,
            text_title = PANEL_ROM_TITLE,
            font_title = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_ROM_TITLE_FONT_SIZE),
            pos_title = PANEL_ROM_TITLE_POS,
            
            table_size= PANEL_ROM_TABLE_SIZE,
            table_data= PANEL_ROM_DATA_SAMPLE,
            table_colors= PANEL_ROM_COLORS,
            font_data= pygame.font.SysFont(PANEL_TEXT_FONT, PANEL_ROM_TEXT_FONT_SIZE),
        
        
            table_ratios_cols= PANEL_ROM_COLS_RATIOS,
            
            table_gaps= PANEL_ROM_GAPS,
            
            groups=[self.panels]
        )
        
        self.panel_state = Panel(
            pos = PANEL_STATE_POS,
            size = PANEL_STATE_SIZE,
            text_title = PANEL_STATE_TITLE,
            font_title = pygame.font.SysFont(PANEL_TITLE_FONT, PANEL_STATE_TITLE_FONT_SIZE),
            pos_title = PANEL_STATE_TITLE_POS,
            
            table_size= PANEL_STATE_TABLE_SIZE,
            table_data= PANEL_STATE_DATA_SAMPLE,
            table_colors= PANEL_STATE_COLORS,
            font_data= pygame.font.SysFont(PANEL_TEXT_FONT, PANEL_STATE_TEXT_FONT_SIZE),
        
        
            table_ratios_cols= PANEL_STATE_COLS_RATIOS,
            
            table_gaps= PANEL_STATE_GAPS,
            
            groups=[self.panels]
        )
        

    def update(self):
        """ 
            Update the state of an emulator
        """
        # Update Panels data
        self.panel_registers.update_data(self.registers_panel_data())
        self.panel_ram.update_data(self.ram_panel_data())
        
        rom_data, rom_colors = self.rom_panel_data()
        self.panel_rom.update_data(data = rom_data, colors=rom_colors)
        
        state_data, state_colors = self.state_panel_data()
        self.panel_state.update_data(data = state_data, colors = state_colors)
        
        # Update screen
        self.screen.update()
        
        # Update draws panel
        self.panels.update()        
        
        
    def registers_panel_data(self):
        """
            Method create data for registers panel
            
            
            :return: returns matrix of strings by size of the panel registers with relevent data to state of hack computer
        """
        
        data = [["" for _ in range(self.panel_registers.table_size[1])] for __ in range(self.panel_registers.table_size[0])]
        
        
        for row in range(self.panel_registers.table_size[0]):
            # Get value by row
            if row == 0:
                # A Register
                value = convert_bin_to_dec(self.hack_computer.cpu.register_a)
            
            elif row == 1:
                # D Register
                value = convert_bin_to_dec(self.hack_computer.cpu.register_d)
                
            elif row == 2:
                # M ram Value
                value = convert_bin_to_dec(self.hack_computer.RAM[self.hack_computer.addressM])
            
            elif row == 3:
                # PC 
                value = self.hack_computer.pc
                
            else:
                # unknown row
                value = 0
                
                    
            
            for col in range(self.panel_registers.table_size[1]):
                # Get data by col and row value
                if col == 0:
                    data[row][col] = PANEL_REGISTERS_DATA_SAMPLE[row][col]
                    
                if col == 1:
                    data[row][col] = str(value)
                
                if col == 2:
                    data[row][col] = hex(value)
                    
                if col == 3:
                    data[row][col] = "".join([str(bit) for bit in convert_dec_to_bin(value)])
                
                    

        
        return data
        

    def ram_panel_data(self):
        """
            Method create data for ram panel
            
            :return: returns matrix of strings by size of the panel ram with relevent data to state of hack computer
        """
        
        
        # Get data for ram panel
        data = [["" for _ in range(self.panel_ram.table_size[1])] for __ in range(self.panel_ram.table_size[0])]
        
        for row in range(self.panel_ram.table_size[0]):
            for col in range(self.panel_ram.table_size[1]):
                if col == 0:
                    # ram number
                    data[row][col] = str(row)
                
                elif col == 1:
                    # ram name if exists
                    data[row][col] = get_ram_name(row)
                
                elif col == 2:
                    # decimal value
                    data[row][col] = str(convert_bin_to_dec(self.hack_computer.RAM[row]))
                    
                elif col == 3:
                    # hex value
                    data[row][col] = str(hex(convert_bin_to_dec(self.hack_computer.RAM[row])))
                    
                elif col == 4:
                    # bin value
                    data[row][col] = "".join([str(x) for x in self.hack_computer.RAM[row]])
                    
        return data
                                
    
    def rom_panel_data(self) -> list[list, list, int]:    
        """
            Method create data for rom panel
            
            :return: list by size of 3 -> [data matrix, colors matrix, select_row]
        """
        # Get center_pc(int) of table and selected row 
        if self.hack_computer.pc  + PANEL_ROM_TABLE_SIZE[0] / 2 > src.hack_config.ROM_SIZE - 1:
            center_pc = src.hack_config.ROM_SIZE - PANEL_ROM_TABLE_SIZE[0] / 2
            selected_row = PANEL_ROM_TABLE_SIZE[0] - (src.hack_config.ROM_SIZE - self.hack_computer.pc)
            
        
        elif self.hack_computer.pc - PANEL_ROM_TABLE_SIZE[0] / 2 < 0:
            center_pc = PANEL_ROM_TABLE_SIZE[0] / 2
            selected_row = self.hack_computer.pc
            
            
        else:
            center_pc = self.hack_computer.pc
            selected_row = self.hack_computer.pc - (center_pc - PANEL_ROM_TABLE_SIZE[0] / 2)
            
        
        # Get rom sublist for table
        rom_start = int(center_pc - PANEL_ROM_TABLE_SIZE[0] / 2)
        rom_end = int(center_pc + PANEL_ROM_TABLE_SIZE[0] / 2)
        
        rom = self.hack_computer.ROM[rom_start:rom_end]
        
        
        # Generate data and colors 
        data = [[None for _ in range(PANEL_ROM_TABLE_SIZE[1])] for __ in range(PANEL_ROM_TABLE_SIZE[0])]
        colors = [[COLOR_TEXT_DEFAULT for _ in range(PANEL_ROM_TABLE_SIZE[1])] for __ in range(PANEL_ROM_TABLE_SIZE[0])]
        
        
        for row in range(PANEL_ROM_TABLE_SIZE[0]):
            instruction = rom[row]
            
            
            for col in range(PANEL_ROM_TABLE_SIZE[1]):
                if col == 0:
                    data[row][col] = str(row + rom_start)

                if col == 1:
                    data[row][col] = "".join([str(x) for x in instruction])
                    
                if col == 2:
                    data[row][col] = src.hack_config.disassemble_instruction(instruction)
                
                # Change color of selected row
                if row == selected_row:
                    colors[row][col] = COLOR_TEXT_YELLOW
                    
        return [data, colors]

    
    def state_panel_data(self) -> list[list, list]:
        """ Method create data and colors fo state panel

        Returns:
            list[list, list]: list of 2 lists -> [data matrix, colors matrix]
        """
        
        
        speed = ((self.gui_speed // 100) - 1) * "-" + "*" + "-" * ((MAX_GUI_SPEED - self.gui_speed) // 100)
        speed = "low[" + speed + "]high" 
        
        
        colors = [[PANEL_STATE_COLORS[row][col] for col in range(PANEL_STATE_TABLE_SIZE[1])] for row in range(PANEL_STATE_TABLE_SIZE[0])]
        colors[1][1] = COLOR_TEXT_GREEN if self.run_hack_computer else COLOR_TEXT_RED
        
        data = [
            ["Program", self.current_file],
            ["State", PANEL_STATE_RUNNING if self.run_hack_computer else PANEL_STATE_PAUSED],
            ["Speed", speed],
        ]
        
        return [data, colors]


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
            
            if event.type == pygame.KEYUP:
                # Pause the program 
                if event.key == KEYBIND_PAUSE:
                    self.run_hack_computer = not self.run_hack_computer              

                # Change speed to higher
                if event.key == KEYBIND_INCREASE_SPEED:
                    self.gui_speed = min(MAX_GUI_SPEED, self.gui_speed + GUI_SPEED_CHANGE)
                
                # Change speed to lower.
                if event.key == KEYBIND_DECREASE_SPEED:
                    self.gui_speed = max(MIN_GUI_SPEED, self.gui_speed - GUI_SPEED_CHANGE)
                                

    def run(self):
        # Work on events
        self.events_handler()
        
        # Update all widgets 
        self.update()
            
        # Fill background
        self.window.fill(COLOR_WINDOW_BACKGROUND)
        
        # Draw objects
        self.panels.draw(self.window)
        self.window.blit(self.screen.image, self.screen.rect)
        
        

        # timeout for fps
        self.clock.tick(WINDOW_FPS)

        # Update dispaly
        pygame.display.update()




