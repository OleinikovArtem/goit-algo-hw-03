import turtle


def get_start_position(size: int) -> tuple[int, int]:
    start_x = -size / 2
    start_y = size * (3**0.5) / 6
    return (start_x, start_y)


def koch_curve(t, order: int, size: int):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: int = 500):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(100)
    t.penup()

    (start_x, start_y) = get_start_position(size)
    t.goto(start_x, start_y)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    order = int(input("Enter the recursion level: "))
    draw_koch_snowflake(order)
