import turtle

ninja = turtle.Turtle()
screen = turtle.Screen()

screen.title("Teenage Mutant Ninja Turtles")
screen.bgcolor("papayawhip")

for step in range(15):
    ninja.forward(50)
    ninja.left(120)



    # after a complete triangle
    print(step, step % 3)
    if step % 3 == 2:
        ninja.penup()
        ninja.forward(100)
        ninja.pendown()


screen.exitonclick()
