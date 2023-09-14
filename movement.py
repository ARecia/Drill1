import turtle
import keyboard

turtle.shape("turtle")
def move_turtle(direction):
    if direction == "w":
        turtle.setheading(90)  # Move up
        turtle.forward(50)
        turtle.stamp()
    elif direction == "a":
        turtle.setheading(180)  # Move left
        turtle.forward(50)
        turtle.stamp()
    elif direction == "s":
        turtle.setheading(270)  # Move down
        turtle.forward(50)
        turtle.stamp()
    elif direction == "d":
        turtle.setheading(0)  # Move right
        turtle.forward(50)
        turtle.stamp()
def reset_turtle():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.stamp()
    turtle.pendown()

keyboard.on_press_key("w", lambda e: move_turtle("w"))
keyboard.on_press_key("a", lambda e: move_turtle("a"))
keyboard.on_press_key("s", lambda e: move_turtle("s"))
keyboard.on_press_key("d", lambda e: move_turtle("d"))
keyboard.on_press_key("esc", lambda e: reset_turtle())

turtle.done()
