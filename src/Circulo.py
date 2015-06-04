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
    TRANSPARENT = (100,0,100)

    def __init__(self, width , height , color , x , y , r):
        '''
        Constructor
        '''
        self.windowWidth = width
        self.windowHeight = height
        self.color = color
        self.coorX = x
        self.coorY = y
        self.radio = r
        self.surf = pygame.Surface((self.radio*2,self.radio*2))
        self.surf.fill(Circulo.TRANSPARENT)

        
    def display(self, display):
        self.surf.set_colorkey(Circulo.TRANSPARENT)
        pygame.draw.circle(self.surf, self.color, (self.radio, self.radio), self.radio)
        self.surf.set_alpha(100)
        display.blit(self.surf, (self.coorX-self.radio, self.coorY-self.radio, 2*self.radio, 2*self.radio))
     
        
    def __str__(self):
        circle =  'R=',self.radio,' C=',self.color,' Coor= ',self.coorX,',',self.coorY 
        return str(circle)

    def getRadio(self):
        return self.radio
    
    def getCentro(self):
        return (self.coorX , self.coorY)
    
    