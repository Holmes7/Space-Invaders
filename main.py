import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((600, 600))

background = pygame.image.load('background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)



playerimg = pygame.image.load('spaceship.png')
playerX = 285
playerY = 500
playerXchange = 0
playerYchange = 5

alienimg = []
alienX = []
alienY = []
alienXchange = []
alienYchange = []
num_of_enemies = 6

for i in range(num_of_enemies):

	alienimg.append(pygame.image.load('alien.png'))
	alienX.append(random.randint(3, 533))
	alienY.append(random.randint(100, 200))
	alienXchange.append(3)
	alienYchange.append(10)

bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletXchange = 0
bulletYchange = -15
bulletState = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gfont = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
textY = 10

def show_score(x, y):
	sc = font.render("Score: " + str(score), True, (255, 255, 255))
	screen.blit(sc, (x, y))

def game_over():
	go = gfont.render("GAME OVER", True, (255,0 ,0))
	screen.blit(go, (100, 250))

def player(x, y):
	screen.blit(playerimg, (x, y))

def alien(x, y, i):
	screen.blit(alienimg[i], (x, y))

def fire_bullet(x, y):
	global bulletState
	bulletState = "fire"
	screen.blit(bulletimg, (x+16, y+10))

def isCollison(x1, y1, x2, y2):
	distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
	if distance < 27:
		return True

	return False

running = True
while running:
	screen.fill((0, 0, 0))

	screen.blit(background, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    running = False  
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerXchange = -5
			if event.key == pygame.K_RIGHT:
				playerXchange = 5
			if event.key == pygame.K_SPACE:
				bulletX = playerX
				fire_bullet(bulletX, bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				playerXchange = 0

	playerX += playerXchange
	if playerX<0 or playerX>536:
		playerX -= playerXchange

	for i in range(num_of_enemies):

		alienX[i] += alienXchange[i]
		if alienX[i]<0 or alienX[i]>536:
			alienX[i] -= alienXchange[i]
			alienXchange[i] *= -1
			alienY[i] += alienYchange[i]

		collision = isCollison(alienX[i], alienY[i], bulletX, bulletY)

		if collision == True:
			bulletY = 500
			bulletState = "ready"
			score +=1
			alienX[i] = random.randint(3, 533)
			alienY[i] = random.randint(100, 200)

		alien(alienX[i], alienY[i], i)

		if alienY[i] > 200:
			game_over()
			break

	if bulletState == "fire":
		fire_bullet(bulletX, bulletY)
		bulletY = bulletY + bulletYchange

	if bulletY < 0:
		bulletY = 500
		bulletState = "ready"



	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()
