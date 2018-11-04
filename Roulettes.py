import sys
import turtle
import canvasvg
import math

print("\n------------------\nPROGRAM TAKES FIVE (5) INPUTS:\n\nType - Roulette Type (Epitrochoid, Hypotrochoid, Trochoid)\nR - Radius of Fixed Circle\nr - Radius of Rolling Circle\nd - Distance of Drawing Point from Center of Rolling Circle\n(OPTIONAL) Theta - Rotations (Default = 100)\n------------------\n")

def getInput():
	try:


		rouletteType = str(raw_input("Type: "))

		if(rouletteType.lower() == "e" or rouletteType.lower() == "epi" or rouletteType.lower() == "epitrochoid"):
			rouletteType = "epitrochoid"
		elif(rouletteType.lower() == "h" or rouletteType.lower() == "hypo" or rouletteType.lower() == "hypotrochoid"):
			rouletteType = "hypotrochoid"
		elif(rouletteType.lower() == "t" or rouletteType.lower() == "tro" or rouletteType.lower() == "trochoid"):
			rouletteType = "trochoid"
		else:
			raise ValueError("Bad type")

		R = float(input("R: "))

		if(rouletteType == "epitrochoid" or rouletteType == "hypotrochoid"):
			r = float(input("r: "))
		else:
			r = 0

		d = float(input("d: "))
		thetaLimit = float(input("Theta: "))

		return rouletteType, R, r, d, thetaLimit


	except(ValueError):
		print("Did not recognize type, try again")
		return getInput()

	except(SyntaxError):
		thetaLimit = 100
		return rouletteType, R, r, d, thetaLimit


rouletteType, R, r, d, thetaLimit = getInput()

if(rouletteType == "epitrochoid" or rouletteType == "hypotrochoid"):
	width = R+r+d
	turtle.setup(width*2.2, width*2.2)

else:
	width = 200
	turtle.setup(width, width/2)

pen = turtle.Turtle()
pen.pensize(1)
pen.tracer(0, 0)
pen.ht()

def Epitrochoid(R, r, d, theta):
	return [(R+r) * math.cos(theta) - d * math.cos( (R+r) * theta / float(r)) , (R+r) * math.sin(theta) - d * math.sin( (R+r) * theta / float(r))]

def Hypotrochoid(R, r, d, theta):
	return [(R-r) * math.cos(theta) + d * math.cos( (R-r) * theta / float(r)) , (R-r) * math.sin(theta) - d * math.sin( (R-r) * theta / float(r))]

def Trochoid(R, d, theta):
	return [R*theta - d*math.sin(theta), R - d*math.cos(theta)]

dTheta = 0.01

if(rouletteType == "epitrochoid"):
	theta = 0
	pen.up()
	pen.goto(Epitrochoid(R, r, d, theta))
	pen.down()
	while theta < thetaLimit*3.14:
		x = Epitrochoid(R, r, d, theta)[0]
		y = Epitrochoid(R, r, d, theta)[1]
		pen.pencolor(abs(x)/(width), abs(y)/(width), .4)
		pen.goto(x,y)
		theta += dTheta
elif(rouletteType == "hypotrochoid"):
	theta = 0
	pen.up()
	pen.goto(Hypotrochoid(R, r, d, theta))
	pen.down()
	while theta < thetaLimit*3.14:
		x = Hypotrochoid(R, r, d, theta)[0]
		y = Hypotrochoid(R, r, d, theta)[1]
		pen.pencolor(abs(x)/(width), abs(y)/(width), .4)
		pen.goto(x,y)
		theta += dTheta
elif(rouletteType == "trochoid"):
	theta = -width/(2*R)
	pen.pencolor('black')
	pen.up()
	pen.goto(Trochoid(R, d, theta))
	pen.down()
	while theta < thetaLimit*3.14 -width/(2*R):
		x = Trochoid(R, d, theta)[0]
		y = Trochoid(R, d, theta)[1]
		pen.goto(x,y)
		theta += dTheta

turtle.update()
turtle.getcanvas().postscript(file=str(rouletteType)+" drawing R="+str(R)+", r="+str(r)+", d="+str(d)+", theta="+str(thetaLimit)+".eps")
print("Roulette File Generated")
