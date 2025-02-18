import pygame
import sys
from constants import *
from asteroidfield import *
from shot import *
from player import Player

def main():
	
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
	
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)	
	asteroid_field = AsteroidField()



# Game Loop #
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, (0,0,0))
		updatable.update(dt)
		for object in asteroids:
			if object.collide(player) == False:
				sys.exit("Game over!")
		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		t = clock.tick(60)
		dt = t/1000

	

if __name__ == "__main__":
    main()
