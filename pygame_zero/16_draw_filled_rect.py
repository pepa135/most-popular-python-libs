WIDTH = 480
HEIGHT = 480


def draw():
    screen.fill("white")

    for j in range(0, 255, 16):
        for i in range(0, 255, 16):
            color = (0, i, j)
            rect = Rect((20+i, 20+j), (14, 14))
            screen.draw.filled_rect(rect, color)

    for j in range(0, 255, 16):
        color = (j, 0, 0)
        rect = Rect((300, 20+j), (160, 14))
        screen.draw.filled_rect(rect, color)

    for i in range(0, 255, 16):
        color = (i, i, 0)
        rect = Rect((20+i, 300), (14, 160))
        screen.draw.filled_rect(rect, color)
