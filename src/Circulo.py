'''
Created on 24/05/2015

@author: Isaac
'''

import pygame
from pygame.locals import *

class Circulo(object):
    '''
    classdocs
    '''
    
    BACKGROUND_COLOR = (255, 255, 255)
    DEFAULT_COLOR = (0, 0, 0)
    DEFAULT_SIZE = 30
    TRANSPARENT = (255,0,255)

#pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect

    def __init__(self, width , height , color , x , y , r):
        '''
        Constructor
        '''
        self.windowWidth = width
        self.windowHeight = height
        self.radio = r
        self.color = color
        self.red   = 0
        self.green = 0
        self.blue  = 0
        self.coorX = x
        self.coorY = y
        self.surf = pygame.Surface((width,height))
        self.surf.fill(Circulo.TRANSPARENT)


        
    def display(self, display):
        self.surf.set_colorkey(Circulo.TRANSPARENT)
        pygame.draw.circle(self.surf, self.color, (self.coorX, self.coorY), self.radio)
        self.surf.set_alpha(100)
        #display.blit(self.surf, (self.location.x-self.r, self.location.y-self.r, 2*self.r, 2*self.r))
        display.blit(self.surf, (self.coorX,self.coorY))
        #self.checkEdges2()
        




    def checkEdges(self):
        if self.coorX >= self.windowWidth or self.coorX <= 0:
            self.velocity.x = self.velocity.x * -1

        if self.coorY>= self.windowHeight or self.coorY<= 0:
            self.velocity.y = self.velocity.y * -1
