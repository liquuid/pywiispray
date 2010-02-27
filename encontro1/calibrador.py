#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
import cwiid

#print 'Pressione 1 + 2 no wiimote'
#w = cwiid.Wiimote()
#w.rpt_mode = cwiid.RPT_IR 

pygame.init()                                                # Inicializa esses modulos

size = width, height = 1024, 600

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




clock = pygame.time.Clock()
lista = [] 
cursor = Cursor(150, 150)
lista.append(cursor)


while 1:                   
	clock.tick(60)					     # Loop principal do game 


	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	
	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      
	

	for i in lista:
		screen.blit(i.image,i.rect)

	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 

