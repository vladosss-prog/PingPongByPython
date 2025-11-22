# import pygame
# import sys
# import random
# from constants import  *
# from pygame.sysfont import font_constructor
# from rich.markup import render
#
# pygame.init()
#
# def Keys(key, pl1_y, pl2_y):
#     if key[pygame.K_w] and pl1_y > 0: player1.y -= 1
#     if key[pygame.K_s] and pl1_y < 720 - 150: player1.y += 1
#     if key[pygame.K_UP] and pl2_y > 0: player2.y -= 1
#     if key[pygame.K_DOWN] and pl2_y < 720-150: player2.y += 1
#
# ball = pygame.Rect(640,360,50,50)
# mine = pygame.Rect(random.randint(300, 1000),random.randint(200, 500), 50, 50)
# player1 = pygame.Rect(0, 275, 25, 150)
# player2 = pygame.Rect(1255, 275, 25, 150)
#
#
# screen = pygame.display.set_mode((1280,720))
# clock = pygame.time.Clock()
#
# while True:
#     screen.fill("black")
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#
#     pygame.draw.ellipse(screen, 'green', ball)
#     pygame.draw.rect(screen, "white", player1)
#     pygame.draw.rect(screen, "white", player2)
#     font = pygame.font.Font(None, 36)
#     score1_text = font.render(f"Score 1: {score1}", True, 'white')
#     score2_text = font.render(f"Score 2: {score2}", True, 'white')
#     screen.blit(score1_text, (50, 10))
#     screen.blit(score2_text, (1100, 10))
#     ball.x += speed_x
#     ball.y += speed_y
#
#     if ball.y + 50 > 720: speed_y *= -1
#     if ball.y < 0: speed_y *= -1
#
#     key = pygame.key.get_pressed()
#
#     Keys(key, player1.y, player2.y)
#
#     if ball.x + 50 > 1280:
#         score1 += 1
#         ball.x = 640
#         ball.y = 360
#
#     if ball.x < 0:
#         score2 += 1
#         ball.x = 640
#         ball.y = 360
#
#
#     if ball.colliderect(player1) or ball.colliderect(player2):
#         speed_x *= -1
#         reflection_count += 1
#
#         if reflection_count % 2 == 0:
#             mine = pygame.Rect(random.randint(300, 1000), random.randint(200, 500), 50, 50)
#
#     if mine:
#         pygame.draw.ellipse(screen, (255, 0, 0), mine)
#
#     if mine and ball.colliderect(mine):
#         if speed_x > 0:
#             mine = None
#             score2 += 1
#         if speed_x < 0:
#             mine = None
#             score1 += 1
#
#
#     pygame.display.update()
#     clock.tick(60)
#
