##VER 3: BUGS FIXED, SOUND ADDED

#Level data
size = {
    "height": 7,
    "width": 6 
    }
c = {
    "x": 0,
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
o = {
    "x": 2,
    
    "y": 5
    }
o2 = {
    "x": 1,
    "y": 3
    }
ob = [o, o2]
    #Initial positions
cx = cx0 = c['x']
cy = cy0 = c['y']
bx = bx0 = b['x']
by = by0 = b['y']
b2x = b2x0 = b2['x']
b2y = b2y0 = b2['y']

# FUNCTION
    #Map display
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
                print (" B ", end = "")
            elif x == s2["x"] and y == s2["y"]:
                print (" S ", end = "")
            elif x == o["x"] and y == o["y"]:
                print (" # ", end = "")
            elif x == o2["x"] and y == o2["y"]:
                print (" # ", end = "")
            else:
                print ( " - ", end = "" )
        print ()
    #Hit the wall
def wall ( x, y ):
    for i in range ( len(ob) ):
        if (x == size["width"] or x == - 1 or y == size["height"] or y == -1) or ( x == ob[i]['x'] and y == ob[i]['y'] ):
            c['x'] = cx
            c['y'] = cy
            b['x'] = bx
            b['y'] = by
            b2['x'] = b2x
            b2['y'] = b2y
    return x,y

print ("Box Pusher the awesome game ver 3")
print ("Control:\nW = up\nS = down\nA = left\nD = right\nR = Restart current level\n\nLoading level \n.\n.\n.")
step = 0
life = 5
# SFX
import winsound
winsound.PlaySound('intro.wav',winsound.SND_FILENAME)
loop = True
while (loop):
# GRAPHICS:
    display_map (size, c, b, s)
    
# LOGIC:
    step += 1
    #C moving
    move = input("Your move?").upper()
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
        life -= 1
        print ("Restarting\n.\n.\n.")
        winsound.PlaySound('restart.wav',winsound.SND_FILENAME)
    else:
        print ("You have to choose your move among W, A, S, D or choose R to restart the level")
    #Box pushing
    if c['x'] == b['x'] and c['y'] == b['y']:
        b['x'] +=  b['x'] - cx
        b['y'] +=  b['y'] - cy
    if c['x'] == b2['x'] and c['y'] == b2['y']:
        b2['x'] +=  b2['x'] - cx
        b2['y'] +=  b2['y'] - cy       
    #Wall hitting
    c["x"] = wall ( c["x"], c["y"] ) [0]
    c["y"] = wall ( c["x"], c["y"] ) [1]
    b["x"] = wall ( b["x"], b["y"] ) [0]
    b["y"] = wall ( b["x"], b["y"] ) [1]
    b2["x"] = wall ( b2["x"], b2["y"] ) [0]
    b2["y"] = wall ( b2["x"], b2["y"] ) [1]
    #Current positions    
    cx = c['x']
    cy = c['y']    
    bx = b['x']
    by = b['y']
    b2x = b2['x']
    b2y = b2['y']
    #Win
    if ( b['x'] == s['x'] and b['y'] == s['y'] and b2['x'] == s2['x'] and b2['y'] == s2['y'] ) or ( b['x'] == s2['x'] and b['y'] == s2['y'] and b2['x'] == s['x'] and b2['y'] == s['y']) :
        display_map (size, c, b, s)
        print ( "YOU WIN!!!" )
        print ("Your steps: {0}".format(step))
        winsound.PlaySound('win.wav',winsound.SND_FILENAME)
        loop = False
    #Loose
    if life == 0 :
        print ("You've played this level 5 times, even a monkey can do better than you :( ")
        winsound.PlaySound('loose.wav',winsound.SND_FILENAME)
        loop = False
