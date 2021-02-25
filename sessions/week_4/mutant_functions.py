import turtle


def draw_square_100(painter):
    for _ in range(4):
        painter.forward(100)
        painter.left(90)


def draw_square(painter, size):
    for _ in range(4):
        painter.forward(size)
        painter.left(90)


if __name__ == '__main__':
    ninja = turtle.Turtle()
    screen = turtle.Screen()

    for square_size in range(10, 200, 20):
        draw_square(ninja, square_size)

    screen.exitonclick()
