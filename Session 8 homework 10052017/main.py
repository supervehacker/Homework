# LỖI : ĐẨY HỘP DỌC ??

import pygame

pygame.init()
pygame.display.set_caption("Sokoban")


clock = pygame.time.Clock()

mario_image = pygame.image.load ("mario.png")
square_image = pygame.image.load ("square.png")
box_image = pygame.image.load("box.png")
gate_image = pygame.image.load("gate.png")
ob_image = pygame.image.load ("ob.png")
win_image = pygame.image.load ("win.png")

square_width = square_image.get_width()
square_height = square_image.get_height()

screen = pygame.display.set_mode ( (555, 555) )

#lEVEL DATA
size = {
    "height": 7,
    "width": 6
}
mario = {
    "x": 3,
    "y": 4
}

boxes = [
    {
        "x": 1,
        "y": 2
    },
    {
        "x": 4,
        "y": 3
    }
]

s_points = [
    {
        "x": 2,
        "y": 1
    },
    {
        "x": 3,
        "y": 2
    }
]

obs = [
    {
        "x": 2,
        "y": 5
    },
    {
        "x": 5,
        "y": 3
    }
]

def f(x):  # có square_width = squard height
    return (x * square_width - square_width / 2 + 33 )
def g(y):
    return (y* square_height - square_height/ 2 + 33 )

def in_map (point):
    return point['x']>= 0 and point['x'] < size['width']\
           and point['y'] >= 0 and point ['y'] < size['height']
def same_point (point1, point2):
    return point1 ['x'] == point2 ['x'] and point1['y'] == point2['y']
def position_in_list(points, x, y):
    for point in points:
        if point['x'] == x and point['y'] ==y:
            return points.index(point)
    return None
def move_point ( point, dx, dy):
    return {
        'x': point['x'] + dx,
        'y': point['y'] + dy
        }
def to_string(points):
    return "{0},{1}".format (points['x'], points['y'])

#LOGIC
loop = True
while loop:
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
    mario_next = move_point(mario, dx, dy)

    if in_map(mario_next):
        box_index = position_in_list(boxes, mario_next['x'], mario['y'])
        if mario_next in obs:       # Có vật cản trước mặt
            print ("Bạn kô thể đi qua vật cản")
        elif box_index is not None:  # Có hộp trước mặt
            box_next = move_point(boxes[box_index], dx, dy)
            if in_map(box_next):
                if box_next in obs :    #Có vật cản trước hộp
                    print ("Bạn kô thể đẩy được hộp qua vật cản")
                elif box_next in boxes: #Có hộp khác trước hộp
                    print ("Bạn kô thể dẩy được 2 hộp")
                else:
                    mario = mario_next
                    boxes[box_index] = box_next
        else:
            mario = mario_next
    else:
        print ("Bạn kô đc ra khỏi máp")


#VẼ
    screen.fill((245, 184, 240))

    for x in range(size ["width"]):     #map
        for y in range(size ["height"]):
            screen.blit (square_image, (f(x), g(y)))

    for i in range (len(obs)):          #vật cản
        screen.blit ( ob_image, ( f(obs[i]['x']), g(obs[i]['y']) ))

    for i in range (len(s_points)):     #s_points
        screen.blit(gate_image, ( f(s_points[i]['x']), g(s_points[i]['y'])))

    for i in range (len(boxes)):        #hộp
        screen.blit(box_image, ( f(boxes[i]['x']), g(boxes[i]['y'])))

    screen.blit(mario_image, ( f(mario['x']) , g(mario['y']) ))     #người chơi

    pygame.display.flip ()
    clock.tick(69)

# Win
    box_string_list = set([to_string(box) for box in boxes])
    s_stringlist = set([to_string(s) for s in s_points])
    if box_string_list == s_stringlist:
        print ("You WON !!!")
        screen.blit(win_image, (100, 100))
        loop = False