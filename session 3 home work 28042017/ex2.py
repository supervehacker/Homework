
sizes = [ 5, 7, 300, 90, 24, 50, 75]

print ("Hello, my name is Viet Anh and these are my ship sizes\n" ,sizes)
print ("Now my biggest sheep has size", max (sizes), "let's shear it" )

sizes [ sizes.index ( max (sizes) ) ] = 8
print ("After shearing, here is my flock\n", sizes, "\n" )


for month in range (1, int( input("Con muon cat long cuu may thang ???") ) + 1 ) :

    sizes = [ s+50 for s in sizes ]

    print ("MONTH", month, ":")
    print ( "One month has passed, now here is my flock\n", sizes)
    print ("Now my biggest sheep has size", max (sizes), "let's shear it" )

    sizes [ sizes.index ( max (sizes) ) ] = 8
    print ("After shearing, here is my flock\n", sizes, "\n")


# sell my flock to travel the world
sizes = [ s+50 for s in sizes ]
print ("MONTH", month + 1 , ":")
print ( "One month has passed, now here is my flock\n", sizes)

total = sum(sizes)
print ("My flock has size in total:", total)
print( "I would get", str(total),"* 2$ =", str(total*2) ) 

