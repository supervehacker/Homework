#Level data
size = {
    "height": 7,
    "width": 6 
    }
c = {
    "x": 0,
    "y": 1
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
    "x": 1,
    "y": 1
    },
    {
    "x": 4,
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

# FUNCTION
def position_in_list(points, x, y):
    for point in points:
        if point['x'] == x and point['y'] ==y:
            return points.index(point)
    return None
    # =>> if INTEGER : tuong duong if True, if None, if 0 tuong duong if False
def vat_can (point, obs):
    for ob in obs:
        return point['x'] == ob['x'] and point['y'] == ob['y']
def hai_hop_canh_nhau (boxes):
    boxes2 = [dict(t) for t in set([tuple(d.items()) for d in boxes])]
    return len(boxes) == len(boxes2)
def display_map (size, c, boxes, s_points):
    for y in range (size["height"]):
        for x in range (size["width"]):
            if x == c["x"] and y == c["y"]:
                print (" C ", end = "")
            elif position_in_list (boxes, x, y) is not None :
                print (" B ", end = "")
            elif position_in_list (s_points, x, y) is not None :
                print (" S ", end = "")
            elif position_in_list (obs, x, y) is not None :
                print (" # ", end = "")
            else:
                print ( " - ", end = "" )
        print ()
def in_map (size, point):
    return point['x']>= 0 and point['x'] < size['width']\
           and point['y'] >= 0 and point ['y'] < size['height']
def same_point (point1, point2):
    return point1 ['x'] == point2 ['x'] and point1['y'] == point2['y']
def move_point ( point, dx, dy):
    return {
        'x': point['x'] + dx,
        'y': point['y'] + dy
        }
def to_string(points):
    return "{0},{1}".format (points['x'], points['y'])
def to_set (points):
    return[to_strinng(point) for point in points]


print ("Box Pusher the awesome game ver 3")
print ("Control:\nW = up\nS = down\nA = left\nD = right\nR = Restart current level\n\nLoading level\n.\n.\n.")
step = 0
life = 5

loop = True
while (loop):
# GRAPHICS:
    display_map (size, c, boxes, s_points)
# LOGIC:
    step += 1
    #C moving
    move = input("Your move?").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = - 1      
    elif move == "D":
        dx = 1
    else:
        print ("You have to choose your move among W, A, S, D")
        step -= 1
    #New position:  
    c_next = move_point(c, dx, dy)
    #Box pushing
    if in_map(size, c_next):
        # Move allowed, check if there is a box front, which box front.
        box_index = position_in_list(boxes, c_next['x'], c_next['y'])
        if vat_can (c_next, obs):
            print ("You can't move")
        elif box_index is not None:
        # Box front, try to push it
            b_next = move_point(boxes[box_index], dx, dy)
            if in_map(size, b_next):
                #Check if ther is a va.t can
                if vat_can (b_next, obs):
                    print ("You can't move")
                else:
                # Do it
                    boxes[box_index] = b_next
                    c = c_next
        else:
            # No boxes ahead
            c = c_next
            
    # Win
    box_string_list = set([to_string(box) for box in boxes])
    s_stringlist = set([to_string(s) for s in s_points])
    if box_string_list == s_stringlist:
        print ("You WON, Your step:{0}".format(step))
        loop = False
