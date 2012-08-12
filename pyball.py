#!/usr/bin/python
import sys
import pygame
from pygame.locals import *
from helpers import *
from ball import Ball

#setup pygame
pygame.init()

#setup the window
MAXWIDTH = 500
MAXHEIGHT = 500
screen = pygame.display.set_mode((MAXWIDTH, MAXHEIGHT), 0, 32)
pygame.display.set_caption('Py ball')
pygame.mouse.set_visible(0)

#setup the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Draw Everything
screen.blit(background, (0, 0))
pygame.display.flip()


#create a new Ball
def newBall(pos):
    ball = Ball(MAXWIDTH, MAXHEIGHT)
    ball.rect.center = pos
    ball.vector = randomVector(5)
    return ball

#create some balls
allsprites = pygame.sprite.LayeredDirty()
for n in range(0, 5):
    ball = newBall((MAXWIDTH / 2, MAXHEIGHT / 2))
    allsprites.add(ball)

#setup the sprites/clock
rects = allsprites.draw(screen)
pygame.display.update(rects)
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)

#run the game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #check if the ball is clicked on
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            ball = newBall(pos)
            allsprites.add(ball)

    allsprites.update()
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()
