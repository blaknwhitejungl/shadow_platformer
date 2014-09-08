import pygame
import const

class Camera(object):
    i = 0
    def __init__(self, width, height):
        self.pos = (0,0)            # world position of the camera frame
        self.max = (width, height)  # size of the world
        self.delta = (0,0)          # how much the camera has moved recently
        self.i = 29

        #self.rect = pygame.Rect(0,0,width,height)

    def apply(self, target):
        x,y = self.delta
        target.rect = target.rect.move(-x, -y)
    
    def update(self, target):
        targX, targY = target.rect.center # Screen coords we want to center around
        camX, camY = self.pos
        worldWidth, worldHeight = self.max
        
        shiftX = targX-(const.SCREEN_WIDTH/2)
        
        if(shiftX > const.SCROLL_RIGHT):
            # Don't snap the player to center
            shiftX = shiftX - const.SCROLL_RIGHT
            
            # Stop at the right edge of the world
            shiftX = min(shiftX, worldWidth-(camX + const.SCREEN_WIDTH))
            
        elif (shiftX < const.SCROLL_LEFT):
            # Don't snap the player to center
            shiftX = shiftX - const.SCROLL_LEFT
            
            # Stop at the left edge of the world
            shiftX = max(shiftX, -camX)
            
        else:
            shiftX = 0
            
        shiftY = targY-(const.SCREEN_HEIGHT/2)

        if(shiftY > const.SCROLL_BOTTOM):
            # Don't snap the player to center
            shiftY = shiftY - const.SCROLL_BOTTOM
            
            # Stop at the bottom edge of the world
            shiftY = min(shiftY, worldHeight-(camY + const.SCREEN_HEIGHT))
            
        elif (shiftY < const.SCROLL_TOP):
            # Don't snap the player to center
            shiftY = shiftY - const.SCROLL_TOP
            
            # Stop at the left edge of the world
            shiftY = max(shiftY, -camY)
            
        else:
            shiftY = 0
        
        self.pos = (camX + shiftX, camY + shiftY)
        self.delta = (shiftX, shiftY)
