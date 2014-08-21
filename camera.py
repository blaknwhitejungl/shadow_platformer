import pygame
import const

class Camera(object):
    i = 0
    def __init__(self, width, height):
        #self.pos = (0,0)            # world position of the camera frame
        #self.max = (width, height)  # size of the world
        #self.delta = (0,0)          # how much the camera has moved recently
        #self.i = 29

        self.rect = pygame.Rect(0,0,width,height)

    def apply(self, target):
        #x,y = self.delta
        target.rect = target.rect.move(self.rect.topleft)
    
    def update(self, target):
        #targX, targY = target.rect.center # Screen coords we want to center around
        #camL, camT = self.pos
        #shiftX = targX-(const.SCREEN_WIDTH/2)
        #shiftY = targY-(const.SCREEN_HEIGHT/2)
        #self.pos = (camL + shiftX, camT + shiftY)
        #self.delta = (shiftX, shiftY)


        l, t, _, _ = target.rect # l = left,  t = top
        _, _, w, h = self.rect      # w = width, h = height
        self.rect = pygame.Rect(-l+const.SCREEN_WIDTH/2, -t+const.SCREEN_HEIGHT/2, w, h)
        #print self.delta
        #self.i = self.i+1
        #if self.i >= 30:
        #    print "printing"
        #    print l
        #l = min(0,l)
        #l = max(-(self.rect.width-const.SCREEN_WIDTH), l)
        #t = max(-(self.rect.height-const.SCREEN_HEIGHT), t)
        #t = min(0,t)
        #if self.i >= 30:
        #    print l
        #    self.i = 0
