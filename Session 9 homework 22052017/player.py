import  pygame
from inputmanager import *
from gamemanager import *
from  playerbullet import *
from enemy import *
class Player:
    def __init__(self):
        self.x = 200
        self.y = 500
        self.image = pygame.image.load("resources/player.png")

    def draw(self, screen):
        screen.blit (self.image, (self.x - self.image.get_width()/2,
                                  self.y - self.image.get_height()/2 ))

    def run(self):
        if input_manager.right_pressed:
            self.x += 5
        if input_manager.left_pressed:
            self.x -= 5
        if input_manager.up_pressed:
            self.y -= 5
        if input_manager.down_pressed:
            self.y +=5
        if input_manager.space_pressed:
            player_bullet = PlayerBullet()
            enemy = Enemy()
            player_bullet.x = self.x
            player_bullet.y = self.y - 22
            game_manager.add(player_bullet)
            if player_bullet.y == enemy.y and player_bullet.x in range ( enemy.x - enemy.image.get_width()/2,
                                                                         enemy.x + enemy.image.get_width()/2 ):
                enemy.dead = True
