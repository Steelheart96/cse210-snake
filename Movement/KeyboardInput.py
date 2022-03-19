import pyray as pr

class KeyInput:
    '''Temporary movement class'''

    Player_Speed = 1

    def update_direction(player):
        if player.player_num == 2:
            if pr.is_key_down(pr.KEY_LEFT):
                player.direction = '-x'
            if pr.is_key_down(pr.KEY_RIGHT):
                player.direction = 'x'
            if pr.is_key_down(pr.KEY_UP):
                player.direction = '-y'
            if pr.is_key_down(pr.KEY_DOWN):
                player.direction = 'y'
            
        if player.player_num == 1:
            if pr.is_key_down(pr.KEY_A):
                player.direction = '-x'
            if pr.is_key_down(pr.KEY_D):
                player.direction = 'x'
            if pr.is_key_down(pr.KEY_W):
                player.direction = '-y'
            if pr.is_key_down(pr.KEY_S):
                player.direction = 'y'
    
    def update_player_position(player):
        x = 0
        y = 0
        
        if player.direction == '-x':
            x = -KeyInput.Player_Speed
        if player.direction == 'x':
            x = KeyInput.Player_Speed

        if player.direction == '-y':
            y = -KeyInput.Player_Speed
        if player.direction == 'y':
            y = KeyInput.Player_Speed
        
        if 0 < player.pos_x + x < player.window.width - player.texture.width:
            player.pos_x += x
        if 0 < player.pos_y + y < player.window.height - player.texture.height:
            player.pos_y += y

    def set_player_speed(speed: int):
        KeyInput.Player_Speed = speed