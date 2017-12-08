import pygame, sys, random
from pygame.locals import *

#This code was created by Jack Hosier on December 7th, 2017 and finished on Dec. 8, 2017. 

#colors
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#constants representing the resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

#dictionary linking resources to textures
textures = {
				DIRT: pygame.image.load('Python Minecraft 2D/Dirtblock.png'),
				GRASS: pygame.image.load('Python Minecraft 2D/grass.png'),
				WATER: pygame.image.load('Python Minecraft 2D/water.png'),
				COAL: pygame.image.load('Python Minecraft 2D/coal.png')
			}

#game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

#a list of resources 
resources = [DIRT, GRASS, WATER, COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ] 

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#loop through the rows
for rw in range(MAPHEIGHT):

	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,15)
		
		if randomNumber == 0:
			tile = COAL
			
		elif randomNumber == 1 or randomNumber == 2:
			tile = WATER
		
		elif randomNumber >= 3 and randomNumber <= 7:
			tile = GRASS
		
		else:
			tile = DIRT
		tilemap[rw][cl] = tile

while True:
	#get all the events
	for event in pygame.event.get():
		print(event)
		#quitters
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		#key-pushers
		elif event.type == KEYDOWN:
			#right arrow
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1:
				playerPos[0] += 1
				
		#the player
		PLAYER = pygame.image.load('Python Minecraft 2D/player.png').convert_alpha()

		playerPos = [0,0]
		
		DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

	pygame.display.update()
