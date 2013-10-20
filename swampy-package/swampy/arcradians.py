# Polygon excercise from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				


import math



def arc(turtle, rad, theta):


	circumfer = rad * 2 * math.pi
	segmentlength = circumfer/120

	thetaconversion = 360/(2 * math.pi)

	thetadegrees = int(round(thetaconversion * theta))


	for i in range(thetadegrees/3):
		fd(turtle, segmentlength)
		lt(turtle, 3)





pu(bob)
fd(bob, 700)
rt(bob)
fd(bob, 300)
pd(bob)


arc(bob, 100, 6.3)




wait_for_user()					
