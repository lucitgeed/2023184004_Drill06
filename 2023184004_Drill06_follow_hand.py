from pico2d import*
import random


open_canvas()
hand = load_image('hand_arrow.png')
char = load_image('animation_sheet.png')
back = load_image('TUK_GROUND.png')


def hand_to_rand(x, y):
#    print("handrand")
    clear_canvas()

    back.draw(600,500,1200,1000)
    hand.draw(x, y)
    delay(0.5)

    update_canvas()
#


def Follow_hand():

 #   back.draw(600, 500, 1200, 1000)
    print("follow")
    char.clip_draw(0, 0, 100, 100, 800//2, 600//2)

    #캐릭터(정자세)를 먼저 그리고

    #캐릭터 애니메이션 프레임구현(방향전환)
    #now는 현재 위치


    #화살표를 찾아서 따라감
    #직선으로
    #따라가는 과정이 보임
    update_canvas()

    pass




#char.draw(400, 300)
while True:
#    x = random.randint(25,785)
#    y = random.randint(26,584)

 #   hand_to_rand(x, y)

    Follow_hand()

