from Actors import Actor
from Structs import Point, String, Window


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
		self.player_points = 0
		self.set_direction()
		self.set_position()
	
	def set_direction(self):
		self.direction = '-y'

	def set_position(self) -> None:
		'''
		Description: Sets the start position of players 1 and 2
		'''
		if self.player_num == 1:
			self.pos_x = self.window.width//3 - self.texture.width//2
			self.pos_y = self.window.height//2 - self.texture.height//2

			self.default_position = Point(self.pos_x, self.pos_y)

		elif self.player_num == 2:
			self.pos_x = (self.window.width//3 * 2) - self.texture.width//2
			self.pos_y = self.window.height//2 - self.texture.height//2

			self.default_position = Point(self.pos_x, self.pos_y)
	
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
	
	def reset(self):
		'''
		Description: Resets player's position to starting position.
		'''
		self.pos_x, self.pos_y = self.default_position.pos_x, self.default_position.pos_y
		self.set_direction()