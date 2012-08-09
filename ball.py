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


class Ball(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('ball.bmp')

    def update(self):
        self.dirty = 1
