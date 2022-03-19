class Handler:
    '''
    Description: The base Handler Class.
    '''

    def __init__(self) -> None:
        self._input = {}

    def add(self, name: str, setup_info: list) -> object:
        '''
        Description: Adds set_up_info to hold and manage.
        
        Args:
        - name (str): The name of the object going into the Handler
        - setup_info (list): All of the setup information that the object going into the Handler needs for setup
        '''

        if name not in self._input:
            self._input[name] = []
            self._input[name] = setup_info
            self.load(name, setup_info)
        return self._input[name][0]
    
    def remove(self, name: str, setup_info: list) -> None:
        '''
        Description: Removed set_up_info from holder and manager.
        
        Args:
        - name (str): The name of the object going into the Handler
        - setup_info (list): All of the setup information that the object going into the Handler needs for setup
        '''

        if name in self._input:
            if setup_info in self._input[name]:
                self._input[name].remove(setup_info)
    
    def load(self, name: str, setup_info: list):
        '''
        Description: Default load function to place the object into Handler lists.

        Args:
        - name (str): The name of the object going into the Handler
        - setup_info (list): All of the setup information that the object going into the Handler needs for setup
        '''
        pass
    
    def draw(self):
        '''
        Description: Default draw function that draws on screen
        '''
        pass

    def update(self):
        '''
        Description: Default update function that updates the objects on screen.
        '''