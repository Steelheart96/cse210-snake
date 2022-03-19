from Structs import Point
from Structs.String import String
from pyray import Color


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

    def copy(self):
        return PositionedString(self.character, self.font_size, self.color, self.position)
    
    def __repr__(self) -> str:
        return f'Character("{self.character}", {self.font_size}, Color{self.color}, {repr(self.position)})'

    def __str__(self) -> str:
        return f'("{self.character}", {self.font_size}, {self.color}, {self.position})'