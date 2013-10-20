# Polygon excercise from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



def polygon(turtle, sidelength):

	ang = 4

	for i in range(90):
		fd(turtle, sidelength)
		lt(turtle, ang)


def circle(turtle, rad):
	
	segmentlength = rad * 2 * 3.141592
	polygon(turtle, segmentlength)

pu(bob)
fd(bob, 700)
rt(bob)
fd(bob, 300)
pd(bob)



circle(bob, 3)















wait_for_user()					
