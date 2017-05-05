##1 Finish CRUD exercise in class, simulate a clothes shop
##
##Welcome to our shop, what do you want (C, R, U, D)? C
##Enter new item: Jeans
##Our items: T-Shirt, Sweater, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? R
##Our items: T-Shirt, Sweater, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? U
##Update position? 1
##New item? Skirt
##Our items:  T-Shirt, Skirt, Jeans
##
##Welcome to our shop, what do you want (C, R, U, D)? D
##Delete position? 2
##Our items:  T-Shirt, Skirt, Jeans


hang = [ "T-Shirt", "Sweater" ]

while True:
    i= input ("Welcome to our shop, what do you want (C, R, U, D)? ")

    if i == "C":
        hang.append ( input ( "Enter new item:" ) )
        print ("Our items:", ", ".join(hang) )

    elif i == "R":
        print ("Our items:", ", ".join(hang) )

    elif i == "U":
        iU = int( input ("Update position? ")) 
        hang[iU] = input ("New item? " )
        print ("Our items:", ", ".join(hang) )

    elif i == "D":
        iD = int( input ("Delete position? ")) 
        del hang [iD]
        print ("Our items:", ", ".join(hang) )

    else:
        print (" zzzz ")
