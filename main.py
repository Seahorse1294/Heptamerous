import turtle

shapeResize = 2.5

# Screen definition
scr = turtle.Screen()
scr.bgcolor("white")

# Turtle Definition
sea = turtle.Turtle()
sea.color("white", "lightblue")
sea.shape("turtle")
sea.width(7)
sea.speed(25)  # Just to make it faster
sea.setposition(-170, 200)  # To get the logo in the middle

# Method for shapes
# Length Ratios, Short length vertex is A, Medium length vertex is B, Long length vertex is C.
perimeter = 99 + 43 + 79  # 221
long = 99 / perimeter * shapeResize
short = 43 / perimeter * shapeResize
medium = 79 / perimeter * shapeResize
shapeSize = 300

# Angles
ABC = 129.3  # Side B's angle
BCA = 75.7  # Side C's angle
CAB = 155.0  # Side A's angle

triangles = []
num_of_triangles = 7

colours = ["purple", "blue", "lightblue", "green", "yellow", "orange", "red"]


# Draw shapes
def drawBig(side1, deg1, side2, deg2, side3, deg3, outline, fill):
    sea.begin_fill()
    sea.color(outline, fill)
    sea.forward(side1 * shapeSize)
    sea.right(deg1)
    sea.forward(side2 * shapeSize)
    sea.right(deg2)
    sea.forward(side3 * shapeSize)
    sea.right(deg3)
    sea.end_fill()
    reposition()


def reposition():
    sea.penup()
    sea.right(89.5)
    sea.forward(53.4 / perimeter * shapeResize * shapeSize)
    sea.right(90)
    sea.forward(13 / perimeter * shapeResize * shapeSize)
    sea.right(ABC)
    sea.pendown()


def finalTriangle():
    sea.penup()
    sea.color("white", "purple")
    sea.setheading(0)
    sea.right(90)
    sea.forward(5)
    sea.left(90)
    sea.forward(43.5 / perimeter * shapeResize * shapeSize)
    sea.pendown()
    sea.begin_fill()
    sea.forward((99 - 43.5) / perimeter * shapeResize * shapeSize)
    sea.right(CAB)
    sea.forward(medium * shapeSize - 32)
    sea.right(BCA + 53)
    sea.forward(30 / perimeter * shapeResize * shapeSize)
    sea.end_fill()


def writeName():
    sea.penup()
    sea.setposition(-245, -300)
    sea.color("black")
    sea.write("heptamerous", font=("Delvon Thin", int(35 / perimeter * shapeResize * shapeSize), "normal"))


for i in range(num_of_triangles):
    drawBig(long, CAB, medium, BCA, short, ABC, "white", colours[i])

finalTriangle()

sea.penup()
sea.home()

writeName()

# Quit
scr.exitonclick()
