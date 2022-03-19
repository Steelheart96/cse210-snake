import pyray as pr
from Handlers.TailHandler import TailHandler
from Structs import Point, Window, String, PositionedString
from Handlers.PlayerHandler import PlayerHandler, Player
from Overlays.PlayerPoints import PlayerPoints

WINDOW = Window(height = 450, width = 800, caption = "Snake", fps_cap = 60)

FONT_SIZE = 12

def main():

    pr.init_window(*WINDOW.get_pr_window_info())
    pr.set_target_fps(WINDOW.fps_cap)

    # player setup
    players = PlayerHandler()
    player_char = String('@', FONT_SIZE, pr.GREEN)
    p1 = players.add('p1', [1, player_char, WINDOW])
    p2 = players.add('p2', [2, player_char, WINDOW])
    Player.set_point_update_amout(1)

    player_1_points = PlayerPoints(p1, PositionedString("Player 1", FONT_SIZE, pr.BLUE, Point(100, 300)))
    player_2_points = PlayerPoints(p2, PositionedString("Player 2", FONT_SIZE, pr.BLUE, Point(200, 300)))

    # tail setup
    tails = TailHandler()
    TailHandler.set_tail_timer(3, WINDOW.fps_cap)
    t1 = tails.add('t1', [p1, p2, String('#', FONT_SIZE, pr.BLUE), WINDOW])
    t2 = tails.add('t2', [p2, p1, String('#', FONT_SIZE, pr.RED), WINDOW])


    while not pr.window_should_close():

        # collision detection (True = Hit, False = No Hit)
        p1_collide = t1.player_collision()
        p2_collide = t2.player_collision()

        # movement updates
        players.update()
        tails.update()

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # draw onscreen
        tails.draw()
        players.draw()

        player_2_points.draw_points()
        player_1_points.draw_points()

        pr.end_drawing()

        if p1_collide:
            p1.update_player_points()

        if p2_collide:
            p2.update_player_points()

    pr.close_window()

if __name__ == "__main__":
    main()