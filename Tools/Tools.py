from pyray import Color, text_length
from Structs import PositionedString, Window, Point

class Tools:
    '''
    Description: Holds helpful functions.
    '''
    def combine_text(string1: str, string2: str) -> str:
        '''
        Discription: Sets text that will always be the same when rendering.

        Args:
        - string1 (str): a String to combine
        - string2 (str): a String to combine

        Returns:
        - str: The combined string
        '''
        return f'{string1} {string2}'

    def get_text_length(text: str, font_size: int) -> int:
        '''
        Description: Calculates the length of a string.

        Args:
        - text (str): A string
        - font_size (int): The font size of the string

        Returns:
        - int: The string length
        '''
        return text_length(text) * font_size

    def convert_to_positioned(text: str, font_size: int, color: Color, position: Point) -> PositionedString:
        '''
        Description: Converts a String struct to a PositionedString Struct.

        Args:
        - text (str): The string that will be stored
        - font_size (int): The font size of the string stored
        - color (pr.Color): The color of the string stored
        - position (point): The position of the string stored 

        Returns:
        - PositionedString: The structs created from PositionedString
        '''
        return PositionedString(text, font_size, color, position)

    def calculate_center(container_width: int, container_height: int, object_width: int, object_height: int) -> Point:
        '''
        Description: Finds the position where the object is centered on the screen.

        Args: 
        - container_width (int): The object container width
        - container_height (int): The object container height
        - object_width (int): The width of the object
        - object_height (int): the height of the object

        Returns:
        Point: The position where the object is centered on the screen 
        '''
        return Point(container_width // 2 - object_width // 2, container_height // 2 - object_height // 2)