from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	
bill = Turtle()

def square(t, sidelength):
	for i in range(4):
		fd(t, sidelength)
		lt(t)



square(bill, 100)

pu(bob)
rt(bob)
fd(bob, 100)

square(bob, 50)




