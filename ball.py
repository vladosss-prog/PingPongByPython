import pygame
import random

from constants import colliderect_board
from players import Player
from mine import Mine
from screen import Screen
pygame.mixer.init()
colliderect_board = pygame.mixer.Sound('sounds/colliderect_board.mp3')
colliderect_player = pygame.mixer.Sound('sounds/colliderect_player.mp3')
rand_lose = random.choice(['sounds/miss1.mp3','sounds/miss2.mp3'])
#rand_lose = random.choice(['sounds/pook.mp3'])
lose = pygame.mixer.Sound(rand_lose)

class Ball:
    def __init__(self, height, length, color, screen_x, screen_y, reflection, speed_x, speed_y):# начальное состояние обьекта
        self.ball = pygame.Rect(screen_x / 2, screen_y / 2, height, length)
        self.height = height
        self.length = length
        self.speed_x = random.choice([-speed_x, speed_x])
        self.speed_y = random.choice([-speed_y, speed_y])
        self.color = color
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.reflection_count = reflection
        self.can_spawn_mine = True #Попытка пофиксить баг с минами(получилось))
        self.wait_timer = 0  # Таймер паузы

    #Стартовая позиция
    def start_pos(self):
        self.ball.x = self.screen_x / 2
        self.ball.y = self.screen_y / 2
        self.speed_x = random.choice([-self.speed_x, self.speed_x])
        self.speed_y = random.choice([-self.speed_y, self.speed_y])
        lose.play()
        self.wait_timer = 120
        self.speed_x = 10

        #Движение + создание мин в моменте
    def move(self, player1, player2, screen):
        if self.wait_timer > 0:
            self.wait_timer -= 1
            return

        self.ball.x += self.speed_x
        self.ball.y += self.speed_y

        if self.ball.x + 50 > self.screen_x:
            player1.score += 1
            self.start_pos()


        if self.ball.x < 0:
            player2.score += 1
            self.start_pos()


        if self.ball.y + 50 > self.screen_y:
            self.speed_y *= -1
            colliderect_board.play()
        if self.ball.y < 0:
            self.speed_y *= -1
            colliderect_board.play()

        if self.ball.colliderect(player1.player) or self.ball.colliderect(player2.player):
            self.speed_x *= -1.1
            self.reflection_count += 1
            colliderect_player.play()

            if self.can_spawn_mine:
                for i in range(1,2):
                    new_mine = Mine(self.screen_x, self.screen_y, self.reflection_count, self.height, self.length,
                                self.color)
                    screen.add_mine(new_mine)
                    self.can_spawn_mine = False
        else:
            self.can_spawn_mine = True

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.ball)

