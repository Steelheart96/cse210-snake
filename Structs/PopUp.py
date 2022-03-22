class PopUp:
    '''
    struct

    Args:
    - width (int): The width of the popup
    - height (int): The height of the popup
    '''

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def copy(self):
        return PopUp(self.width, self.height)
    
    def __repr__(self) -> str:
        return f'PopUp({self.width}, {self.height})'
    
    def __str__(self) -> str:
        return f'({self.width}, {self.height})'