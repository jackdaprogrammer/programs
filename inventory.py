import pygame, sys, random
from pygame.locals import *

#This code was created by Jack Hosier on Dec. 11, 2017. 

#colors
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

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
inventory = {
				DIRT: 0,
				GRASS: 0,
				WATER: 0,
				COAL: 0
			}
			
#game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20


#the player
PLAYER = pygame.image.load('Python Minecraft 2D/player.png')

playerPos = [0,0]
#a list of resources 
resources = [DIRT, GRASS, WATER, COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ] 

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#inventory font
INVFONT = pygame.font.SysFont('E:/Python Minecraft 2D/FreeSansBold.ttf', 18)
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
			if event.key == K_RIGHT and playerPos[0] < MAPWIDTH -1:
				playerPos[0] += 1
			#left arrow
			if event.key == K_LEFT and playerPos[0] > 0:
				playerPos[0] -= 1
			#up arrow
			if event.key == K_UP and playerPos[1] > 0:
				playerPos[1] -= 1
			#down arrow
			if event.key == K_DOWN and playerPos[1] < MAPHEIGHT -1:
				playerPos[1] += 1
				
			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				
			if (event.key == K_1):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIRT] > 0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					inventory[currentTile] += 1
		
		
	
	#loop through each row
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
	#player positioning
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
	#display inventory
	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
	
	pygame.display.update()
