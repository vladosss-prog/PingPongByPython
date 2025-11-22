import pygame
import random
class Mine:
    def __init__(self, screen_x, screen_y, reflection_count, height, length, color):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.mine = pygame.Rect(
            int(random.randint(self.screen_x // 8, self.screen_x - self.screen_x // 8)),
            int(random.randint(self.screen_y // 8, self.screen_y - self.screen_y // 8)),
            int(height),
            int(length)
        )

        self.color = color
        self.reflection = reflection_count

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.mine)
