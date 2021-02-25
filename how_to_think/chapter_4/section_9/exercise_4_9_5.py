import turtle


screen = turtle.Screen()
poly = turtle.Turtle()

poly.penup()
poly.setposition(-150, 0)
poly.pendown()

number_of_revolutions = 20
for i in range(number_of_revolutions * 4):
    poly.forward(i * 3)
    poly.right(90)

poly.penup()
poly.setposition(150, 0)
poly.pendown()

for i in range(number_of_revolutions * 4):
    poly.forward(i * 3)
    poly.right(89)

screen.exitonclick()
