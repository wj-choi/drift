import random
import os

from pico2d import *

import framework
import title_state
import pause_state

name = "MainState"

back = None
keyboard = None

def enter():
    global back, keyboard, font
    font = load_font("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\font\\overWatch.TTF")
    back = load_image("C:\\Users\\Avantgardist\\Desktop\\2DGP_2016\\image\\scene\\manual.png")


def exit():
    pass

def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)

def update(frame_time):
    pass

def draw(frame_time):
    clear_canvas()

    back.draw(500, 300)
    update_canvas()





