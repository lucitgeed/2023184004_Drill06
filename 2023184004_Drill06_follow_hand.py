from pico2d import*
import random


open_canvas()
hand = load_image('hand_arrow.png')
char = load_image('animation_sheet.png')
back = load_image('TUK_GROUND.png')


#
def Draw_hand_back(x,y):
    clear_canvas()
    back.draw(600, 500, 1200, 1000)
    hand.draw(x, y)
#

#
def Follow_hand(x, y, lastx, lasty):

    frame = 0
    for i in range(0, 100+1, 2):
        t = i / 100
        xline = (1 - t) * lastx + t * x
        yline = (1 - t) * lasty + t * y

        Draw_hand_back(x, y)

        if x >= lastx:
            char.clip_draw(frame * 100, 100, 100, 100, int(xline), int(yline), 100, 100)
        elif x < lastx:
            char.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', int(xline), int(yline), 100, 100)
        frame = (frame + 1) % 8
        delay(0.05)

        update_canvas()
#


xlast = 800 // 2
ylast = 600 // 2

delay(0.1)

while True:
    x = random.randint(25,785)
    y = random.randint(26,584)

    Follow_hand(x, y, xlast, ylast)

    Draw_hand_back(x, y)
    if x>= xlast:
        char.clip_draw(0,300, 100,100, x,y, 100,100)
    elif x < xlast:
        char.clip_draw(0,200, 100,100, x,y, 100,100)
    update_canvas()
    delay(0.6)

    xlast = x
    ylast = y

