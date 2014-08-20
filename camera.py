import pygame
import const

class Camera(object):
    i = 0
    def __init__(self, width, height):
        self.rect = pygame.Rect(0,0, width, height)
        self.i = 29

    def apply(self, target):
        target.rect = target.rect.move(self.rect.topleft)
    
    def update(self, target):
        l, t, _, _ = target.rect # l = left,  t = top
        _, _, w, h = self.rect      # w = width, h = height
        l, t, _ , _ = -l+(const.SCREEN_WIDTH/2), -t+(const.SCREEN_HEIGHT/2), w, h
        self.i = self.i+1
        if self.i >= 30:
            print "printing"
            print l
        l = max(0,l)
        l = (-(self.rect.width-const.SCREEN_WIDTH), l)
        t = max(-(self.rect.height-const.SCREEN_HEIGHT), t)
        t = min(0,t)
        if self.i >= 30:
            print l
            self.i = 0
        self.rect = pygame.Rect(l,t,w,h)
