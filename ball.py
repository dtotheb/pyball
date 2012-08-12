#!/usr/bin/python
from helpers import *
import pygame
from pygame.locals import *

#A Ball
class Ball(pygame.sprite.DirtySprite):
    def __init__(self, maxwidth, maxheight):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = load_image('blue_ball.bmp')
        self.vector = (0, 0)
        self.bounce_sound = load_sound('whiff.wav')
        self.maxwidth = maxwidth
        self.maxheight = maxheight

    def update(self):
        self.dirty = 1
        self.rect.move_ip(self.vector)
        self.check_bounce()

    #checks if the ball bounces off the screen edge
    def check_bounce(self):
        hx = self.rect.width / 2
        hy = self.rect.height / 2
        x = self.rect.centerx
        y = self.rect.centery

        #check for bounds
        if x + hx >= self.maxwidth or x - hx <= 0:
            self.vector = (self.vector[0] * -1, self.vector[1])
            #self.bounce_sound.play()
        if y + hy >= self.maxheight or y - hy <= 0:
            self.vector = (self.vector[0], self.vector[1] * -1)
            #self.bounce_sound.play()

    #handle ball clicks
    def clicked(self):
        self.vector = randomVector(2)
        #self.bounce_sound.play()
