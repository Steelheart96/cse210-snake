from pyray import draw_text
from Actors import Player
from Structs import Point, String
from Tools.Tools import Tools

class PlayerPoints:
    '''
    Description: A class for instancing and displaying a player's points.

    Args:
    - player_to_monitor (Player): The player whos points are to be displayed
    - static_text (Positioned String): The string that is always going to be displayed directly before player points.
    '''

    def __init__(self, player_to_monitor: Player, static_text: String) -> None:
        self.player = player_to_monitor
        self.static_text = static_text
        self.string = Tools.combine_text(self.static_text.string, str(self.player.player_points))
        self.calculate_beginning_position()
        self.text = String(self.string, self.static_text.font_size, self.static_text.color)

    def calculate_beginning_position(self):
        '''
        Description: Calculates the position of the player scores.
        '''
        self.text_length = Tools.get_text_length(self.string, self.static_text.font_size)

        if self.player.player_num == 1:
            self.position = Point(pos_x = 1 * self.static_text.font_size, pos_y = 5)

        if self.player.player_num == 2:
            self.position = Point(pos_x = self.player.window.width - self.text_length, pos_y = 5)
    
    def draw_points(self):
        '''
        Description: Draws the player's points on the screen.
        '''
        self.text.string = Tools.combine_text(self.static_text.string, str(self.player.player_points))
        draw_text(self.text.string, self.position.pos_x, self.position.pos_y, self.text.font_size, self.text.color)