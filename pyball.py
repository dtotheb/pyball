#!/usr/bin/python
import sys, os
import random
import pygame
from pygame.locals import *


#setup pygame
pygame.init()

#setup the window
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Py ball')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Draw Everything
screen.blit(background, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
