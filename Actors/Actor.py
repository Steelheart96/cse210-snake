from Structs import String, Window
from Actors.Load import Load

class Actor:
    '''
    Description: A Class that takes in a Character and a Window and sets a texture instance variable.

    Args:
    - display_char (String): String information to create a texture
    - window (Window): All window information
    '''

    def __init__(self, display_char: String, window: Window) -> None:
        self.display_char = display_char
        self.window = window
        self.Load_texture()

    def Load_texture(self):
        '''
        Description: Loads in an Actor Texture
        
        Uses: self.display_char (Character)
        '''
        self.texture = Load.text_to_texture(self.display_char.string, self.display_char.font_size, self.display_char.color)

    def draw(self):
        '''
       Description: Draws an Actor using the Actor's position and texture
        '''
        Load.draw_rectangle(self)