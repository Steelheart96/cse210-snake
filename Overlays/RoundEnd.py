from Actors import Player
from Overlays.Overlay import Overlay
from Structs import String, Window
import pyray as pr


class RoundEnd(Overlay):
    '''
    Description: The overlay that appears at the end of a round.

    Args:
    - window (Window): Window information
    - width (int): The width you want to overlay background to be
    - height (int): The height you want the overlay background to be
    - background_color (pr.Color): The color you want the overlay background to be
    '''

    def __init__(self, window: Window, width: int, height: int, background_color: pr.Color, header: String, player1: Player, player2: Player) -> None:
        super().__init__(window, width, height, background_color, header, player1, player2)

    def find_winner(self, winner_text: str):
        self.winner_text = winner_text