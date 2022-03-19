from Actors.Actor import Actor
from Structs.Window import Window
from Structs.Texture import String


class Player(Actor):
	'''
	Description: A Class for instancing players.

	Args:
	- player_num (int): The player number
	- display_char (String): String information to create a texture
	- window (Window): All window information
	'''
	
	Point_update_amount = 0

	def __init__(self, player_num: int, display_char: String, window: Window) -> None:
		super().__init__(display_char, window)
		self.player_num = player_num
		self.direction = '-y' # This is the player start direction
		self.player_points = 0
		self.set_position()

	def set_position(self) -> None:
		'''
		Description: Sets the start position of players 1 and 2
		'''
		if self.player_num == 1:
			self.pos_x = self.window.width//3 - self.texture.width
			self.pos_y = self.window.height//2 - self.texture.height

		elif self.player_num == 2:
			self.pos_x = (self.window.width//3 * 2) - self.texture.width
			self.pos_y = self.window.height//2 - self.texture.height
	
	def set_point_update_amout(point_amount):
		'''
		Description: Sets amount of points player gets for winning a round.
		'''
		Player.Point_update_amount = point_amount

	def update_player_points(self):
		'''
		Description: Updates a player's points.
		'''
		self.player_points += Player.Point_update_amount