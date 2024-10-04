from pico2d import*
import random

open_canvas()
hand = load_image('hand_arrow.png')
char = load_image("animation_sheet.png")
back = load_image('TUK_GROUND.png')


def hand_to_rand():
    print("handrand")
    clear_canvas()

#    back.draw(600,500,1200,1000)
    hand.draw(random.randint(25,785), random.randint(26,584))
    delay(0.5)

    update_canvas()


    #손은 이동과정이 보이지 않음.
    #화면 내에서 랜덤위치로 이동하고
    #!!기다림!!
    pass


def Follow_hand():
    print("follow")
    pass





while True:

    hand_to_rand()

 #   Follow_hand()

