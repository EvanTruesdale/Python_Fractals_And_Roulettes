import turtle
import canvasvg

depth = input("Depth: ")
width = 500
turtle.setup(2.2*width, 2.2*width)

pen = turtle.Turtle()
pen.pensize(.1)
pen.pencolor('black')
pen.tracer(0, 0)
pen.ht()

points = [[-width, -2*width/3], [0, 5*width/6], [width, -2*width/3]]

def getMid(p1, p2):
	return ( (p1[0]+p2[0]) / float(2), (p1[1]+p2[1]) / float(2) )

def triangle(points, depth):

	if depth>0:
		triangle([points[0],
				  	getMid(points[0], points[1]),
			      	getMid(points[0], points[2])],
			    depth - 1)
		triangle([points[1],
				  	getMid(points[1], points[2]),
			      	getMid(points[1], points[0])],
			    depth - 1)
		triangle([points[2],
				  	getMid(points[2], points[0]),
			      	getMid(points[2], points[1])],
			    depth - 1)
	if depth == 0:
		pen.up()
		pen.goto(points[0][0], points[0][1])
		pen.down()
		pen.goto(points[1][0], points[1][1])
		pen.goto(points[2][0], points[2][1])
		pen.goto(points[0][0], points[0][1])

triangle(points, depth)
turtle.update()

turtle.getcanvas().postscript(file="Sierpinkski Triangle Vector Map Depth="+str(depth)+".eps")
