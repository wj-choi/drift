import framework
from pico2d import *

import title_state

name = "PressState"
image = None
back = None
key = None
title = None

logo_time = 0.0
enterLobby = 0

def enter():
    global image, back, title, key

    image = load_image("select_image.png")
    back = load_image("background_image.png")
    key = load_image("key.png")
    title = load_image("game_title.png")

def exit():
    global image
    del(image)


imageTime = 0
keyTime = 1
dir = 1

def update(frame_time):
    global imageTime, keyTime, dir

    if imageTime < 1:
        imageTime += 0.0025

    keyTime -= 0.005 * dir

    if keyTime > 1:
        keyTime = 1
        dir *= -1

    if keyTime < 0.001:
        dir *= -1



def draw(frame_time):
    global image, back, enterLobby
    clear_canvas()

    back.draw(500, 300)
    if(imageTime > 0.001):
        image.draw(500, 300)
    image.opacify(imageTime)

    if(imageTime > 0.99):
        enterLobby = 1
        key.draw(500, 400)
        title.draw(520, 500)
        key.opacify(keyTime)

    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            if event.type == SDL_KEYDOWN and event.key != SDLK_ESCAPE and enterLobby == 1:
                framework.push_state(title_state)

def pause(): pass


def resume(): pass




