# coding: utf-8
import pygame, glob
from pygame import *
from os import sep

pygame.init()

class Player:
	def __init__(self):
		self.x = 200
		self.y = 300
		# Velocidade de movimento
		self.velocity = 4
		# Posicao
		self.pos = 0
		# Posicao anterior para executar as sprites de Stand by
		self.previous_pos = 0
		
		# Para atirar
		self.shot = False

		# Velocidade de animacao para Running
		self.ani_speed_init_run = 4
		self.ani_speed_run = self.ani_speed_init_run

		# Velocidade de animacao para Stand by
		self.ani_speed_init_by = 15
		self.ani_speed_by = self.ani_speed_init_by

		# Velocidade de animacao para Shotting
		self.ani_speed_init_shot = 3
		self.ani_speed_shot = self.ani_speed_init_shot

		# Importando imagens

		# Running
		self.ani_running_R = glob.glob('Running' + sep + 'Right' + sep + 'Running *.png')
		self.ani_running_L = glob.glob('Running' + sep + 'Left' + sep + 'Running *.png')
		# Stand by
		self.ani_stand_by_R = glob.glob('Stand by' + sep + 'Right' + sep + 'Stand by *.png')
		self.ani_stand_by_L = glob.glob('Stand by' + sep + 'Left' + sep + 'Stand by *.png')
		# Jumpping
		self.ani_jump_R = glob.glob('Jump' + sep + 'Right' + sep + 'Jump *.png')
		self.ani_jump_L = glob.glob('Jump' + sep + 'Left' + sep + 'Jump *.png')
		# Shotting
		self.ani_shotting_R = glob.glob('Shotting' + sep + 'Right' + sep + 'Shotting *.png')
		self.ani_shotting_L = glob.glob('Shotting' + sep + 'Left' + sep + 'Shotting *.png')

		# Ordenação das imagens
		self.ani_running_R.sort()
		self.ani_running_L.sort()
		self.ani_stand_by_R.sort()
		self.ani_stand_by_L.sort()
		self.ani_jump_R.sort()
		self.ani_jump_L.sort()
		self.ani_shotting_R.sort()
		self.ani_shotting_L.sort()

		# Variáveis de movimento
		self.ani_pos_run = 0
		self.ani_pos_by = 0
		self.ani_pos_shot = 0

		# Índices máximos de gerar movimento
		self.ani_max_run = len(self.ani_running_R) - 1
		self.ani_max_by = len(self.ani_stand_by_R) - 1
		self.ani_max_shot = len(self.ani_shotting_R) - 1

		# Loads
		self.img_running_R = pygame.image.load(self.ani_running_R[0])
		self.img_running_L = pygame.image.load(self.ani_running_L[0])

		self.img_stand_by_R = pygame.image.load(self.ani_stand_by_R[0])
		self.img_stand_by_L = pygame.image.load(self.ani_stand_by_L[0])

		self.img_jump_R = pygame.image.load(self.ani_jump_R[0])
		self.img_jump_L = pygame.image.load(self.ani_jump_L[0])

		self.img_shotting_R = pygame.image.load(self.ani_shotting_R[0])
		self.img_shotting_L = pygame.image.load(self.ani_shotting_L[0])


	def handle(self, event):
		if event.type == KEYDOWN:
			self.animation()
			
		elif event.type == KEYUP:	
			if self.pos != 0:
				self.previous_pos = self.pos
				self.pos = 0
	
	# Imprime as sprites
	def update(self, pos):
		
		# Running Right
		if self.pos == self.velocity:
			self.ani_speed_run -= 1
			self.x += self.pos
			if self.ani_speed_run == 0:
				self.img_running_R = pygame.image.load(self.ani_running_R[self.ani_pos_run])
				self.ani_speed_run = self.ani_speed_init_run
				if self.ani_pos_run == self.ani_max_run:
					self.ani_pos_run = 0

				else:
					self.ani_pos_run += 1

		# Running Left
		elif self.pos == - self.velocity:
			self.ani_speed_run -= 1
			self.x += self.pos
			if self.ani_speed_run == 0:
				self.img_running_L = pygame.image.load(self.ani_running_L[self.ani_pos_run])
				self.ani_speed_run = self.ani_speed_init_run
				if self.ani_pos_run == self.ani_max_run:
					self.ani_pos_run = 0

				else:
					self.ani_pos_run += 1

		# Stand by
		else:
			
			if self.previous_pos == - self.velocity:
				self.ani_speed_by -= 1
				if self.ani_speed_by == 0:
					self.img_stand_by_L = pygame.image.load(self.ani_stand_by_L[self.ani_pos_by])
					self.ani_speed_by = self.ani_speed_init_by

					if self.ani_pos_by == self.ani_max_by:
						self.ani_pos_by = 0
					else:
						self.ani_pos_by += 1

			else:
				if self.previous_pos == self.velocity:
					self.ani_speed_by -= 1
					if self.ani_speed_by == 0:
						self.img_stand_by_R = pygame.image.load(self.ani_stand_by_R[self.ani_pos_by])
						self.ani_speed_by = self.ani_speed_init_by

						if self.ani_pos_by == self.ani_max_by:
							self.ani_pos_by = 0
						else:
							self.ani_pos_by += 1

	
	# Verifica qual acao realizar
	def animation(self):
		pygame.event.pump()
		key = pygame.key.get_pressed()
		if key[pygame.K_c]:
			self.shot = True
							
		else:
			self.shot = False
			if key[pygame.K_LEFT]:
				self.pos = - self.velocity

			if key[pygame.K_RIGHT]:
				self.pos =  self.velocity
			
	def shot_now(self):
		if self.previous_pos == self.velocity:
			if self.pos == 0:
				self.ani_speed_shot -= 1
				if self.ani_speed_shot == 0:
					self.img_shotting_R = pygame.image.load(self.ani_shotting_R[self.ani_pos_shot])
					self.ani_speed_shot = self.ani_speed_init_shot
					if self.ani_pos_shot == self.ani_max_shot:
						self.ani_pos_shot = 0
				
					else:
						self.ani_pos_shot += 1
		
		elif self.previous_pos == - self.velocity:
			if self.pos == 0:
				self.ani_speed_shot -= 1
				if self.ani_speed_shot == 0:
					self.img_shotting_L = pygame.image.load(self.ani_shotting_L[self.ani_pos_shot])
					self.ani_speed_shot = self.ani_speed_init_shot
					if self.ani_pos_shot == self.ani_max_shot:
						self.ani_pos_shot = 0
				
					else:
						self.ani_pos_shot += 1
