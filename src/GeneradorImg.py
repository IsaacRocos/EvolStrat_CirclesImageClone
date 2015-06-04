'''
Created on 24/05/2015

@author: Isaac
'''
import random, pygame, sys #, thread
from pygame.locals import *
from Circulo import Circulo
from math import sqrt
#import time

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
        self.ventanaAnalisis = []
        self.numeroCirculos = 0
        

    def verificaArgumentos(self):
        if len(sys.argv) <= 1:
            self.nombreImagen = "circulo.png"
        else:
            self.nombreImagen = sys.argv[1]
            print 'Abriendo <', self.nombreImagen , '> ...'
        print 'Imagen a imitar: ', self.nombreImagen



#     def blancoYNegro(self): # generar colores blanco-negro-gris
#         coloresBW = []
#         coloresBW.append(random.randint(0,100)) # para grises
#         coloresBW.append(random.randint(200,255)) # para blancos
#         col = coloresBW[random.randint(0,1)]
#         

    def nuevoCirculo(self):
        print 'Generando nuevo circulo'
        nuevoCirculo = Circulo(
        self.WINDOWWIDTH, 
        self.WINDOWHEIGHT, 
        (random.randint(0,255) , random.randint(0,255) , random.randint(0,255) ,  100), #para colores aleatorios
        x =random.randint(0,self.WINDOWWIDTH) ,
        y =random.randint(0,self.WINDOWHEIGHT) , 
        r =random.randint(1,50)
        )
        self.numeroCirculos += 1
        self.circulos.append(nuevoCirculo)
        print 'Circulo ' , self.numeroCirculos , nuevoCirculo
        

    
    def borrarCirculo(self):
        if(len(self.circulos)>0):
            self.circulos.pop()
            self.numeroCirculos -= 1

    
    def dibujarCirculos(self):        
        for ball in self.circulos:            
            ball.display(self.DISPLAYSURF)
        pygame.display.flip()

    
#     def definirVentana(self):
#         centro = self.circulos[self.numeroCirculos-1].getCentro()
#         x = centro[0]
#         y = centro[1]
#         radio = self.circulos[self.numeroCirculos-1].getRadio()
#         
#         inicioX = 0
#         finX    = self.WINDOWWIDTH-1
#         inicioY = 0
#         finY    = self.WINDOWHEIGHT-1
#     
#         if(x - radio > 0):
#             inicioX = x - radio
#         if(x + radio < self.WINDOWWIDTH):
#             finX= x + radio
#         if(y - radio > 0):
#             inicioY = y - radio 
#         if(y + radio < self.WINDOWHEIGHT):
#             finY = y + radio
#         
#         self.ventanaAnalisis = [inicioX,finX,inicioY,finY]
#         print 'Ventana: ', inicioX , ',' , inicioY , ';' ,finX, ',', inicioY , ';', inicioX , ',' , finY , ';' ,finX, ',', finY
#         
#     #Para comparar unicamente las regines que corresponden al nuevo circulo generado y evitar recorrer por completo ambas imagenes 
#     def evaluarAptitudVentana(self):
#         self.definirVentana()
#         print 'Analizando nueva imagen ...'
#         sumM = 0
#         for x in range (self.ventanaAnalisis[0] , (self.ventanaAnalisis[1]+1)): #leer pixeles hacia derecha
#             sumN = 0
#             for y in range (self.ventanaAnalisis[2] , (self.ventanaAnalisis[3]+1)): #leer pixeles hacia abajo
#                 print 'Analizando pixel ' , x , ',', y 
#                 pixelIMG = self.imagen.get_at((x,y))
#                 pixelSURF = self.DISPLAYSURF.get_at((x,y))
#                 nvopixel = self.restaPixel(pixelIMG, pixelSURF)
#                 sumN += nvopixel 
#             sumM += sumN
#         return sqrt(sumM)
    
    
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
        #while True:
        print 'Actualizando ventana...'
        self.DISPLAYSURF.fill(Generador.WHITE)
        self.dibujarCirculos()
        pygame.display.update()
        FPSCLOCK.tick(self.FPS)
        #time.sleep(tiempo)
    
    def start(self):
        print "Generando..."
        # Inicializar ventana -----------
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        self.DISPLAYSURF.fill(Generador.WHITE)
        numeroImagen = 0
        exitos = 0
        #thread.start_new_thread(self.actualizar, tuple([60]))
        while True:
            for event in pygame.event.get(): # event handling loop
                if (event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    print 'Salvando ultima imagen'
                    imgNombre= 'last_'+self.nombreImagen
                    pygame.image.save(self.DISPLAYSURF,imgNombre)
                    pygame.quit()
                    print 'Fin de ejecucion'
                    sys.exit()
            
            self.nuevoCirculo()
            self.actualizar()
            apt = self.evaluarAptitud()
            #apt = self.evaluarAptitudVentana()
            if(apt < self.aptitud):
                print '[OK] H-APT:',apt,'<','P_APT:',self.aptitud
                self.aptitud = apt
                exitos +=1
            else:
                print 'H-APT:',apt,' no supera a padre'
                print '[X]Desechando hijo'
                self.borrarCirculo()
                #self.actualizar()
            if(exitos == 200):
                imgNombre= 'N'+ str(numeroImagen) + '_' +self.nombreImagen
                print '<Guardando imagen: ' + imgNombre,'>'
                pygame.image.save(self.DISPLAYSURF,imgNombre)
                exitos = 0
                numeroImagen +=1
            
prueba = Generador(5)
prueba.start()


