import turtle
import random

tim = turtle.Turtle()
colors = ['red','blue','purple','yellow','orange','black']

#Set colors for turtle
tim.color('red','blue')

#Set pen width
tim.width(5)

#Fill in shape with color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()
tim.color('yellow', 'black')
#write 4 times and draw square instead for loop
tim.begin_fill()
for x in range(4):
    tim.forward(100)
    tim.right(90)

tim.end_fill()

for x in range(5):
    randcolor = random.randrange(0,len(colors))
    tim.color(colors[randcolor], colors[random.randrange(0,len(colors))])
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    tim.penup()
    tim.setpos(rand1,rand2)
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()