import pyray as pr
from Handlers.TailHandler import TailHandler
from Structs.Window import Window
from Structs.Texture import String
from Handlers.PlayerHandler import PlayerHandler, Player

WINDOW = Window(height = 450, width = 800, caption = "Greed", fps_cap = 60)

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

        pr.end_drawing()

        if p1_collide or p2_collide:
            pass

    pr.close_window()

if __name__ == "__main__":
    main()