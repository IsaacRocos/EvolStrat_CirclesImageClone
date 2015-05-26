'''
Created on 24/05/2015

@author: Isaac
'''
import random, pygame, sys
from pygame.locals import *
from Circulo import Circulo
from math import sqrt

NUMBER_BALLS = 10

class Generador(object):
    '''
    classdocs
    '''
    RED   = (255,0,0)
    WHITE = (255, 255, 255,255)
    BLUE  = (0,0,220)

    def __init__(self,FPS):
        self.nombreImagen = ""
        self.verificaArgumentos()
#         self.WINDOWWIDTH = WINDOWWIDTH
#         self.WINDOWHEIGHT = WINDOWHEIGHT
        self.imagen  = pygame.image.load(self.nombreImagen)
        self.WINDOWWIDTH = self.imagen.get_size()[0]
        self.WINDOWHEIGHT = self.imagen.get_size()[1]
        self.aptitud = 100000
        self.FPS = FPS
        self.circulos = []
        

    def verificaArgumentos(self):
        if len(sys.argv) <= 1:
            self.nombreImagen = "circulo.png"
        else:
            self.nombreImagen = sys.argv[1]
            print 'Abriendo <', self.nombreImagen , '> ...'
        print 'Imagen a imitar: ', self.nombreImagen


    def nuevoCirculo(self):
        print 'Generando nuevo circulo'
        col = random.randint(0,100) # para grises
        nuevoCirculo = Circulo(
        self.WINDOWWIDTH, 
        self.WINDOWHEIGHT, 
        #(random.randint(0,255) , random.randint(0,255) , random.randint(0,255) ,  100), #para colores aleatorios
        (col, col , col ,  100),
        x =random.randint(0,self.WINDOWWIDTH),
        y =random.randint(0,self.WINDOWHEIGHT), 
        r =random.randint(5,90)
        )
        self.circulos.append(nuevoCirculo)
        print nuevoCirculo
        
    
    def borrarCirculo(self):
        if(len(self.circulos)>0):
            self.circulos.pop()

    
    def dibujarCirculos(self):        
        for ball in self.circulos:            
            ball.display(self.DISPLAYSURF)
        pygame.display.flip()

    
    def evaluarAptitud(self):
        print 'Analizando nueva imagen ...'
        sumM = 0
        for x in range (self.WINDOWWIDTH): #leer pixeles hacia derecha
            sumN = 0
            for y in range (self.WINDOWHEIGHT): #leer pixeles hacia abajo 
                pixelIMG = self.imagen.get_at((x,y))
                pixelSURF = self.DISPLAYSURF.get_at((x,y))
                nvopixel = self.restaPixel(pixelIMG, pixelSURF)
                sumN += nvopixel 
            sumM += sumN
        return sqrt(sumM)
            
    
    def restaPixel(self,pixelIMG,pixelSURF):
        npr = pixelIMG.r - pixelSURF.r
        npg = pixelIMG.g - pixelSURF.g 
        npb = pixelIMG.b - pixelSURF.b
        npa = pixelIMG.a - pixelSURF.a
        return (npr**2 + npg**2 + npb**2  + npa**2 + 0.0) / 4.0

    def actualizar(self):
        self.DISPLAYSURF.fill(Generador.WHITE)
        self.dibujarCirculos()
        pygame.display.update()
        FPSCLOCK.tick(self.FPS)
    
    
    def start(self):
        print "Generando..."
        # Inicializar ventana -----------
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        self.DISPLAYSURF.fill(Generador.WHITE)
        evaluar = 0
        while True:
            for event in pygame.event.get(): # event handling loop
                if (event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    print 'Fin de ejecucion'
                    sys.exit()
#                 if event.type == MOUSEBUTTONUP:
#                     self.mousex, self.mousey = event.pos
#                     print "Click en: ",self.mousex,self.mousey,' RGBA:',self.DISPLAYSURF.get_at((self.mousex,self.mousey))
#                 if (event.type == KEYUP and event.key == K_SPACE):
#                     print 'Agregando circulo'
#                     self.nuevoCirculo()
#                     evaluar = 1
#                 if (event.type == KEYUP and event.key == K_BACKSPACE):
#                     print 'Borrando anterior'
#                     self.borrarCirculo()
                self.nuevoCirculo()
                self.actualizar()
                apt = self.evaluarAptitud()
                if(apt < self.aptitud):
                    print 'H-APT:',apt,'<','P_APT:',self.aptitud
                    self.aptitud = apt
                else:
                    print 'H-APT:',apt,' no supera a padre'
                    print 'Desechando hijo'
                    self.borrarCirculo()
                    self.actualizar()
                        
prueba = Generador(10)
prueba.start()


