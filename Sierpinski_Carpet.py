import turtle
import canvasvg

depth = input("Depth: ")
width = 300
turtle.setup(1.5*width, 1.5*width)

pen = turtle.Turtle()
pen.pensize(.1)
pen.pencolor('black')
pen.tracer(0, 0)
pen.ht()

points = [[-width/2, -width/2], [-width/2, width/2], [width/2, width/2], [width/2, -width/2]]

def square(points):
	pen.up()
	pen.goto(points[0][0], points[0][1])
	pen.down()
	boxSize = points[1][1] - points[0][1]
	pen.begin_fill()
	pen.forward(boxSize)
	pen.left(90)
	pen.forward(boxSize)
	pen.left(90)
	pen.forward(boxSize)
	pen.left(90)
	pen.forward(boxSize)
	pen.end_fill()
	pen.setheading(0)

def split(points):
	newWidth = (points[1][1] - points[0][1]) / float(3)
	return [[[points[0][0], 			 points[0][1]], 			 [points[0][0], 			 points[0][1] + newWidth],   [points[0][0] + newWidth,   points[0][1] + newWidth],   [points[0][0] + newWidth,   points[0][1]]],
			[[points[0][0], 			 points[0][1] + newWidth],   [points[0][0], 			 points[0][1] + 2*newWidth], [points[0][0] + newWidth,   points[0][1] + 2*newWidth], [points[0][0] + newWidth,   points[0][1] + newWidth]],
			[[points[0][0], 			 points[0][1] + 2*newWidth], [points[0][0], 			 points[0][1] + 3*newWidth], [points[0][0] + newWidth,   points[0][1] + 3*newWidth], [points[0][0] + newWidth,   points[0][1] + 2*newWidth]],
			[[points[0][0] + newWidth, 	 points[0][1]], 			 [points[0][0] + newWidth,   points[0][1] + newWidth],   [points[0][0] + 2*newWidth, points[0][1] + newWidth],   [points[0][0] + 2*newWidth, points[0][1]]],
			[[points[0][0] + newWidth, 	 points[0][1] + newWidth], 	 [points[0][0] + newWidth,   points[0][1] + 2*newWidth], [points[0][0] + 2*newWidth, points[0][1] + 2*newWidth], [points[0][0] + 2*newWidth, points[0][1] + newWidth]],
			[[points[0][0] + newWidth, 	 points[0][1] + 2*newWidth], [points[0][0] + newWidth,   points[0][1] + 3*newWidth], [points[0][0] + 2*newWidth, points[0][1] + 3*newWidth], [points[0][0] + 2*newWidth, points[0][1] + 2*newWidth]],
			[[points[0][0] + 2*newWidth, points[0][1]], 			 [points[0][0] + 2*newWidth, points[0][1] + newWidth],   [points[0][0] + 3*newWidth, points[0][1] + newWidth],   [points[0][0] + 3*newWidth, points[0][1]]],
			[[points[0][0] + 2*newWidth, points[0][1] + newWidth],   [points[0][0] + 2*newWidth, points[0][1] + 2*newWidth], [points[0][0] + 3*newWidth, points[0][1] + 2*newWidth], [points[0][0] + 3*newWidth, points[0][1] + newWidth]],
			[[points[0][0] + 2*newWidth, points[0][1] + 2*newWidth], [points[0][0] + 2*newWidth, points[0][1] + 3*newWidth], [points[0][0] + 3*newWidth, points[0][1] + 3*newWidth], [points[0][0] + 3*newWidth, points[0][1] + 2*newWidth]]]

def tile(points, depth):
	splitcanvas = split(points)
	square(splitcanvas[4])
	if depth > 1:
		for i in range(0,9):
			if i != 4:
				tile(splitcanvas[i], depth-1)
	

tile(points, depth)
turtle.update()

turtle.getcanvas().postscript(file="Sierpinski Carpet Vector Map Depth=" + str(depth) + ".eps")
