WIDTH = 480
HEIGHT = 480

BACKGROUND_COLOR = (0, 0x80, 0x80)
TEXT_COLOR = "Orange"
TEXT_LEFT = 10
TEXT_HEIGHT = 16

MESSAGES = (
        "F - fast animation",
        "S - slow animation",
        "R - reset animation",
        "",
        "I - fast animation, elastic @ in tween",
        "O - fast animation, elastic @ out tween",
        "B - fast animation, elastic @ both sides tween",
        "",
        "Esc - exit"
        )

sprite = Actor("sprite1.png")
sprite.pos = (0, 240)


def draw():
    screen.fill(BACKGROUND_COLOR)
    sprite.draw()

    y = 10
    for message in MESSAGES:
        screen.draw.text(message, (TEXT_LEFT, y), color=TEXT_COLOR)
        y += TEXT_HEIGHT


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.R:
        sprite.x = 0
    if key == keys.F:
        animate(sprite, x=WIDTH, duration=1)
    if key == keys.S:
        animate(sprite, x=WIDTH, duration=5)
    if key == keys.I:
        animate(sprite, x=WIDTH, duration=2, tween="in_elastic")
    if key == keys.O:
        animate(sprite, x=WIDTH, duration=2, tween="out_elastic")
    if key == keys.B:
        animate(sprite, x=WIDTH, duration=2, tween="in_out_elastic")
