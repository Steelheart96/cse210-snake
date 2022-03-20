import pyray as pr
from Structs import Window, String
from Handlers.PlayerHandler import PlayerHandler, Player
from Overlays.PlayerPoints import PlayerPoints
from Handlers.TailHandler import TailHandler

class Game:
    '''
    Description: The class that runs and manages the higher level program operations.
    '''

    def __init__(self, window: Window, font_size: int, point_update_amount: int, player_head_char: str) -> None:
        self.window = window
        self.font_size = font_size
        self.point_update_amount = point_update_amount
        self.player_head = player_head_char
        self.set_up_window()
        self.set_up_players(self.player_head)
        self.set_up_player_points()
        self.set_up_player_tails()

    def set_up_window(self):
        pr.init_window(*self.window.get_pr_window_info())
        pr.set_target_fps(self.window.fps_cap)

    def set_up_players(self, player_head_char: str):
        self.players = PlayerHandler()
        self.player_char = String(player_head_char, self.font_size, pr.GREEN)
        self.p1 = self.players.add('p1', [1, self.player_char, self.window])
        self.p2 = self.players.add('p2', [2, self.player_char, self.window])
        
    
    def set_up_player_points(self):
        Player.set_point_update_amout(self.point_update_amount)

        self.player_1_points = PlayerPoints(self.p1, String("Player 1: ", self.font_size, pr.RED))
        self.player_2_points = PlayerPoints(self.p2, String("Player 2: ", self.font_size, pr.BLUE))

    def set_up_player_tails(self):
        self.tails = TailHandler()
        TailHandler.set_tail_timer(3, self.window.fps_cap)
        self.t1 = self.tails.add('t1', [self.p1, self.p2, String('#', self.font_size, pr.RED), self.window])
        self.t2 = self.tails.add('t2', [self.p2, self.p1, String('#', self.font_size, pr.BLUE), self.window])

    def play_game(self):
        while not pr.window_should_close():

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

            if self.p2_collided:
                self.p1.update_player_points()

            if self.p1_collided:
                self.p2.update_player_points()
    
    def close_window(self):
        pr.close_window()