import turtle

kamo = turtle.Screen()
kamo.bgcolor('black')

jod = turtle.Turtle()
jod.shape('turtle')
jod.color('#e7fc03' , 'red')
jod.begin_fill()
jod.forward(100)
jod.left(90)
jod.forward(100)
jod.left(90)
jod.forward(100)
jod.left(90)
jod.forward(100)
jod.end_fill()

jod.penup()
jod.forward(100)
jod.pendown()

if jod.pencolor() == '#e7fc03':
    jod.pencolor('orange')
    

fraud = turtle.Turtle()
fraud.shape('turtle')
fraud.color('#03fcf0')
fraud.forward(200)
fraud.left(90)
fraud.forward(200)
fraud.left(90)
fraud.forward(200)
fraud.left(90)
fraud.forward(200)
if fraud.xcor() < 270 and fraud.ycor() < 280:
    fraud.goto(80,180)
# Sets the coordinate
fraud.forward(200)

if fraud.heading() >=90 and fraud.heading() <=270:
    fraud.setheading(180)
# sets the direction
fraud.forward(100)

kamo.exitonclick()
turtle.done()