import  pygame

class PlayerBullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load ("resources/player_bullet.png")

    def draw(self, screen):
        screen.blit (self.image, (self.x - self.image.get_width()/2,
                                  self.y - self.image.get_height()/2 ))

    def run(self):
        self.y -= 11