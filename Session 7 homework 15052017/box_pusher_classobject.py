class Map:
    def __init__(self): #constructor
        self.width = 5
        self.height = 7
        self.chaien = SKObject(2, 3, " C ")
        self.box = SKObject(1, 1, " B ")
        self.s_point = SKObject(2, 4, " S ")
        self.ob = SKObject(1, 2, " # ")
        self.objects = [self.chaien, self.box, self.s_point, self.ob]
    def print_objects(self,x, y):
        for object in self.objects:
            if object.print(x, y):
                return True
        return False
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.print_objects(x, y):
                    pass
                else:
                    print(" - ", end="")
            print()
    def process_input(self):
        move = input("Your move?").upper()
        dx = 0
        dy = 0
        if move == "D":
            dx = 1
        elif move == "A":
            dx = -1
        elif move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        else :
            print ("You can't only choose your move among W, A, S, D")
        C_next = self.chaien.calculate_next(dx, dy)
    #GAMEPLAY
        B = [self.box.x, self.box.y ]
        O = [self.ob.x, self.ob.y]
        if self.in_map( C_next):
            if self.same_point(C_next, O):
                print ("Đâm vào vật cản rồi bạn")
            elif self.same_point(C_next, B):
                B_next = self.box.calculate_next(dx, dy)
                if self.in_map(B_next):
                    if self.same_point(B_next, O):
                        print ("Đẩy vào vật cản rồi bạn")
                    else:
                        self.chaien.x = C_next[0]
                        self.chaien.y = C_next[1]
                        self.box.x = B_next[0]
                        self.box.y = B_next[1]
                else:
                    print("Đẩy vào tường rồi bạn :(...")
            else:
                self.chaien.x = C_next[0]
                self.chaien.y = C_next[1]
        else:
            print ("Đâm vào tường rồi bạn :(...")

    def in_map (self, point):
        return point[0] >= 0 and point[0] < self.width and point[1] >= 0 and point[1] < self.height
    def same_point(self, point1, point2):
        return point1[0] == point2[0] and point1[1] == point2[1]

class SKObject:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character
    def print(self, x, y):
        if self.x == x and self.y == y:
            print(self.character, end="")
            return  True
        return  False
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def calculate_next(self, dx, dy):
        return [ self.x + dx, self.y + dy]

sokoban = Map()
loop = True
while loop:
    sokoban.print()
    sokoban.process_input()
    #WIN CHECKING
    if sokoban.s_point.x == sokoban.box.x and sokoban.s_point.y == sokoban.box.y:
        loop = False
print ("WIN RỒI BẠN !!!")
sokoban.print()
