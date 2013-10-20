# Polygon excercise from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

bob.delay = 0.03 

import math

def arc(turtle, rad, theta, sidenumber):


	circumfer = rad * 2 * math.pi
	segmentlength = circumfer/sidenumber

	for i in range(sidenumber):
		fd(turtle, segmentlength)
		lt(turtle, (theta/sidenumber))


pu(bob)
fd(bob, 700)
rt(bob)
fd(bob, 300)
pd(bob)

arc(bob, 120, 301, 34)





wait_for_user()					
