#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
pygame.init()                                                # Inicializa esses modulos

size = width, height = 512, 448

color = 255, 255, 255                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 


bola = pygame.image.load("bola.png")


class Bola(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bola.png")
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y




clock = pygame.time.Clock()
lista = [] 
bola = Bola(150, 150)
lista.append(bola)


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

