import pyray as pr
from Actors import Player
from Structs import PositionedString

class PlayerPoints:
    '''
    Description: A class for instancing and displaying a player's points.

    Args:
    - player_to_monitor (Player): The player whos points are to be displayed
    - static_text (Positioned String): The string that is always going to be displayed directly before player points.
    '''

    def __init__(self, player_to_monitor: Player, static_text: PositionedString) -> None:
        self.player = player_to_monitor
        self.static_text = static_text
        self.set_text()

    def set_text(self,):
        '''
        Discription: Sets text that will always be the same on render.
        '''
        self.text = self.static_text.copy()
        self.text.character = f'{self.static_text.character}: {str(self.player.player_points)}'
        
    
    def draw_points(self):
        # Transfer to Rectangle to dynamically set points display position?
        self.set_text()
        pr.draw_text(self.text.character, self.text.position.pos_x, self.text.position.pos_y, self.text.font_size, self.text.color)