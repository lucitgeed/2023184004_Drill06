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


#
def Follow_hand(x, y):
    print("follow")

    xnow = 800//2
    ynow = 600//2
    frame = 0

    #캐릭터 애니메이션 프레임구현(방향전환)
    if x >= xnow:
        for i in range(0, 100+1, 4):
            t = i / 100
            xline = (1 - t) * xnow + t * x
            yline = (1 - t) * ynow + t * y

            clear_canvas()
            char.clip_draw(frame * 100, 100, 100, 100, int(xline), int(yline), 100, 100)
            frame = frame + 1
            update_canvas()
            delay(0.1)

        char.clip_draw(0, 300, 100, 100, x, y)


    elif x < xnow:
        for i in range(0, 100+1, 4):
            t = i / 100
            xline = (1 - t) * xnow + t * x
            yline = (1 - t) * ynow + t * y

            clear_canvas()
            char.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', int(xline), int(yline), 100, 100)
            frame = frame + 1
            update_canvas()
            delay(0.1)

        char.clip_composite_draw(0, 300, 100, 100, 0, 'h', x, y)

    pass




#char.draw(400, 300)
while True:
    x = random.randint(25,785)
    y = random.randint(26,584)

 #   hand_to_rand(x, y)

    Follow_hand(x, y)

