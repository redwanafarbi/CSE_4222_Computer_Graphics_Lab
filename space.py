import turtle
import random

NUM_STARS = 200
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#08090F")
screen.title("Travel Through Space")
screen.tracer(0)

stars = []

def reset_star(star):
    star.hideturtle()
    star.goto(random.randint(-90, 90), random.randint(-100, 100))
    star.speed_factor = random.uniform(0.02, 0.08)
    star.shapesize(0.1)
    star.showturtle()

for _ in range(NUM_STARS):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.penup()
    reset_star(star)
    stars.append(star)

def move_stars():
    for star in stars:
        x, y = star.position()
        star.goto(x * (1 + star.speed_factor), y * (1 + star.speed_factor))

        distance = star.distance(0, 0)
        new_size = 0.1 + (distance / SCREEN_WIDTH) * 2
        star.shapesize(new_size)

        if abs(star.xcor()) > SCREEN_WIDTH / 2 or abs(star.ycor()) > SCREEN_HEIGHT / 2:
            reset_star(star)

    screen.update()
    screen.ontimer(move_stars, 33)

move_stars()
turtle.done()