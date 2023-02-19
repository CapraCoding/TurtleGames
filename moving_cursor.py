from turtle import Screen, Turtle

sanic = Turtle()
screen = Screen()
screen.colormode(255)


def move_forwards():
    sanic.forward(10)

def move_backward():
    sanic.backward(10)

def left():
    new_heading = sanic.heading() + 10
    sanic.setheading(new_heading)


def right():
    new_heading = sanic.heading() - 10
    sanic.setheading(new_heading)

def clear():
    sanic.clear()
    sanic.home()

screen.listen()
sanic.degrees()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)


screen.exitonclick()