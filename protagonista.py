# coding: utf-8
import pygame, sys, glob
from pygame import *

class Player:
    def __init__(self):
        self.x = 200
        self.y = 300

        # Velocidade de animacao para Running
        self.ani_speed_init_run = 5
        self.ani_speed_run = self.ani_speed_init_run

        # Velocidade de animacao para Stand by
        self.ani_speed_init_by = 16
        self.ani_speed_by = self.ani_speed_init_by

        # Importando imagens

        # Running
        self.ani_running_R = glob.glob('Running\Right\Running *.png')
        self.ani_running_L = glob.glob('Running\Left\Running *.png')
        # Stand by
        self.ani_stand_by_R = glob.glob('Stand by\Right\Stand by *.png')
        self.ani_stand_by_L = glob.glob('Stand by\Left\Stand by *.png')
        # Jumpping
        self.ani_jump_R = glob.glob('Jump\Right\Jump *.png')
        self.ani_jump_L = glob.glob('Jump\Left\Jump *.png')
        # Shotting
        self.ani_shotting_R = glob.glob('Shotting\Right\Shotting *.png')
        self.ani_shotting_L = glob.glob('Shotting\Left\Shotting *.png')

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

        # Índices máximos de gerar movimento
        self.ani_max_run = len(self.ani_running_R) - 1
        self.ani_max_by = len(self.ani_stand_by_R) - 1

        # Loads
        self.img_running_R = pygame.image.load(self.ani_running_R[0])
        self.img_running_L = pygame.image.load(self.ani_running_L[0])

        self.img_stand_by_R = pygame.image.load(self.ani_stand_by_R[0])
        self.img_stand_by_L = pygame.image.load(self.ani_stand_by_L[0])

        self.img_jump_R = pygame.image.load(self.ani_jump_R[0])
        self.img_jump_L = pygame.image.load(self.ani_jump_L[0])

        self.img_shotting_R = pygame.image.load(self.ani_shotting_R[0])
        self.img_shotting_L = pygame.image.load(self.ani_shotting_L[0])

    velocity = 2
    pos = 0
    previous_pos = 0
    def handle(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                self.pos = self.velocity
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.pos = 0

            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.pos = - self.velocity
            elif event.type == KEYUP and event.key == K_LEFT:
                self.pos = 0

            if self.pos != 0:
                self.previous_pos = self.pos

    def update(self, pos):
        # Running Right
        if pos == self.velocity:
            self.ani_speed_run -= 1
            self.x += pos
            if self.ani_speed_run == 0:
                self.img_running_R = pygame.image.load(self.ani_running_R[self.ani_pos_run])
                self.ani_speed_run = self.ani_speed_init_run
                if self.ani_pos_run == self.ani_max_run:
                    self.ani_pos_run = 0

                else:
                    self.ani_pos_run += 1

        # Running Left
        elif pos == - self.velocity:
            self.ani_speed_run -= 1
            self.x += pos
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
                self.x += pos
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
                    self.x += pos
                    if self.ani_speed_by == 0:
                        self.img_stand_by_R = pygame.image.load(self.ani_stand_by_R[self.ani_pos_by])
                        self.ani_speed_by = self.ani_speed_init_by
                        if self.ani_pos_by == self.ani_max_by:
                            self.ani_pos_by = 0
                        else:
                            self.ani_pos_by += 1
