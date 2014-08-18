import pygame
import const

class Camera(object):
    i=39
    
    def __init__(self, width, height):
        self.rect = pygame.Rect(0,0, width, height)
        self.i = 39

    def apply(self, target):
        print self.rect.topleft
        target.rect = target.rect.move(self.rect.topleft)
    
    def update(self, target):
        l, t, _, _ = target.rect # l = left,  t = top
        _, _, w, h = self.rect      # w = width, h = height
        self.i=self.i+1
        if self.i == 40:
            print l
            print t
            print w
            print h
            self.i=0
        self.rect = pygame.Rect(-l+(const.SCREEN_WIDTH/2), -t+(const.SCREEN_HEIGHT/2), w, h)
        #self.rect = self.rect.clamp(target.rect)
