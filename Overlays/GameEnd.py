from Actors import Player
from Overlays.Overlay import Overlay
from Structs import Window, String, Point
import pyray as pr
from Tools.Tools import Tools

class GameEnd(Overlay):
    '''
    Description: The overlay that appears at the end of a game.

    Args:
    - window (Window): Window information
    - width (int): The width you want to overlay background to be
    - height (int): The height you want the overlay background to be
    - background_color (pr.Color): The color you want the overlay background to be
    - header (str): The words displayed at the top of the overlay
    - player1 (Player): Player 1 in the game
    - player2 (Player): Player 2 in the game
    '''

    def __init__(self, window: Window, width: int, height: int, background_color: pr.Color, header: String, player1: Player, player2: Player) -> None:
        super().__init__(window, width, height, background_color, header, player1, player2)
        

    def find_winner(self):
        '''
        Description: Finds the winner of the curent game.
        '''
        if self.player1.player_points > self.player2.player_points:
            self.winner_text = 'Winner: Player 1'

        elif self.player1.player_points < self.player2.player_points:
            self.winner_text = 'Winner: Player 2'
        
        else:
            self.winner_text = 'Else'