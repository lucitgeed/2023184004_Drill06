from pico2d import*

open_canvas()
hand = load_image('hand_arrow')
char = load_image("animation_sheet")
back = load_image('TUK_GROUND')


def hand_to_rand():
    print("handrand")
    clear_canvas()
    back.draw(0,0)

    char.draw(400, 300)
    delay(0.1)


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

