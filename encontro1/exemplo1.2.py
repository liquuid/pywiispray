#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys, pygame, random                           # Importa os modulos do pygame
import cwiid

pygame.init()                                                # Inicializa esses modulos

print "Aperte os botoes 1 e 2 do controle"

wii = cwiid.Wiimote()
wii.rpt_mode = cwiid.RPT_IR 

size = width, height = 512, 448

color = 255 , 255, 255    # Define a cor de fundo da tela

screen = pygame.display.set_mode(size)      


#bola = pygame.image.load("bola.png")


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
bola2 = Bola(50,100)
bola3 = Bola(400, 200)
bola4 = Bola(100,300)
lista.append(bola)
lista.append(bola2)
lista.append(bola3)
lista.append(bola4)

for bolinha in xrange(5):
	lista.append(Bola( random.randrange(0,width), random.randrange(0 , height )))


som = pygame.mixer.Sound("jump.wav")
#mousepos = ""

wii_pos=[]

while 1:                   
	clock.tick(6000)					     # Loop principal do game 


	for event in pygame.event.get():                     # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	
	screen.fill(color)                                   # Preenche a tela com cor de fundo 
      
	

	for i in lista:
		"""
		i.rect.x = i.rect.x + 1
		i.rect.y = i.rect.y + 4
			
		if pressed_keys[pygame.K_LEFT]:
			i.rect.x -= 2
		if pressed_keys[pygame.K_RIGHT]:
			i.rect.x += 2

		if i.rect.x > width:
			i.rect.x = 0		
		if i.rect.y > height:
			i.rect.y = 0		
			print "tlim"
			som.play(0)
		"""	
		#mousepos = pygame.mouse.get_pos()		
		#print mousepos
		try:
			wii_pos = wii.state['ir_src'][0]['pos']
		except TypeError:
			pass	
		if wii_pos:	
			i.rect.x = wii_pos[0]
			i.rect.y = height-wii_pos[1]
	
		screen.blit(i.image,i.rect)

	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 

