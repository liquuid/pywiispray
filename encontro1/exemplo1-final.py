#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                                   # Importa os modulos do pygame
import cwiid
print 'Pressione 1 + 2 no wiimote'
w = cwiid.Wiimote()
w.rpt_mode = cwiid.RPT_IR

pygame.init()                                                # Inicializa esses modulos

size = width, height = 1024, 600
grav = 0.01
color = 255, 255, 255                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 



class Bola(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bola.png")
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.cor = "azul"
		self.acey = 1 
		
class BolaV(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("bolar.png")
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.cor = "vermelho"



clock = pygame.time.Clock()
lista = [] 
bola = Bola(150, 150)
bola2 = Bola(400,50)
lista.append(bola)
lista.append(bola2)
lista.append(Bola(60,300)) 
lista.append(BolaV(120,120))

queda = 1.0

while 1:                   
	clock.tick(60)					     # Loop principal do game 


	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()
	pos_wii=[]	
	try:
		pos_wii = w.state['ir_src'][0]['pos']
	except TypeError:
		print 'sem fonte'
				
	print pos_wii
	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      
	

	for i in lista:
		if i.cor == "vermelho":
			if pressed_keys[pygame.K_RIGHT]:
				i.rect.centerx = i.rect.centerx + 5
			if pressed_keys[pygame.K_LEFT]:
				i.rect.centerx = i.rect.centerx - 5
			if pressed_keys[pygame.K_UP]:
				i.rect.centery = i.rect.centery - 5
			if pressed_keys[pygame.K_DOWN]:
				i.rect.centery = i.rect.centery + 5
			
			if pos_wii:
				i.rect.centerx = pos_wii[0]
				i.rect.centery = 600-pos_wii[1]

		if i.cor == "azul":
					i.rect.centery = i.rect.centery + i.acey
					if i.rect.centery < 400:
						i.acey = i.acey + grav
					else:
						i.acey = i.acey*-1
		
			 
		screen.blit(i.image,i.rect)

	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 













