#!/usr/bin/python
import sys, os
import random
import pygame
from pygame.locals import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,  0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


#generate a random vector within n
def randomVector(n):
    x = random.randint(-1 * n, n)
    y = random.randint(-1 * n, n)
    return (x, y)


class Ball(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('ball.bmp')
        self.vector = (0, 0)

    def update(self):
        self.dirty = 1
        self.rect.move_ip(self.vector)

    #checks if the ball bounces off the screen edge
    def check_bounce(self, maxwidth, maxheight):
        hx = self.rect.width / 2
        hy = self.rect.height / 2
        x = self.rect.centerx
        y = self.rect.centery

        #check for bounds
        if x + hx >= maxwidth or x - hx <= 0:
            self.vector = (self.vector[0] * -1, self.vector[1])
        if y + hy >= maxheight or y - hy <= 0:
            self.vector = (self.vector[0], self.vector[1] * -1)

    #handle ball clicks
    def clicked(self):
        self.vector = randomVector(2)
