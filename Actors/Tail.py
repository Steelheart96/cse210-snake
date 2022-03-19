from Actors import Player, Actor, Collision, Segment, Load
from Structs import String, Window

class Tail(Actor):
    '''
    Class for Tail Segments of Player
    
    Class Variable:
    - Timer (int): The amount of time a tail piece stays on screen (in seconds)
    
    Args:
    - attached_player (Player): The player the tail is going to be generated from
    - opponent_player (Player): The player that the tail is going to be checking for collisions
    - display_char (String): String information to create a texture
    - window (Window): All window information
    '''

    Timer = 0

    def __init__(self, attached_player: Player, opponent_player: Player, display_char: String, window: Window) -> None:
        super().__init__(display_char, window)
        self._attached_player = attached_player
        self._opponent = opponent_player
        self.set_up()
    
    def set_up(self) -> None:
        '''
        Description: Prepares the Tail instance to hold Segment instances.
        '''
        self._segments = []
        self._segments.append(self._attached_player)

    def update_tail(self) -> None:
        '''
        Description: Main update function that runs through runtime Tail insatnce operations
        '''
        self.tail_collision()
        self.update_tail_timer()
    
    def tail_collision(self) -> None:
        '''
        Description: Checks for collision between last placed tail and possible new tail
        '''
        pos_x = self._attached_player.pos_x
        pos_y = self._attached_player.pos_y

        new_segment = Tail.create_new_tail(pos_x, pos_y, self.texture)

        if self._segments.index(self._segments[-1]) != 0:
            if not Collision.tail_collide_check(self._segments[-1], new_segment):
                self._segments.append(new_segment)
        else:
            self._segments.append(new_segment)

    def player_collision(self) -> bool:
        '''
        Description: Checks for collision of opponent and attached player tail
        '''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                if Collision.player_collide_check( segment, self._opponent):
                    return True
        return False
    
    def create_new_tail(pos_x, pos_y, texture) -> Segment:
        '''
        Description: Creates a new tail segment
        '''
        return Segment(pos_x, pos_y, texture, Tail.Timer)
    
    def update_tail_timer(self) -> None:
        '''
        Description: Updates segments onscreen timer
        '''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                segment.update_timer()
                if segment.screen_time == 0:
                    self._segments.remove(segment)

    def draw_tail(self) -> None:
        '''
        Description: Draws Tail segments
        '''
        for segment in self._segments:
            if self._segments.index(segment) != 0:
                Load.draw_rectangle(segment)