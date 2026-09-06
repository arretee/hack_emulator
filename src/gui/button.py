import pygame

class Button(pygame.sprite.Sprite):
    """
        Class that represent button. 
        Give function to call back
        Update with param of mouse pos to update visual of an button
    """

    def __init__(self, pos:list, size: list, text: str, font: pygame.font, borders_size:int, main_color:str, second_color: str, text_color: str, border_color: str, func = None, groups = []):

        
        super().__init__(groups)
        
        
        self.text = text
        self.font = font
        
        self.main_color = main_color
        self.second_color = second_color
        self.text_color = text_color
        self.border_color = border_color
        
        self.size = size
        
        # Call Back function
        self.func = func
        
        # ---------- Sprite General ----------
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(topleft=pos)
        
        
        # ---------- Setup ----------
        self.background_image = pygame.Surface((self.size[0] - borders_size, self.size[1] - borders_size))
        self.background_image.fill(self.main_color)
        self.background_rect = self.background_image.get_rect(topleft = (borders_size / 2, borders_size / 2))
        
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_image.get_rect(center = (self.size[0] / 2, self.size[1]/2))
        
        # Draw button it self
        self.image.fill(self.border_color)
        self.image.blit(self.background_image, self.background_rect)
        self.image.blit(self.text_image, self.text_rect)
        
        # Ready second color for an updates
        self.background_second_image = pygame.Surface((self.size[0] - borders_size, self.size[1] - borders_size))
        self.background_second_image.fill(self.second_color)
        self.background_second_rect = self.background_second_image.get_rect(topleft = (borders_size / 2, borders_size / 2))
    
    
    def call_function(self):
        """
            Method call the function that was saved inside button
        """
        if self.func != None:
            self.func()
        
    def update(self, mouse_pos):
        """ Function is updating button view by mouse position on the screen

        Args:
            mouse_pos (tuple): (x, y) of mouse position on the screen
        """
        if self.rect.collidepoint(mouse_pos):
            self.image.fill(self.border_color)  # border
            self.image.blit(self.background_second_image, self.background_second_rect)  # background
            self.image.blit(self.text_image, self.text_rect)  # text
        else:
            self.image.fill(self.border_color)  # border
            self.image.blit(self.background_image, self.background_rect)  # background
            self.image.blit(self.text_image, self.text_rect)  # text
        
    