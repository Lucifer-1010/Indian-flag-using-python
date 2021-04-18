import turtle
# 
# print(dir(turtle))
ws=turtle.Screen()
flagTurtle=turtle.Turtle()
flagTurtle.penup()
flagTurtle.goto(-180,60)


flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("orange")
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.right(90)
flagTurtle.forward(400)
flagTurtle.right(90)
flagTurtle.forward(90)
flagTurtle.right(90)
flagTurtle.forward(400)
flagTurtle.end_fill()

flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)

flagTurtle.begin_fill()
flagTurtle.fillcolor("Green")
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(400)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.left(90)
flagTurtle.forward(90)
flagTurtle.end_fill()


flagTurtle.penup()
flagTurtle.goto(23,32)
flagTurtle.pendown()
flagTurtle.begin_fill()
flagTurtle.fillcolor("blue")
flagTurtle.circle(20)
flagTurtle.end_fill()

turtle.done()




