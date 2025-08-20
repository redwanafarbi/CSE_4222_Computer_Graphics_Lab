import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Looping Name Animation")

# Create turtle for writing
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")
writer.speed(0)

# Constants
start_x = 300     # Starting x (right side)
end_x = -400      # End x (left side)
y_position = -100    # Fixed y position

# Infinite animation loop
while True:
    x = start_x
    while x > end_x:
        writer.clear()
        writer.goto(x, y_position)
        writer.write("Farbi", font=("Arial", 32, "bold"))
        x -= 5
        time.sleep(0.03)  # delay for smoothness
