# Polygon excercise from Week 0

# Name: Steve Gallagher


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



def polygon(turtle, sidelength, sidenumber):

	ang = 360/sidenumber

	for i in range(sidenumber):
		fd(turtle, sidelength)
		lt(turtle, ang)


polygon(bob, 4, 30)














wait_for_user()					
