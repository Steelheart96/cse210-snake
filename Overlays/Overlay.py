from Actors import Player
from Structs import String, Window, Point
from Tools.Tools import Tools
import pyray as pr

class Overlay:
    '''
    Description: Default program overlay class.

    Args:
    - window (Window): Window information
    - width (int): The width you want to overlay background to be
    - height (int): The height you want the overlay background to be
    - background_color (pr.Color): The color you want the overlay background to be
    '''

    def __init__(self, window: Window, width: int, height: int, background_color: pr.Color, header: String, player1: Player, player2: Player) -> None:
        self.window = window
        self.width = width
        self.height = height
        self.background_color = background_color
        self.header = header
        self.player1 = player1
        self.player2 = player2
        self.position = Tools.calculate_center(self.window.width, self.window.height, self.width, self.height)

    def draw_background(self):
        '''
        Description: Draws the background onto the screen.
        '''
        pr.draw_rectangle(self.position.pos_x, self.position.pos_y, self.width, self.height, self.background_color)
        pr.draw_rectangle_lines(self.position.pos_x, self.position.pos_y, self.width, self.height, pr.GRAY)

    def find_header_attributes(self):
        '''
        Description: Sets up header text and converts header text to a PositionedString.
        '''
        self.header_length = Tools.get_text_length(self.header.string, self.header.font_size)
        self.header_position = Point(self.width // 2 - self.header_length // 4 + self.position.pos_x, self.height // 4 + self.position.pos_y)
    
    def find_winner_attributes(self):
        '''
        Description: Sets up winner text and sets it as a PositionedString.
        '''
        self.winner_font_size = self.header.font_size // 2
        self.winner_length = Tools.get_text_length(self.winner_text, self.winner_font_size)
        self.winner_position = Point(self.width // 2 - self.winner_length // 4 + self.position.pos_x, self.height // 4 * 2 + self.position.pos_y)
        self.winner_color = pr.YELLOW

    def score_setup(self):
        '''
        Description: Sets score text as a PositionedString.
        '''
        self.create_score_strings()
        self.find_score_attributes()
        self.p_score_color = pr.RED

    def create_score_strings(self):
        '''
        Description: Creates the Score display for the End Overlay.
        '''
        self.static = 'Points: '
        self.p1_score_string = f'{self.static} {self.player1.player_points}'
        self.p2_score_string = f'{self.static} {self.player2.player_points}'
        self.score_font_size = self.header.font_size // 3
    
    def find_score_attributes(self):
        '''
        Description: Finds the Score text attributes for the End Overlay.
        '''
        self.score_length = Tools.get_text_length(self.p1_score_string, self.score_font_size)
        self.p1_score_position = Point(self.width // 4 - self.score_length // 2 + self.position.pos_x, self.height // 4 * 3 + self.position.pos_y)
        self.p2_score_position = Point(self.width // 4 * 3 + self.position.pos_x, self.height // 4 * 3 + self.position.pos_y)
    
    def get_text(self):
        '''
        Description: Sets up all of the text for the Game End Overlay.
        '''
        self.find_header_attributes()
        self.find_winner_attributes()
        self.score_setup()

    def draw_text(self):
        '''
        Description: Draws all of the text for the Game End Overlay.
        '''
        pr.draw_text(self.header.string, self.header_position.pos_x, self.header_position.pos_y, self.header.font_size, self.header.color)
        pr.draw_text(self.winner_text, self.winner_position.pos_x, self.winner_position.pos_y, self.winner_font_size, self.winner_color)
        pr.draw_text(self.p1_score_string, self.p1_score_position.pos_x, self.p1_score_position.pos_y, self.score_font_size, self.p_score_color)
        pr.draw_text(self.p2_score_string, self.p2_score_position.pos_x, self.p2_score_position.pos_y, self.score_font_size, self.p_score_color)
    
    def draw(self):
        '''
        Description: Calls all of the functions that create the End Overlay.
        '''
        self.get_text()
        self.draw_background()
        self.draw_text()