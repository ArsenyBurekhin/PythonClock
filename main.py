import pygame, sys

import time
from pygame.locals import QUIT
from Clock import Clock
from ClockBuilder import ClockBuilder

pygame.init()
pygame.display.set_caption('Super Clock!')

DISPLAYSURF = pygame.display.set_mode((500, 500))

clock = ClockBuilder.buildBlueSquereFaceWithNumbersAndRedArrows(120,DISPLAYSURF)
clock.draw()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill((0,0,30))		
	clock.draw()
	pygame.display.flip()
	time.sleep(1)