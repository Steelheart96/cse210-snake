import pyray as pr
from Overlays.GameEnd import GameEnd
from Overlays.RoundEnd import RoundEnd
from Structs import Window, String, PopUp
from Handlers.PlayerHandler import PlayerHandler, Player
from Handlers.TailHandler import TailHandler
from Points.PlayerPoints import PlayerPoints

class Game:
    '''
    Description: The class that runs and manages the higher level program operations.

    Args:
    - window (Window): The program window's information
    - font_size (int): The size of the players and their trails
    - point_update_amount (int): The amount of points that a player recieves for getting the other player to hit their tail
    - player_head_char (str): The character that the player head is displayer as
    - round_recap_length (int): The amount of time the Round recap stays on screen (in seconds)
    - end_recap_length (int): The amount of time the End recap stays on screen (in seconds)
    '''

    def __init__(self, window: Window, font_size: int, point_update_amount: int, player_head_char: str, round_recap_length: int, end_recap_length: int) -> None:
        self.window = window
        self.font_size = font_size
        self.point_update_amount = point_update_amount
        self.player_head = player_head_char
        self.round_recap_length = round_recap_length
        self.end_recap_length = end_recap_length
        self.function_setup()

    def function_setup(self):
        '''
        Description: Holds all game classes on start functions.
        '''
        self.setup_window()
        self.setup_players()
        self.setup_player_points()
        self.setup_player_tails()
        self.calculate_overlay_size()
        self.setup_overlays()

    def setup_window(self):
        '''
        Description: Sets up the program window.
        '''
        pr.init_window(*self.window.get_pr_window_info())
        pr.set_target_fps(self.window.fps_cap)

    def setup_players(self):
        '''
        Description: Sets up all players.
        '''
        self.players = PlayerHandler()
        self.player_char = String(self.player_head, self.font_size, pr.GREEN)
        self.p1 = self.players.add('p1', [1, self.player_char, self.window])
        self.p2 = self.players.add('p2', [2, self.player_char, self.window])
        
    
    def setup_player_points(self):
        '''
        Description: Sets up all player point trackers.
        '''
        Player.set_point_update_amout(self.point_update_amount)
        self.player_1_points = PlayerPoints(self.p1, String("Player 1: ", self.font_size, pr.RED))
        self.player_2_points = PlayerPoints(self.p2, String("Player 2: ", self.font_size, pr.BLUE))

    def setup_player_tails(self):
        '''
        Description: Sets up all player trails.
        '''
        self.tails = TailHandler()
        TailHandler.set_tail_timer(3, self.window.fps_cap)
        self.t1 = self.tails.add('t1', [self.p1, self.p2, String('#', self.font_size, pr.RED), self.window])
        self.t2 = self.tails.add('t2', [self.p2, self.p1, String('#', self.font_size, pr.BLUE), self.window])

    def setup_overlays(self):
        '''
        Description: Sets up end of round recap overlay.
        '''
        end_header = String("Game End", self.font_size * 3, pr.BLUE)
        round_header = String("Round End",  self.font_size * 3, pr.GREEN)
        self.round_overlay = RoundEnd(self.window, self.overlay_size.width, self.overlay_size.height, pr.BLACK, round_header, self.p1, self.p2)

        self.end_overlay = GameEnd(self.window, self.overlay_size.width, self.overlay_size.height, pr.BLACK, end_header, self.p1, self.p2)
    
    def calculate_overlay_size(self):
        '''
        Description: Calculates the size of an overlay for a single run of the program.
        '''
        self.overlay_size = PopUp(self.window.width // 3 + self.window.width // 4, self.window.height // 3 + self.window.height // 4)

    def play_game(self) -> bool:
        '''
        Description: The program's game loop.

        Returns:
        - bool: Whether or not entire program continues
        '''
        run = True
        while not pr.window_should_close() and run:

            # collision detection (True = Hit, False = No Hit)
            self.p2_collided = self.t1.player_collision()
            self.p1_collided = self.t2.player_collision()

            # movement updates
            self.players.update()
            self.tails.update()

            pr.begin_drawing()
            pr.clear_background(pr.BLACK)

            self.player_2_points.draw_points()
            self.player_1_points.draw_points()

            # draw onscreen
            self.tails.draw()
            self.players.draw()

            pr.end_drawing()

            if self.p2_collided or self.p1_collided:
                run = False
        
        if run:
            self.close_window()
        else:
            return True
    
    def update_points(self):
        '''
        Description: Updates the player's points.
        '''
        if self.p2_collided:
            self.p1.update_player_points()
            self.round_overlay.find_winner('Player 1')

        if self.p1_collided:
            self.p2.update_player_points()
            self.round_overlay.find_winner('Player 2')
    
    def set_recap_length(self, recap_length):
        return recap_length * self.window.fps_cap

    def round_end(self) -> bool:
        '''
        Description: The Round end loop.

        Returns:
        - bool: Whether or not entire program continues
        '''
        self.update_points()

        self.players.reset()
        self.tails.reset()

        self.recap_length = self.set_recap_length(self.round_recap_length)

        run = True
        while not pr.window_should_close() and run and (self.p1.player_points < 3 and self.p2.player_points <3):
            pr.begin_drawing()
            pr.clear_background(pr.BLACK)

            # draw onscreen
            self.tails.draw()
            self.players.draw()
            self.round_overlay.draw()

            pr.end_drawing()

            if self.recap_length <= 0:
                run = False
            else:
                self.recap_length -= 1
        
        if run and not (self.p1.player_points <= 3 or self.p2.player_points <= 3):
            return False
        else:
            return True
    
    def game_end(self) -> bool:
        '''
        Description: The Game end loop.

        Returns:
        - bool: Whether or not entire program continues
        '''
        self.recap_length = self.set_recap_length(self.end_recap_length)
        self.end_overlay.find_winner()

        run = True
        while not pr.window_should_close() and run:
            pr.begin_drawing()
            pr.clear_background(pr.BLACK)

            # draw onscreen
            self.tails.draw()
            self.players.draw()
            self.end_overlay.draw()

            pr.end_drawing()

            if self.recap_length <= 0:
                run = False
            else:
                self.recap_length -= 1

        return False
    
    def close_window(self):
        '''
        Description: Closes program window.
        '''
        pr.close_window()