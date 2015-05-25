'''
Created on 24/05/2015

@author: Isaac
'''
import random, pygame, sys
from pygame.locals import *
from Circulo import Circulo

NUMBER_BALLS = 10

class Test(object):
    '''
    classdocs
    '''
    RED   = (255,0,0)
    WHITE = (255, 255, 255)
    BLUE  = (0,0,220)

    def __init__(self, WINDOWWIDTH,WINDOWHEIGHT,FPS):
        '''
        Constructor
        '''
        self.WINDOWWIDTH = WINDOWWIDTH
        self.WINDOWHEIGHT = WINDOWHEIGHT
        self.FPS = FPS
        self.circulos = []

    def setup(self):
        self.circulos = [ 
        Circulo(self.WINDOWWIDTH, self.WINDOWHEIGHT, (random.randint(0,255) , random.randint(0,255) , random.randint(0,255) , 100),x=random.randint(0,400),y=random.randint(0,400), r=random.randint(10,50)) 
        for i in xrange(NUMBER_BALLS)]
        
    def nuevoCirculo(self):
        print 'Generando nuevo circulo'
        self.circulos.append( Circulo(
        self.WINDOWWIDTH, 
        self.WINDOWHEIGHT, 
        (random.randint(0,255) , random.randint(0,255) , random.randint(0,255) ,  100),
        x =random.randint(0,400),
        y =random.randint(0,400), 
        r =random.randint(10,50)
        )
        )
        
    def borrarCirculo(self):
        self.circulos.pop()

    def dibujarCirculos(self):        
        for ball in self.circulos:            
            ball.display(self.DISPLAYSURF)
        pygame.display.flip()

    
    def start(self):
        print "----INICIO----"
        # Inicializar ventana --------------------------------------------
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        self.DISPLAYSURF.fill(Test.WHITE)
        while True:
            for event in pygame.event.get(): # event handling loop
                if (event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    print 'Fin de ejecucion'
                    sys.exit()
                if (event.type == KEYUP and event.key == K_SPACE):
                    print 'Agregando circulo'
                    self.nuevoCirculo()
                if (event.type == KEYUP and event.key == K_BACKSPACE):
                    print 'Borrando anterior'
                    self.borrarCirculo()
                self.DISPLAYSURF.fill(Test.WHITE)
                self.dibujarCirculos()()        
                pygame.display.update()
                FPSCLOCK.tick(self.FPS)

prueba = Test(800,800,30)
prueba.start()
