from pyray import check_collision_recs

'''
NOTE This is class and file are likely to be removed!
'''

class Collision:
    '''
    Description: A Class that holds all the base collision methods.
    '''

    def player_collide_check(tail, player) -> bool:
        '''
        Description: Checks for collision between player and tail.
        
        Args:
        - player (Player): A Player's tail
        - tail (Tail): The opposing Player's tail
        '''
        return check_collision_recs(
                [tail.pos_x, tail.pos_y, tail.texture.width, tail.texture.height],
                [player.pos_x, player.pos_y, player.texture.width, player.texture.height]
            )

    def tail_collide_check(tail1, tail2) -> bool:
        '''
        Description: Checks for collision between tail piece and possible tail piece.

        Args:
        - tail1: tail already created
        - tail2: possible tail
        '''
        if tail2 != None:
            return check_collision_recs(
                    [tail1.pos_x, tail1.pos_y, tail1.texture.width, tail1.texture.height],
                    [tail2.pos_x, tail2.pos_y, tail2.texture.width, tail2.texture.height]
                )
        return False