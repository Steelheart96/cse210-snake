import pyray as pr
from Actors import Player
from Structs import PositionedString, Point, String

class PlayerPoints:
    '''
    Description: A class for instancing and displaying a player's points.

    Args:
    - player_to_monitor (Player): The player whos points are to be displayed
    - static_text (Positioned String): The string that is always going to be displayed directly before player points.
    '''

    def __init__(self, player_to_monitor: Player, static_text: String) -> None:
        self.player = player_to_monitor
        self.set_beginning_position(static_text)
        self.set_text()

    def set_beginning_position(self, static_text):
        self.text_length = pr.text_length(static_text.character)
        if self.player.player_num == 1:
            position = Point(pos_x = 1 * static_text.font_size, pos_y = 5)

        if self.player.player_num == 2:
            position = Point(pos_x = self.player.window.width - self.text_length * static_text.font_size, pos_y = 5)
            
            
        self.static_text = PositionedString(static_text.character, static_text.font_size, static_text.color, position)

    def set_text(self):
        '''
        Discription: Sets text that will always be the same on render.
        '''
        self.text = self.static_text.copy()
        self.text.character = f'{self.static_text.character} {str(self.player.player_points)}'

        self.text_length = pr.text_length(self.text.character)
        
    
    def draw_points(self):
        self.set_text()
        pr.draw_text(self.text.character, self.text.position.pos_x, self.text.position.pos_y, self.text.font_size, self.text.color)