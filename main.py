import turtle

# Screen definition
scr = turtle.Screen()
scr.bgcolor("lightgrey")

# Turtle Definition
sea = turtle.Turtle()
sea.color("white", "lightblue")
sea.shape("turtle")
sea.width(6)

# Method for shapes
# Length Ratios
perimeter = 99 + 43 + 79
hyp = 99 / perimeter
short = 43 / perimeter
long = 79 / perimeter
shapeSize = 300

# Angles
hypA = 128
shortA = 180 - 50.55
longA = 180 - 104.59

triangles = []
num_of_triangles = 7


# Draw shapes
def drawBig(deg1, side1, deg2, side2, deg3, side3, outline, fill):
    sea.begin_fill()
    sea.color(outline, fill)
    sea.left(deg1)
    sea.forward(side1 * shapeSize)
    sea.left(deg2)
    sea.forward(side2 * shapeSize)
    sea.left(deg3)
    sea.forward(side3 * shapeSize)
    sea.end_fill()


def reposition():
    sea.forward(80)


for i in range(num_of_triangles):
    drawBig(hypA, hyp, longA, long, shortA, short)

# Quit
scr.exitonclick()
