from Actors import Player
from Structs import PositionedString
from Overlays.PlayerPoints import PlayerPoints

class PointsDisplay(PlayerPoints):
    '''
    Description: A class for holding, managing, and displaying all player's points.


    Args:
    - player_to_monitor (Player): The player whos points are to be displayed
    - static_text (Positioned String): The string that is always going to be displayed directly before player points.
    '''

    def __init__(self, player_to_monitor: Player, static_text: PositionedString) -> None:
        super().__init__(player_to_monitor, static_text)