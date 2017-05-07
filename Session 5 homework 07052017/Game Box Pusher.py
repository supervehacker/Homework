size = {
    "height": 7,
    "width": 6 
    }
c = {
    "x": 2,
    "y": 1
    }
b = {
    "x": 1,
    "y": 2
    }
s = {
    "x": 1,
    "y": 1
    }
b2 = {
    "x": 4,
    "y": 3
    }
s2 = {
    "x": 4,
    "y": 2
    }
#Initian Position
cx0 = c['x']
cy0 = c['y']
bx0 = b['x']
by0 = b['y']
b2x0 = b2['x']
b2y0 = b2['y']

# Function
    #Map display function
def display_map (size, c, b, s):
    for y in range (size["height"]):
        for x in range (size["width"]):
            if x == c["x"] and y == c["y"]:
                print (" C ", end = "")
            elif x == b["x"] and y == b["y"]:
                print (" B ", end = "")
            elif x == s["x"] and y == s["y"]:
                print (" S ", end = "")
            elif x == b2["x"] and y == b2["y"]:
                print (" B2", end = "")
            elif x == s2["x"] and y == s2["y"]:
                print (" S2", end = "")
            else:
                print ( " - ", end = "" )
        print ()
    # Hit the wall function
def wall ( x, y ):
    if x > size["width"] - 1 or x < 0 or y > size["height"] - 1 or y < 0:
        c['x'] = cx
        c['y'] = cy
        b['x'] = bx
        b['y'] = by
        b2['x'] = b2x
        b2['y'] = b2y
    return x,y

print ("Control:\nW = up\nS = down\nA = left\nD = right\nR = Restart current level")
step = 0
loop = True
while (loop):
# GRAPHICS:
    display_map (size, c, b, s)
    
# LOGIC (GAMEPLAY):
    step += 1
    move = input("Your move?").upper()
    # => de cho move = chu hoa luon
    if move == "W":
        c["y"] -= 1
    elif move == "S":
        c["y"] += 1
    elif move == "A":
        c["x"] -= 1      
    elif move == "D":
        c["x"] += 1
    elif move == "R":
        c['x'] = cx0
        c['y'] = cy0
        b['x'] = bx0
        b['y'] = by0
        b2['x'] = b2x0
        b2['y'] = b2y0
        step = 0
    else:
        print ("You have to choose your move among W, A, S, D")

    #C hit the wall
    c["x"] = wall ( c["x"], c["y"] ) [0]
    c["y"] = wall ( c["x"], c["y"] ) [1]
    #Box pushing
    if c['x'] == b['x'] and c['y'] == b['y']:
        b['x'] +=  b['x'] - cx
        b['y'] +=  b['y'] - cy
    if c['x'] == b2['x'] and c['y'] == b2['y']:
        b2['x'] +=  b2['x'] - cx
        b2['y'] +=  b2['y'] - cy   
    #Box 1, 2 hit the wall
    b["x"] = wall ( b["x"], b["y"] ) [0]
    b["y"] = wall ( b["x"], b["y"] ) [1]
    b2["x"] = wall ( b2["x"], b2["y"] ) [0]
    b2["y"] = wall ( b2["x"], b2["y"] ) [1]
    #C and Box current positions    
    cx = c['x']
    cy = c['y']
    bx = b['x']
    by = b['y']
    b2x = b2['x']
    b2y = b2['y']
    
    #Win
    if b['x'] == s['x'] and b['y'] == s['y'] and b2['x'] == s2['x'] and b2['y'] == s2['y']:
        loop = False
    elif b['x'] == s2['x'] and b['y'] == s2['y'] and b2['x'] == s['x'] and b2['y'] == s['y']:
        loop = False
display_map (size, c, b, s)
print ( "YOU WIN!!!" )
print ("Your steps: {0}".format(step))
