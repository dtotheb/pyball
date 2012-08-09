#!/usr/bin/python
import sys, os
import random
import pygame
from pygame.locals import *
from ball import Ball

#setup pygame
pygame.init()

#setup the window
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Py ball')
pygame.mouse.set_visible(0)

#setup the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Draw Everything
screen.blit(background, (0, 0))
pygame.display.flip()

screenwidth = screen.get_width()
screenheight = screen.get_height()

#setup the Ball
ball = Ball()
ball.rect.center = (250, 250)
ball.vector = (-1, -1)

#setup the sprites/clock
allsprites = pygame.sprite.LayeredDirty((ball))
rects = allsprites.draw(screen)
pygame.display.update(rects)
clock = pygame.time.Clock()

#run the game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    allsprites.update()
    ball.check_bounce(screenwidth, screenheight)
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()
