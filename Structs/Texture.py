from pyray import Color
from Structs.Point import Point

class String:
    '''
    struct
    
    Args:
    - character (str): Text character
    - font_size (int): Text font size
    - color (pr.Color): Text font color
    '''
    
    def __init__(self, character: str, font_size: int, color: Color):
        self.character = character
        self.font_size = font_size
        self.color = color
    
    def __repr__(self) -> str:
        return f'Character("{self.character}","{self.font_size}", "{self.color}")'
    
    def __str__(self) -> str:
        return f'({self.character}, {self.font_size}, {self.color})'

class PositionedString(String):
    '''
    struct

    Args:
    - character (str): Text character
    - font_size (int): Text font size
    - color (pr.Color): Text font color
    - position (Point): Position (x,y) of text on screen
    '''

    def __init__(self, character: str, font_size: int, color: Color, position: Point):
        super().__init__(character, font_size, color)
        self.position = position
    
    def __repr__(self) -> str:
        return f'Character("{self.character}","{self.font_size}", "{self.color}", "{self.position}")'

    def __str__(self) -> str:
        return f'({self.character}, {self.font_size}, {self.color}, {self.position})'