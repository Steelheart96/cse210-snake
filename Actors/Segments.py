from pyray import Texture


class Segment:
    '''
    Description: Class for the Segments in Each Player's Tail
    
    Args:
    - pos_x (int): Segment instance x position
    - pos_y (int): Segment instance y position
    - texture (Texture): Segment instance texture
    - screen_time (int): Segment instance time on screen 
    '''

    def __init__(self, pos_x: int, pos_y: int, texture: Texture, screen_time: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen_time = screen_time
        self.texture = texture

    def update_timer(self) -> None:
        '''
        Description: Updates segment "on screen time" timer
        '''
        self.screen_time -= 1