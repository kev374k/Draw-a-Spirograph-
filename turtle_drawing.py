from turtle import Turtle, Screen
import random
import turtle as t


t.colormode(255)
tim = Turtle()
tim.shape("triangle")
# tim.color("cyan")
tim.penup()
tim.setpos(0,0)
tim.pendown()
colors = ['black','blue','red','yellow','red','green','orange','purple','lavender','dark green','cyan']
directions = [0,90,180,270]


def draw_square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)

def draw_dashed_line():
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def draw_shape(n):
    '''draw shape up to the amount of sides, starting with triangle'''
    # after a triangle, each shape increases the degrees it has by +180, for each degree
    if n < 3:
        return False
    angle = 360/n
    for i in range(n+1):
        tim.forward(100)
        tim.right(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def random_walk():
    tim.pensize(10)
    tim.speed(0)
    for i in range(100):
        tim.pencolor(random_color())
        choice = random.choice(directions)
        tim.forward(25)
        tim.setheading(choice)

def draw_spirograph(gap_size):
    tim.speed(0)
    for i in range(int(360/gap_size)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)



draw_spirograph(2)
tim.penup()
tim.forward(400)

# for shape in range(3,10):
#     tim.pencolor(random.choice(colors))
#     draw_shape(shape)

# draw_dashed_line()
# draw_square()

# random_walk()
on_screen = Screen()
on_screen.exitonclick()
