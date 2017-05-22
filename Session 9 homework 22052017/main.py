import pygame
from player import *
from enemy import *
from background import *
from inputmanager import *
from gamemanager import *


def init_pygame():
    pygame.init()
    pygame.display.set_caption("1945 xxx")
    screen = pygame.display.set_mode( (600,800))
    return screen

def handle_exit_event(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
        #return True => Sai, return phai o ngoai
    return True

def run():
    game_manager.run()


def draw(screen):
    screen.fill ((0, 0, 0))

    game_manager.draw(screen)

screen = init_pygame()
clock = pygame.time.Clock()

loop = True

# background = Background()
# player = Player()
game_manager.add(Background())
game_manager.add(Enemy())
game_manager.add(Player())


while loop:
    events = pygame.event.get()

    #Handle exit event
    loop =  handle_exit_event(events)

    input_manager.run(events)



    ## update logic
    run()
    ##update graphics
    draw(screen)

    ## delay by frame rate
    pygame.display.flip()  #=> phải lật
    clock.tick(60)
