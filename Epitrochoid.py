import sys
import turtle
import canvasvg
import math

try:
	R = float(sys.argv[1])
	r = float(sys.argv[2])
	d = float(sys.argv[3])
except(IndexError):
	print("\n------------------\nPROGRAM TAKES THREE INPUTS:\n\nRadius of Fixed Circle\nRadius of Rolling Circle\nDistance of Drawing Point from Center of Rolling Circle\n\nPLEASE TRY AGAIN\n------------------\n")
	sys.exit(2)

width = R+r+d
turtle.setup(width*2.2, width*2.2)
pen = turtle.Turtle()
pen.pensize(1)
pen.tracer(0, 0)
pen.ht()

dTheta = 0.01
theta = 0
pen.up()
pen.goto( (R+r) * math.cos(theta) - d * math.cos( (R+r) * theta / float(r)),(R+r) * math.sin(theta) - d * math.sin( (R+r) * theta / float(r)))
pen.down()
while theta < 50*3.14:
	x = (R+r) * math.cos(theta) - d * math.cos( (R+r) * theta / float(r))
	y = (R+r) * math.sin(theta) - d * math.sin( (R+r) * theta / float(r))
	pen.pencolor(abs(x)/(width), abs(y)/(width), .4)
	pen.goto(x,y)
	theta += dTheta

turtle.update()
turtle.getcanvas().postscript(file="Epitrochoid_Drawing.eps")