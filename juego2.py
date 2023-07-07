import pygame, sys 
from pygame.locals import*
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))

pygame.display.set_caption('videojuego de derek')


while True: # mine game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0 ,255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_x = 400
cord_y = 200

speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    if(cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if(cord_y > 320 or cord_y < 0):
        speed_x *= -1

    cord_x += speed_x
    cord_y += speed_y

screen.fill(WHILE) 

pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80)) 

pygame.display.flip()

clock.tick(60)
