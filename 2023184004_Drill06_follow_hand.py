from pico2d import*
import random


open_canvas()
hand = load_image('hand_arrow.png')
char = load_image("animation_sheet.png")
back = load_image('TUK_GROUND.png')


def hand_to_rand(x, y):
    print("handrand")
    clear_canvas()

    back.draw(600,500,1200,1000)
    hand.draw(x, y)
    delay(0.5)

    update_canvas()
#


def Follow_hand(x, y):
    print("follow")
    pass





while True:
    x = random.randint(25,785)
    y = random.randint(26,584)

    hand_to_rand(x, y)

 #   Follow_hand(x, y)

