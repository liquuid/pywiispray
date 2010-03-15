#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Copyright 2010 Fernando Henrique R. Silva (liquuid@gmail.com)
# http://www.linuxmafia.com.br

# Bibliotecas para os graficos, wii, numeros randomicos etc...
import sys
import pygame
import random
import os
import cwiid

# Pega o diretorio onde o script esta sendo executado e soma a string data
dpath = os.getcwd()+"/data/"

# apresenta a mensagem inicial de modo grafico
os.system('zenity --info --text "Pressione 1 + 2 no wiimote e clique em OK"')

try:
	# conecta a biblioteca cwiid com o Wiimote
	w = cwiid.Wiimote()
	# coloca o wiimote em modo relatorio de infra vermelho
	w.rpt_mode = cwiid.RPT_IR 
except:
	os.system('zenity --error --text "Tempo esgotado durante a conexao com o wiimote"')
	sys.exit(1)


# Inicializa esses modulos
pygame.init()                                          

# Tamanho da tela
size = width, height = 640, 480

# Define a cor de fundo da tela
color = 255, 255, 255
                    
# Inicializa a janela onde rola o game 
screen = pygame.display.set_mode(size)

# Carrega o barulho do jato de tinta na memoria
ts = pygame.mixer.Sound(dpath+"ts.wav")

class Cursor(pygame.sprite.Sprite):
	"""
		Classe cursor cria objetos do tipo cursor, onde sera desenhado o jato de tinta
	
		c = Cursor( coordenada x , coordenada y)
	"""	
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(dpath+"branco/br_large.png"),[32,32])
		self.image_orig = self.image
		self.rect  = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y

class Target(pygame.sprite.Sprite):
	"""
		Classe Targate posiciona o alvo de calibragem na tela

		t = Target( coord x , coord y )
	"""
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(dpath+"x.png")
                self.rect  = self.image.get_rect()
                self.rect.centerx = x
                self.rect.centery = y
                self.estado = False

# Inicializa o timer interno do pygame
clock = pygame.time.Clock()

# lista de objetos a serem desenhados na tela
lista = [] 

# cria objeto a partir da classe cursor
cursor = Cursor(0, 0)

# cria os objetos alvo
target1 = Target(20,20)
target2 = Target(width-20,20)
target3 = Target(20,height-20)
target4 = Target(width-20,height-20)

# Adiciona objeto a lista que sera impressa na tela
lista.append(target1)

# contador de captura de posicao
pcount=0

# contador de conjuntos de captura
tcount=0

# lista de coordenadas capturadas
coords=[]

# preenche o fundo da tela
screen.fill(color)     

# carrega a imagem de fundo na memoria
wall = pygame.image.load(dpath+"wall_1.jpg")

# loop principal do programa

while 1:              
	# timer, acelera o clock do programa a 600 CPS, se sua maquina aguentar :)    
	clock.tick(600)
	
	# Verifica eventos do teclado, mouse etc 
	for event in pygame.event.get():
		# Se o evento for do tipo QUIT encerra
		if event.type == pygame.QUIT: sys.exit()    
	# captura de teclas
	pressed_keys = pygame.key.get_pressed()

	# Encerra se alguem apertar o ESC
	if pressed_keys[pygame.K_ESCAPE]:
		sys.exit()
	# Fullscreen :)
	if pressed_keys[pygame.K_f]:
		pygame.display.toggle_fullscreen()
	# Limpa o muro
	if pressed_keys[pygame.K_SPACE]:
		screen.blit(wall,[0,0])
	# lista com a posicao do wiimote
	pos_wii=[]
	# leitura das coordenadas do wiimote
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
	
	# desenha tudo na tela
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

