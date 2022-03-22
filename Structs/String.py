from pyray import Color

class String:
    '''
    struct
    
    Args:
    - character (str): Text character
    - font_size (int): Text font size
    - color (pr.Color): Text font color
    '''
    
    def __init__(self, string: str, font_size: int, color: Color):
        self.string = string
        self.font_size = font_size
        self.color = color

    def copy(self):
        return String(self.string, self.font_size, self.color)
    
    def __repr__(self) -> str:
        return f'String("{self.string}", {self.font_size}, Color({self.color}))'
    
    def __str__(self) -> str:
        return f'("{self.string}", {self.font_size}, {self.color})'