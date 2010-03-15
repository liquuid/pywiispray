#!/usr/bin/env python
# -*- coding : utf8 -*-
import sys
import pygame
import random
import os
import cwiid

dpath = os.getcwd()+"/data/"

os.system('zenity --info --text "Pressione 1 + 2 no wiimote e clique em OK"')

w = cwiid.Wiimote()
w.rpt_mode = cwiid.RPT_IR 

pygame.init()                                                # Inicializa esses modulos

size = width, height = 640, 480

color = 255, 255, 255                                        # Define a cor de fundo da tela
screen = pygame.display.set_mode(size)                       # Inicializa a janela onde rola o game 

ts = pygame.mixer.Sound(dpath+"ts.wav")
class Cursor(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(dpath+"branco/br_large.png"),[32,32])

		self.image_orig = self.image
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

class Target(pygame.sprite.Sprite):

        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(dpath+"x.png")
                self.rect  = self.image.get_rect()
                self.rect.centerx = x
                self.rect.centery = y
                self.estado = False

clock = pygame.time.Clock()
lista = [] 
cursor = Cursor(0, 0)

target1 = Target(20,20)
target2 = Target(width-20,20)
target3 = Target(20,height-20)
target4 = Target(width-20,height-20)

lista.append(target1)

pcount=0
tcount=0
coords=[]
screen.fill(color)     
wall = pygame.image.load(dpath+"wall_1.jpg")

while 1:                   
	clock.tick(6000)	     # Loop principal do game 
	
	for event in pygame.event.get():            # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()
	if pressed_keys[pygame.K_f]:
		pygame.display.toggle_fullscreen()
	if pressed_keys[pygame.K_SPACE]:
		screen.blit(wall,[0,0])

	 

	pos_wii=[]
        try:
                pos_wii = w.state['ir_src'][0]['pos']
	#	if pygame.mouse.get_pressed()[0]:
	#		pos_wii= pygame.mouse.get_pos()
	#		cursor.image = pygame.transform.rotate(cursor.image_orig,random.randrange(0,89))
		if pcount == 20:
			#print 'gotcha !  '+str(pos_wii)
			coords.append(pos_wii)
			tcount = tcount + 1
		if tcount == 1:
			target1.image = pygame.image.load(dpath+"ok.png")
			lista.append(target4)
			
		if tcount == 2:
			target4.image = pygame.image.load(dpath+"ok.png")
			Cx = ( coords[1][0] - coords[0][0])/float(width)
			Cy = ( coords[0][1] - coords[1][1])/float(height)
			
			lista=[]
			screen.blit(wall,[0,0])
		
		pcount = pcount + 1
		
		
			
        except TypeError:
		pcount = 0 
	except ZeroDivisionError:
		print "ooops x/0"
	
	for i in lista:
		screen.blit(i.image,i.rect)
	if pos_wii and cursor.__class__.__name__ == "Cursor":
		try:
			cursor.rect.centerx = (pos_wii[0] - coords[0][0])/Cx
			#print pos_wii[0] - coords[0][0] , 768-pos_wii[1] 
			cursor.rect.centery = (768-pos_wii[1])/Cy
			ts.play(0) 
		#	cursor.rect.centerx = pos_wii[0]
		#	cursor.rect.centery = pos_wii[1]
			
			if cursor.rect.centerx > width :
				cursor.image = pygame.transform.scale(pygame.image.load(dpath+"branco/br_littleFat.png"),[32,32])
			if cursor.rect.centerx < 0  :
				cursor.image = pygame.transform.scale(pygame.image.load(dpath+"preto/br_littleFat.png"),[32,32])
			if cursor.rect.centery > height :
				screen.blit(wall,[0,0])
		except:
			pass
		screen.blit(cursor.image,cursor.rect)

	
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 

