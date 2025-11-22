import random

import sys
from constants import  *

pygame.init()
pygame.mixer.init()
bobma_s = random.choice(['bah1.mp3', 'bah2.mp3'])
bomba_sound = pygame.mixer.Sound(bobma_s)

class Screen:
    def __init__(self, length, height):
        self.screen = pygame.display.set_mode((length, height))
        self.height = height
        self.length = length
        self.font = pygame.font.Font(None, 75)
        self.mines = []
        self.bg = pygame.image.load("area.png")  # путь к файлу
        self.bg = pygame.transform.scale(self.bg, (length, height))  # подгоняем размер картинки под наш экран
        self.paddle_png = pygame.image.load("rocket.png").convert_alpha()###
        self.paddle_png = pygame.transform.scale(self.paddle_png, (paddle_length, paddle_height))###
        self.ball_png = pygame.image.load("pong2.png").convert_alpha()
        self.ball_png = pygame.transform.scale(self.ball_png, (50, 50))
        self.bomb_png = pygame.image.load("bobma.png").convert_alpha()###
        self.bomb_png = pygame.transform.scale(self.bomb_png, (100, 100))
        self.exp_png = pygame.image.load("bomb.png").convert_alpha()
        self.exp_png = pygame.transform.scale(self.exp_png, (100, 100))
        self.paused = False



    def add_mine(self, new_mine):
        self.mines.append(new_mine)

    def remove_mine(self, mine):
        if mine in self.mines:
            self.mines.remove(mine)

    def draw_paddle(self, paddle_rect):
        self.screen.blit(self.paddle_png, (paddle_rect.x, paddle_rect.y)) ###

    def draw_ball(self, ball):
        self.screen.blit(self.ball_png, (ball.x, ball.y))  ###

    def draw_bomb(self, bomb):
        self.screen.blit(self.bomb_png, (bomb.x, bomb.y))

    def draw_exp(self, exp):
        for i in range (0, 30):
            self.screen.blit(self.exp_png, (exp.x, exp.y))

   # def draw_game_over(self, player1, player2): ------ РЕАЛИЗОВАТЬ ГЕЙМ ОВЕР


    def update(self, ball, player1, player2, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # буква P для паузы
                    self.paused = not self.paused  # включить/выключить паузу

        if self.paused:
            return

        #if player1.score >= 10 or player2.score >= 10: ------ РЕАЛИЗОВАТЬ ГЕЙМ ОВЕР
            self.draw_game_over(player1, player2)
            pygame.display.update()
            pygame.time.wait(3000)  # показать надпись 3 секунды
            pygame.quit()
            sys.exit()
            return
        self.screen.blit(self.bg, (0,0))

        pygame.draw.aaline(self.screen, "white", (self.length / 2, 0), (self.height / 2, 0))

        player1.player_move()

        self.draw_paddle(player1.player)###


        player2.player_move()

        self.draw_paddle(player2.player)###

        score_text1 = self.font.render(f"SCORE: {player1.score}", True, text_color)
        score_text2 = self.font.render(f"SCORE: {player2.score}", True, text_color)
        self.screen.blit(score_text1, (self.length / 5, 30))
        self.screen.blit(score_text2, (self.length / 5 * 3, 30))

        ball.move(player1, player2, self)
        ball.draw(self.screen)
        self.draw_ball(ball.ball)  ###

        for mine in self.mines:
            self.draw_bomb(mine.mine)
            if ball.ball.colliderect(mine.mine):
                self.draw_exp(mine.mine)
                bomba_sound.play()
                if ball.speed_x > 0:
                    self.mines.remove(mine)
                    player2.score += 1
                if ball.speed_x < 0:
                    self.mines.remove(mine)
                    player1.score += 1




