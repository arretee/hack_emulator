from src.gui_config import * 

class TextSprite(pygame.sprite.Sprite):
    """
        Class for representing Text in pygame
    """
    def __init__(self,
                text: str,
                font: pygame.font.Font,
                color: str, 
                pos: list[int, int],
                
                groups = []
            ):
        super().__init__(groups)
        
        self.text = text
        self.pos = pos        
        self.color = color
        
        self.font = font
        
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect(topleft=pos)
        
        
    def change_text(self, text: str, color: str = None):
        """Method to change text of object

        Args:
            text (str): new text
        """
        
        if text != self.text or ((color is not None) and color != self.color):
            self.text = text
            
            self.image = self.font.render(text, True, self.color if color is None else color)
            self.rect = self.image.get_rect(topleft=self.pos)
