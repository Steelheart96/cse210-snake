import pyray as pr
from Actors.Player import Player
from Structs.Texture import String

class PointsOverlay:
    '''
    Description: A class for instancing and displaying a player's points.
    '''

    def __init__(self, player_to_monitor: Player, static_text: String) -> None:
        self.player = player_to_monitor
        self.set_static_text(static_text)

    def set_static_text(self, static_text: String):
        '''
        Discription: Sets text that will always be the same on render.
        '''
        self.static_text = static_text
    
    def draw_points(self):
        pr.draw_text(self.static_text)