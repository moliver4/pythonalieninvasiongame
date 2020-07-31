import sys 

import pygame

class AlientInvasion:
	"""Overall class to manage game assests and behavior"""

	def ___init___(self):
		"""initialize the game, and create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")


	def run_game(self): 
		"""Start the main loop for the game."""
		while True: 
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Make the most recently drawn screen visible
			pygame.display.flip()


if ___name__ == '__main__':
	# Make a game instance, and run the game (if not running via own )
	ai = AlientInvasion()
	ai.run_game()