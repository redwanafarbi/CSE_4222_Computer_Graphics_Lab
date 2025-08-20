import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Overlapping Shapes in Random Order")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)

# Hide turtle cursor
t.hideturtle()

# Define drawing functions
def draw_rectangle():
    t.color("blue", "blue")
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

def draw_circle():
    t.color("green", "green")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def draw_triangle():
    t.color("red", "red")
    t.penup()
    t.goto(-40, 60)
    t.pendown()
    t.begin_fill()
    t.goto(40, 60)
    t.goto(0, 120)
    t.goto(-40, 60)
    t.end_fill()

# Store shape functions in a list
shapes = [draw_rectangle, draw_circle, draw_triangle]

# Shuffle the order of drawing
random.shuffle(shapes)

# Draw shapes in random order
for shape in shapes:
    shape()

# Keep the window open
turtle.done()
