import pygame
from playerbullet import *
from player import *
class Enemy:
    def __init__(self):
        self.x = 300
        self.y = 50
        self.image = pygame.image.load("resources/enemy.png")
        self.explosion_image = pygame.image.load ("resources/explosion.png")
        self.dead = False

    def run(self):
        self.y += 1

    def draw(self, screen):
        if not self.dead:
            screen.blit (self.image, (self.x - self.image.get_width()/2,
                                  self.y - self.image.get_height()/2 ))
        else:
            screen.blit(self.explosion_image, (self.x - self.image.get_width() / 2,
                                     self.y - self.image.get_height() / 2))