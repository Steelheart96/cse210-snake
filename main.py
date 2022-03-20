from Structs import Window
from Director.Game import Game

WINDOW = Window(height = 450, width = 800, caption = "Snake", fps_cap = 60)
FONT_SIZE = 12
PLAYER_POINT_UPDATE_AMOUNT = 1
PLAYER_HEAD_CHAR = '@'

def main():
    game = Game(WINDOW, FONT_SIZE, PLAYER_POINT_UPDATE_AMOUNT, PLAYER_HEAD_CHAR)

    game.play_game()

    game.close_window()
    

if __name__ == "__main__":
    main()