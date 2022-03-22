from Structs import Window
from Director.Game import Game

WINDOW = Window(height = 550, width = 800, caption = "Snake", fps_cap = 60)
FONT_SIZE = 12
PLAYER_POINT_UPDATE_AMOUNT = 1
PLAYER_HEAD_CHAR = '@'
ROUND_RECAP_LENGTH = 4
END_RECAP_LENGTH = 5

def main():
    game = Game(WINDOW, FONT_SIZE, PLAYER_POINT_UPDATE_AMOUNT, PLAYER_HEAD_CHAR, ROUND_RECAP_LENGTH, END_RECAP_LENGTH)

    run = True
    while run:

        continue_game = game.play_game()
        
        if continue_game:
            continue_game = game.round_end()
        
        if continue_game and (game.p1.player_points >= 3 or game.p2.player_points >= 3):
            run = game.game_end()

        if not continue_game:
            run = False


    game.close_window()
    

if __name__ == "__main__":
    main()