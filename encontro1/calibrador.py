#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
import cwiid

print 'Pressione 1 + 2 no wiimote'
w = cwiid.Wiimote()
w.rpt_mode = cwiid.RPT_IR 

pygame.init()                                                # Inicializa esses modulos

size = width, height = 1024, 768

color = 255, 255, 255                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 


cursor = pygame.image.load("arrow.png")


class Cursor(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("arrow.png")
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

class Target(pygame.sprite.Sprite):

        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("x.png")
                self.rect  = self.image.get_rect()
                self.rect.centerx = x
                self.rect.centery = y
                self.estado = False

def eme(a,b):
	print b[1],a[1],b[0],a[0]
	return ( b[1]-a[1] ) / float((b[0] - a[0])) 
	

clock = pygame.time.Clock()
lista = [] 
#cursor = Cursor(150, 150)

target1 = Target(20,20)
target2 = Target(width-20,20)
target3 = Target(20,height-20)
target4 = Target(width-20,height-20)

lista.append(target1)
lista.append(target2)
lista.append(target3)
lista.append(target4)

#lista.append(cursor)

count=0
coords=[]

while 1:                   
	clock.tick(60)	     # Loop principal do game 
	
	for event in pygame.event.get():            # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	pos_wii=[]
        try:
                pos_wii = w.state['ir_src'][0]['pos']
		if count == 4:
			print 'gotcha !  '+str(pos_wii)
			coords.append(pos_wii)
			if len(coords) == 2 :
				print eme(coords[0] , coords[1])
				coords=[]
			
		count = count + 1
		#print pos_wii
        except TypeError:
 #              print 'sem fonte'
		count = 0 

 #       print pos_wii
	

	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      
	

	for i in lista:
		screen.blit(i.image,i.rect)

	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 

