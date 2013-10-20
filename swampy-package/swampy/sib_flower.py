# Flower excercise (4.2) from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

bob.delay = .01

import math

def arc(turtle, rad, theta, sidenumber):


	circumfer = rad * 2 * math.pi
	segmentlength = circumfer/sidenumber

	for i in range(sidenumber):
		fd(turtle, segmentlength)
		lt(turtle, theta/sidenumber)



def petal(turtle, rad, theta):

	entryangle = theta/2	

	arc(turtle, rad, theta, 10)
	lt(turtle, 180 - (2 * entryangle))
	arc(turtle, rad, theta, 10)





def flower(turtle, rad, theta, petalnum):

	rotationangle = 360/petalnum
	entryangle = theta/2	
	
	for i in range(petalnum):
		petal(turtle, rad, theta)
		lt(turtle, (180-entryangle))
		lt(turtle, (rotationangle - entryangle))
		
pu(bob)
fd(bob, 500)
rt(bob)
fd(bob, 200)
pd(bob)

flower(bob, 30, 30, 18)




wait_for_user()					
