import turtle


def main():
    # setup and calibrate pen
    t = turtle.Turtle()
    t.getscreen().bgcolor("black")
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("blue")
    t.speed(30)
    draw_star(t, 360)
    turtle.done()


def draw_star(turtle_obj, size):
    # stopping condition
    if size <= 10:
        return
    else:
        turtle_obj.begin_fill()
    # 5 points as it is a star
    for i in range(5):
        turtle_obj.forward(size)
        # recursive call
        draw_star(turtle_obj, size / 3)
        turtle_obj.left(216)
        turtle_obj.end_fill()


if __name__ == '__main__':
    main()
