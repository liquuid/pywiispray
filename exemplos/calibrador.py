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


#cursor = pygame.image.load("arrow.png")


class Cursor(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("preto/br_large.png")
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
cursor = Cursor(0, 0)
#cursor.image = pygame.image.load("bola.png")

target1 = Target(20,20)
target2 = Target(width-20,20)
target3 = Target(20,height-20)
target4 = Target(width-20,height-20)

lista.append(target1)

pcount=0
tcount=0
coords=[]
screen.fill(color)     

while 1:                   
	clock.tick(6000)	     # Loop principal do game 
	
	for event in pygame.event.get():            # Verifica eventos do teclado, mouse etc 
		if event.type == pygame.QUIT: sys.exit()     # Se o evento for do tipo QUIT encerra

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()

	pos_wii=[]
        try:
                #pos_wii = w.state['ir_src'][0]['pos']
		if pygame.mouse.get_pressed()[0]:
			pos_wii= pygame.mouse.get_pos()
			print pos_wii
		if pcount == 20:
			print 'gotcha !  '+str(pos_wii)
			coords.append(pos_wii)
			tcount = tcount + 1
		if tcount == 1:
			target1.image = pygame.image.load("ok.png")
			lista.append(target4)
			
		if tcount == 2:
			target4.image = pygame.image.load("ok.png")
			Cx = ( coords[1][0] - coords[0][0])/float(width)
			Cy = ( coords[0][1] - coords[1][1])/float(height)
			
			#Px = -coords[0][0]
			#Py = -60 
			
			lista=[]
		#	print Cx , Cy
		
				
	#		lista.append(target3)

	#	if tcount == 3:
	#		target3.image = pygame.image.load("ok.png")
	#		lista.append(target4)

	#	if tcount == 4:
	#		target4.image = pygame.image.load("ok.png")
	#		print coords

		
		pcount = pcount + 1
		
		
			
        except TypeError:
		pcount = 0 
	except ZeroDivisionError:
		print "ooops x/0"
	

	#screen.fill(color)                                   # Preenche a tela com cor de fundo 
	try:    
		pass  
		#print Cx, Cy , pos_wii[0]*Cx , pos_wii[1]*Cy
	except:
		pass	
	
	for i in lista:
		screen.blit(i.image,i.rect)
	if pos_wii and cursor.__class__.__name__ == "Cursor":
		try:
			#cursor.rect.centerx = pos_wii[0] - (coords[1][0] - coords[0][0] )/Cx 
			#print pos_wii[0] - (coords[1][0] - coords[0][0] )/Cx 
			#cursor.rect.centery = (768-pos_wii[1] - coords[1][1]) 
			cursor.rect.centerx = pos_wii[0]
			cursor.rect.centery = pos_wii[1]
		except:
			pass
		screen.blit(cursor.image,cursor.rect)

	
	pygame.display.flip()                                # Envia o que foi desenhado para o monitor 

