import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load ("resources/background.png")
        self.y = 0
        self.y2 = - self.image.get_height()

    def draw(self, screen):
        screen.blit (self.image, (0, self.y))
        screen.blit (self.image, (0, self.y2))

    def run(self):
        self.y += 7
        self.y2 +=7
        if self.y2 >= 0:
            self.y = 0
            self.y2 = -self.image.get_height()