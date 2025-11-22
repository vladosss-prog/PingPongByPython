import pygame
from constants import  *

class Player:
    def __init__(self, paddle_l,  paddle_h, paddle_x, paddle_y, key_up, key_down, color, screen_y, speed):
        self.player = pygame.Rect(paddle_x, paddle_y, paddle_l, paddle_h)
        self.paddle_h = paddle_h
        self.paddle_l = paddle_l
        self.key_up = key_up
        self.key_down = key_down
        self.key = pygame.key.get_pressed()
        self.score = 0
        self.color = color
        self.screen_y = screen_y
        self.speed = speed


    # def push(self, event):
    #     if event.type == self.key_up and self.player.y >= 0: self.speed = -1
    #     if event.type == self.key_down and self.player.y + self.paddle_h < 720: self.speed = 1

    # def push(self, event):
    #     if event.type == pygame.KEYDOWN: #Когда клавиша нажата
    #         if event.key == self.key_up and self.player.y > 0:
    #             self.speed = -1
    #         elif event.key == self.key_down and self.player.y + self.paddle_h < self.screen_y:
    #             self.speed = 1
    #     if event.type == pygame.KEYUP:
    #         self.speed = 0

    def push(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_up] and self.player.y > 0:
            self.speed = -20
        elif keys[self.key_down] and self.player.y + self.player.height < self.screen_y:
            self.speed = 20
        else:
            self.speed = 0


    def player_move(self):
        self.player.y += self.speed

        self.player.y = max(0, min(self.player.y, self.screen_y - self.player.height)) #Если наша координата = 0, то минимальное значение берется как ноль и соотв-но мы принуждаем ее оставаться нулем, иначе мы принуждаем координату оставаться максимумом из возможной!!!!
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.player)
