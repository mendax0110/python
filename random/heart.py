# import the modules
import turtle

# define speed and size
turtle.speed(3)
turtle.pensize(3)


# function to draw the heart
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


# make color
turtle.color('black', 'red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
