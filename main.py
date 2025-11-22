import random

import pygame
import sys
from constants import  *
from ball import Ball
from screen import Screen
from players import Player
pygame.mixer.init()
#ЗАДАЧИ - ДОБАВИТЬ ФУНКЦИЮ ГЕЙМ ОВЕР (С ВЫВОДОМ ТОГО, КТО ПОБЕДИЛ) И ДОБАВТЬ ФУНКЦИЮ ПАУЗЫ
music = random.choice(['pixelated-adventure_92830.mp3', 'pixelated-joyride_92775.mp3', 'vibrant-pixel-rush_92817.mp3', 'nostalgic-beats_92780.mp3'])
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

events = pygame.event.get()
pygame.init()
display = Screen(screen_x, screen_y)
player1 = Player(paddle_length, paddle_height, player1x, player1y, pygame.K_w, pygame.K_s, player_color, screen_y, speed)
player2 = Player(paddle_length, paddle_height, player2x, player2y, pygame.K_UP, pygame.K_DOWN, player_color, screen_y, speed)
ball = Ball(height, length, ball_color, screen_x, screen_y, reflection_count, speed_x, speed_y)
clock = pygame.time.Clock()

while True:
    display.screen.fill("black")
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

        player1.push()
        player2.push()

    display.update(ball, player1, player2, events)
    pygame.display.update()

    clock.tick(60)