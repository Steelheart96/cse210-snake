from Handlers.Handler import Handler
from Actors.Tail import Tail

class TailHandler(Handler):
    '''
    Description: Handles all player actions
    '''

    def set_tail_timer(time: int, window_fps: int):
        '''
        Description: Sets timer for player tail.
        
        Args:
        - time (int): Amount of time (seconds) a Segment is on screen
        - window_fps (int): Program window fps
        '''
        Tail.Timer = time * window_fps

    def load(self, name: str, setup_info: list):
        '''
        Description: Creates an instance of a Tlayer

        Args:
        - name: The name of an object already in the Handler
        - setup_info: attached_player (Player), opponent_player (Player), texture (Texture), window (Window)
        '''
        tail = Tail(*setup_info)
        self._input[name].insert(0, tail)
    
    def draw(self):
        for tail_info in self._input.values():
            tail_info[0].draw_tail()

    def update(self):
        for tail_info in self._input.values():
            tail_info[0].update_tail()