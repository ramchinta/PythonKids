import turtle

pegasus = turtle.Turtle()
pegasus.getscreen().bgcolor("#994444")

# for i in range(5):
#     pegasus.forward(10)
#     pegasus.left(216)
pegasus.penup()
pegasus.goto(-200,100)
pegasus.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()

star(pegasus,360)
turtle.done()