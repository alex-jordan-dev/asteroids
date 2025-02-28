import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


print("Constants imported:", SCREEN_WIDTH, SCREEN_HEIGHT)
def main():

	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	fps = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	player.set_shots_group(shots)
	asteroid_field = AsteroidField()
	
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))


		updatable.update(dt)



		for sprite in asteroids:
			if sprite.collisions(player):
				print ("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if shot.collisions(asteroid):
					print ("hit!")
					asteroid.kill()
					shot.kill()



		for sprite in drawable:
			sprite.draw(screen)
   		
		   

		pygame.display.flip()
		dt = fps.tick(60) / 1000


	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")
	


if __name__ == "__main__":
	main()