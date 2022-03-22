class Point:
    '''
    struct

    Args:
    - pos_x (int): X position
    - pos_y (int): Y position
    '''

    def __init__(self, pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

    def copy(self):
        return Point(self.pos_x, self.pos_y)

    def __repr__(self) -> str:
        return f'Point({self.pos_x}, {self.pos_y})'
    
    def __str__(self) -> str:
        return f'({self.pos_x}, {self.pos_y})'