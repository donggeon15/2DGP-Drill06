from pico2d import *

import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            return
    pass

def Random_Mouse():
    global mouse_x, mouse_y
    global mouse_px, mouse_py
    mouse_px = mouse_x
    mouse_py = mouse_y
    mouse_x = random.randint(0,TUK_WIDTH)
    mouse_y = random.randint(0,TUK_HEIGHT)
    pass

def Move_character():
    global mouse_x, mouse_y
    global mouse_px, mouse_py
    global x, y, frame
    for i in range(0, 100):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand_arrow.draw(mouse_x, mouse_y)
        t = i / 100
        x = (((1 - t) * mouse_px) + (t * mouse_x))
        y = (((1 - t) * mouse_py) + (t * mouse_y))
        if mouse_x < mouse_px:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        elif mouse_x > mouse_px:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        handle_events()
        update_canvas()

    delay(0.1)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mouse_px, mouse_py = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0


while running:
    Random_Mouse()
    Move_character()


close_canvas()



