# Polygon excercise from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				


import math


def arc(turtle, rad, theta):


	circumfer = rad * 2 * math.pi
	segmentlength = circumfer/120

	for i in range(theta/3):
		fd(turtle, segmentlength)
		lt(turtle, 3)


pu(bob)
fd(bob, 700)
rt(bob)
fd(bob, 300)
pd(bob)

arc(bob, 120, 100)





wait_for_user()					
