import random
import json
import os

from pico2d import *
from math import *

import game_framework
import start_state
import title_state
import pause_state

name = "DriftState"

font = None
car, road = None, None
roadMoveRAD = None           # 반지름
distance = None              # 거리
back, frame = None, None    #배경
obstacle = None             #장애물
state = None                #상태
question, ufo = None, None
volume = None
wasted = None
box, beer, cell = None, None, None
beers, boxes, cells = None, None, None
cone, stick, crashed, tree = None, None, None, None
speedup = None
road1, road2, road3, road4 = None, None, None, None
# -------------------------------------
carX, carY = 237, 130       # 차량 초기화
roadX, roadY = 280, 0       # 도로 초기화
angle_0, angle_1 = 0, 0     # 각도 초기화
PI = 3.14                   # 3.14 pi
# -------------------------------------
drift_state = 0             # 드리프트 상태 초기화
volume_state = 0
stageEnd = 0              # 스테이지 상태
# -------------------------------------
driftCount = 0              # 드리프트 횟수 카운트
mouseCount = 0              # 클릭 횟수 카운트
# -------------------------------------
life = 1
moveBack = 0
carMoveStatus, carMoveLine = 0, 0
tempT, tempTime = 0, 0
mileage = 0
# -------------------------------------
tempx, tempy = 0, 0
ufoDirX = 1
ufoDirY = 1
itemTime, itemDir = 1, 1
questionMark = 0
# --------------------------------------
wasted_state, tempRe = 0, 0
boxCount, beerCount, cellCount, tempS, ufoCount = 0, 0, 0, 1, 0
clear_state = 0
soundCount = 0
stealth_state, stealth_mode = 0, 0

# ----------------------------------------------------------------
class Road1:
    road = None

    def __init__(self):
        self.time = 0.0                         # 시간 초기화
        self.speed = 320                        # 처음 속도 320 - 200 = 120km

        if Road1.road == None:
            Road1.road = load_image('road1.png')

    def update(self, frame_time):
        pass

    def draw(self):
        for i in range(10):
            Road1.road.draw(roadX, 75 + (i * 150) - roadY)
        for i in range(8):
            Road1.road.draw(roadX + 181, 1755 + (i * 150) - roadY)
        for i in range(5):
            Road1.road.draw(roadX + 362, 3075 + (i * 150) - roadY)
        for i in range(5):
            Road1.road.draw(roadX + 542, 3975 + (i * 150) - roadY)
        for i in range(6):
            Road1.road.draw(roadX + 800, 4875 + (i * 150) - roadY)
        for i in range(3):
            Road1.road.draw(roadX + 1239, 5880 + (i * 150) - roadY)
        for i in range(5):
            Road1.road.draw(roadX + 1600, 6680 + (i * 150) - roadY)
        for i in range(55): # feel the speed 구간
            Road1.road.draw(roadX + 2320, 7760 + (i * 150) - roadY)
        for i in range(7):
            Road1.road.draw(roadX + 3400, 16520 + (i * 150) - roadY)
        for i in range(20):
            Road1.road.draw(roadX + 4480, 18680 + (i * 150) - roadY)
        Road1.road.draw(roadX + 3760, 17780 - roadY)
        Road1.road.draw(roadX + 4300, 18140 - roadY)
        Road1.road.draw(roadX + 4300, 18320 - roadY)

class Road2:
    road = None

    def __init__(self):
        if Road2.road == None:
            Road2.road = load_image('road2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        # 1번
        Road2.road.draw(roadX + 1, 1575 - roadY)

        # 2번
        Road2.road.draw(roadX + 182, 2901 - roadY)

        # 3번
        Road2.road.draw(roadX + 362, 3800 - roadY)

        # 4번
        Road2.road.draw(roadX + 542, 4700 - roadY)

        # 5번
        Road2.road.draw(roadX + 800, 5700 - roadY)
        Road2.road.draw(roadX + 1240, 6325 - roadY)
        Road2.road.draw(roadX + 1420, 6505 - roadY)

        # 7번
        Road2.road.draw(roadX + 1600, 7400 - roadY)
        Road2.road.draw(roadX + 1780, 7580 - roadY)

        #8번
        Road2.road.draw(roadX + 2320, 15980 - roadY)
        Road2.road.draw(roadX + 2860, 16160 - roadY)
        Road2.road.draw(roadX + 3040, 16340 - roadY)
        Road2.road.draw(roadX + 3400, 17600 - roadY)
        Road2.road.draw(roadX + 3760, 17960 - roadY)
        Road2.road.draw(roadX + 4300, 18500 - roadY)

class Road3:
    road = None

    def __init__(self):
        if Road3.road == None:
            Road3.road = load_image('road3.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Road3.road.draw(roadX + 181, 1575 - roadY)
        Road3.road.draw(roadX + 362, 2901 - roadY)
        Road3.road.draw(roadX + 542, 3800 - roadY)
        Road3.road.draw(roadX + 800, 4700 - roadY)
        Road3.road.draw(roadX + 1240, 5700 - roadY)
        Road3.road.draw(roadX + 1420, 6325 - roadY)
        Road3.road.draw(roadX + 1600, 6505 - roadY)
        Road3.road.draw(roadX + 1780, 7400 - roadY)
        Road3.road.draw(roadX + 2320, 7580 - roadY)
        Road3.road.draw(roadX + 2860, 15980 - roadY)
        Road3.road.draw(roadX + 3040, 16160 - roadY)
        Road3.road.draw(roadX + 3400, 16340 - roadY)
        Road3.road.draw(roadX + 3760, 17600 - roadY)
        Road3.road.draw(roadX + 4300, 17960 - roadY)
        Road3.road.draw(roadX + 4480, 18500 - roadY)

class Road4:
    road = None

    def __init__(self):
        if Road4.road == None:
            Road4.road = load_image('road4.png')

    def update(self, frame_time):
        pass

    def draw(self):
        # 4번
        Road4.road.draw(roadX + 720, 4700 - roadY)

        # 5번
        Road4.road.draw(roadX + 980, 5700 - roadY)
        Road4.road.draw(roadX + 1060, 5700 - roadY)

        # 7번
        Road4.road.draw(roadX + 1960, 7580 - roadY)
        Road4.road.draw(roadX + 2140, 7580 - roadY)

        #8번
        Road4.road.draw(roadX + 2500, 15980 - roadY)
        Road4.road.draw(roadX + 2680, 15980 - roadY)
        Road4.road.draw(roadX + 3220, 16340 - roadY)
        Road4.road.draw(roadX + 3580, 17600 - roadY)
        Road4.road.draw(roadX + 3940, 17960 - roadY)
        Road4.road.draw(roadX + 4120, 17960 - roadY)

class Speedup:
    speedup = None

    def __init__(self):
        if Speedup.speedup == None:
            Speedup.speedup = load_image('speedup.png')
            Speedup.down = load_image('down.png')

    def update(self, frame_time):
        pass

    def draw(self):

        #speedup 구간
        Speedup.speedup.draw(roadX, 400 - roadY)
        Speedup.speedup.draw(roadX + 180, 2000 - roadY)
        Speedup.speedup.draw(roadX + 540, 4000 - roadY)
        Speedup.speedup.draw(roadX + 800, 5000 - roadY)
        Speedup.speedup.draw(roadX + 1235, 6000 - roadY)
        Speedup.speedup.draw(roadX + 2320, 7900 - roadY)
        Speedup.speedup.draw(roadX + 2320, 9900 - roadY)
        Speedup.speedup.draw(roadX + 3400, 16500 - roadY)
        Speedup.speedup.draw(roadX + 3760, 17800 - roadY)

        #slowdonw구간
        Speedup.down.draw(roadX + 2320, 15500 - roadY)  # slow down

class Car:
    crashed = None
    drift = None
    engine = None

    def __init__(self):
        self.image = load_image('car.png')
        self.right = load_image('moveR.png')
        self.direct = load_image('moveD.png')
        self.explode = load_image('explode.png')
        self.right_frame, self.direct_frame, self.explode_frame = 0, 0, 0

        if Car.crashed == None:
            Car.crashed = load_wav('crash.ogg')
            Car.crashed.set_volume(50)

        if Car.drift == None:
            Car.drift = load_wav('drift.wav')
            Car.drift.set_volume(50)

        if Car.engine == None:
            Car.engine = load_wav('engine.ogg')
            Car.engine.set_volume(10)



    def update(self, frame_time):
        global questionMark, stealth_state, stealth_mode, tempS
        if carX > 400 - roadY:
            road1.speed = 400
        if carX > 2000 - roadY:
            road1.speed = 450
        if carX > 4000 - roadY:
            road1.speed = 530
        if carX > 5000 - roadY:
            road1.speed = 700
        if carX > 6000 - roadY:
            road1.speed = 800
        if carX > 7900 - roadY:
            road1.speed = 900

        if carX > 9900 - roadY:
            road1.speed = 1400

        if carX > 15500 - roadY:
            road1.speed = 700
            stealth_mode = 0
            stealth_state = 0
            tempS = 1

        if carX > 16450 - roadY:
            road1.speed = 750
        if carX > 17850 - roadY:
            road1.speed = 800


    def draw(self):
        global drift_state, roadMoveRAD, carX, carY, stageEnd, soundCount

        if drift_state == 0:
            if life >= 1:
                self.image.draw(carX, carY)
                self.image.opacify(tempS)

        elif drift_state == 1:
            self.right.clip_draw(self.right_frame * 100, 0, 100, 100, carX, carY)
            self.right.opacify(tempS)
            if self.right_frame < 5:
                self.right_frame += 1
            if self.right_frame > 5:
                self.right_frame = 6
            self.direct_frame = 0

        elif drift_state == 2:
            self.direct.clip_draw(self.direct_frame * 100, 0, 100, 100, carX, carY)
            self.direct.opacify(tempS)
            if self.direct_frame < 5:
                self.direct_frame += 1
            if self.direct_frame > 5:
                self.direct_frame = 6
            self.right_frame = 0

        if life == 0:
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, carX, carY)
            self.explode_frame += 1
            stageEnd = 1
            if soundCount < 0.5:
                Car.crashed.play()
            soundCount += 1



    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if driftCount == 0 or driftCount == 2:
            return carX - 35, carY - 50, carX + 35, carY + 50
        if driftCount == 1:
            return carX - 50, carY - 35, carX + 50, carY + 35
# ----------------------------------------------------------------
class Obstacle:
    stop = None

    def __init__(self):
        if Obstacle.stop == None:
            Obstacle.stop = load_image('stop.png')

        self.ac1 = load_image('ac1.png')
        self.ac2 = load_image('ac2.png')
        self.work = load_image('work.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Obstacle.stop.draw(roadX + 2280, 8800 - roadY)
        Obstacle.stop.draw(roadX + 2360, 9200 - roadY)
        Obstacle.stop.draw(roadX + 2280, 9600 - roadY)

        self.ac1.draw(roadX + 270, 3200 - roadY)
        self.ac2.draw(roadX + 400, 3500 - roadY)
        self.work.draw(roadX + 500, 4320 - roadY)
        Obstacle.stop.draw(roadX + 758, 5150 - roadY)
        Obstacle.stop.draw(roadX + 758, 5300 - roadY)

class Cone:
    cone = None
    def __init__(self):
        if Cone.cone == None:
            Cone.cone = load_image('cone.png')

        self.x, self.y = 100, 100

    def update(self, frame_time):
        pass


    def draw(self):
        Cone.cone.draw(roadX - 45, 800 - roadY)
        Cone.cone.draw(roadX + 40, 1400 - roadY)
        Cone.cone.draw(roadX + 1200, 5900 - roadY)
        Cone.cone.draw(roadX + 1560, 6980 - roadY)
        Cone.cone.draw(roadX + 1560, 7290 - roadY)
        Cone.cone.draw(roadX + 2360, 8200 - roadY)

class Stick:
    stick = None

    def __init__(self):
        if Stick.stick == None:
            Stick.stick = load_image('stick.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Stick.stick.draw(roadX + 3440, 16900 - roadY)
        Stick.stick.draw(roadX + 3360, 17300 - roadY)
        Stick.stick.draw(roadX + 3970, 18050 - roadY)
        Stick.stick.draw(roadX + 4440, 18800 - roadY)
        Stick.stick.draw(roadX + 4520, 19270 - roadY)

class Crashed:
    crashed = None
    def __init__(self):
        if Crashed.crashed == None:
            Crashed.crashed = load_image('crashed.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Crashed.crashed.draw(roadX + 100, 2500 - roadY)
        Crashed.crashed.draw(roadX + 3940, 18050 - roadY)

class Tree:
    tree1, tree2 = None, None
    def __init__(self):
        if Tree.tree1 == None:
            Tree.tree1 = load_image('tree1.png')

        if Tree.tree2 == None:
            Tree.tree2 = load_image('tree2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        for i in range(42):
            Tree.tree1.draw(roadX + 2190, 7850 + (i * 200) - roadY)
        for i in range(42):
            Tree.tree2.draw(roadX + 2190, 7750 + (i * 200) - roadY)
# ----------------------------------------------------------------
class Beer:
    image = None

    def __init__(self):
        if Beer.image == None:
            Beer.image = load_image('beer.png')
        self.beer = load_image('beer.png')
        self.x = random.randint(850, 850)
        self.y = random.randint(4800, 5400)

    def update(self, frame_time):
        pass

    def draw(self):
        Beer.image.draw(roadX + self.x, self.y - roadY)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return roadX + self.x - 25, self.y - roadY - 25, roadX + self.x + 25, self.y - roadY + 25

class Box:
    image = None
    def __init__(self):
        if Box.image == None:
            Box.image = load_image('box.png')
        self.box = load_image('box.png')
        self.x = random.randint(2270, 2380)
        self.y = random.randint(11000, 15400)

    def update(self, frame_time):
        pass

    def draw(self):
        Box.image.draw(roadX + self.x, self.y - roadY)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return roadX + self.x - 25, self.y - roadY - 25, roadX + self.x + 25, self.y - roadY + 25

class Cell:
    image = None
    def __init__(self):
        if Cell.image == None:
            Cell.image = load_image('cell.png')
        self.cell = load_image('cell.png')
        self.x = random.randint(220, 220)
        self.y = random.randint(2000, 2700)

    def update(self, frame_time):
        pass

    def draw(self):
        Cell.image.draw(roadX + self.x, self.y - roadY)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return roadX + self.x - 25, self.y - roadY - 25, roadX + self.x + 25, self.y - roadY + 25

class Question:
    image = None

    def __init__(self):
        self.image = load_image('question.png')
        self.x, self.y = 2360, 9600
    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(roadX + self.x, self.y - roadY)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return roadX + self.x - 30, self.y - 30 - roadY, roadX + self.x + 30, self.y + 30 - roadY

class Ufo:
    image = None

    def __init__(self):
        if Ufo.image == None:
            Ufo.image = load_image('ufo.png')

        self.x, self.y = random.randint(0, 700), 500
        self.ufoRand = random.randint(1, 4)
        self.explode = load_image('explode.png')
        self.explode_frame = 0

    def update(self, frame_time):
        global tempx, tempy, ufoDirX, ufoDirY

        if questionMark == 1:
            if self.ufoRand == 1:
                tempx -= 5 * ufoDirX
                tempy -= 5 * ufoDirY
            if self.ufoRand == 2:
                tempx += 5 * ufoDirX
                tempy += 5 * ufoDirY
            if self.ufoRand == 3:
                tempx -= 5 * ufoDirX
                tempy += 5 * ufoDirY
            if self.ufoRand == 4:
                tempx += 5 * ufoDirX
                tempy -= 5 * ufoDirY


            if self.x + tempx > 700 or self.x + tempx < 0:
                ufoDirX *= -1

            if self.y + tempy > 600 or self.y + tempy < 0:
                ufoDirY *= -1


    def draw(self):
        global questionMark, ufoCount

        if boxCount < 10:
            Ufo.image.draw(self.x + tempx, self.y + tempy)
        else:
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, self.x + tempx, self.y + tempy)
            self.explode_frame += 1
            if self.explode_frame < 16:
                ufoCount += 1
                if ufoCount > 3:
                    questionMark = 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x + tempx - 40, self.y + tempy - 40, self.x + tempx + 40, self.y + tempy + 40
# ----------------------------------------------------------------
class Volume:
    def __init__(self):
        self.volume_frame = 0
        self.image = load_image('vol.png')

    def update(self,frame_time):
        if volume_state == 1:
            if start_state.volume > 0:
                start_state.volume -= 1
        else:
            pass

    def draw(self):
        self.image.clip_draw(self.volume_frame * 60, 0, 60, 60, 50, 550)

        if start_state.volume < 20:
            self.volume_frame = 1
        if start_state.volume < 15:
            self.volume_frame = 2
        if start_state.volume < 10:
            self.volume_frame = 3
        if start_state.volume < 0:
            self.volume_frame = 4

class Wasted:
    def __init__(self):
        self.x, self.y = 400, 400
        self.image = load_image('wasted.png')
    def update(self, frame_time):
        pass
    def draw(self):
        global wasted_state

        if life == 0:
            self.image.draw(self.x, self.y)
            wasted_state = 1
# ----------------------------------------------------------------

def enter():
    global car, road, font, back, obstacle, state, frame
    global beer, cell, question, ufo, volume, wasted
    global cone, stick, crashed, tree
    global boxes, beers, cells
    global speedup, road1, road2, road3, road4

    road4 = Road4()
    road1 = Road1()
    road2 = Road2()
    road3 = Road3()

    car = Car()
    speedup = Speedup()

    beers = [Beer() for i in range(5)]
    boxes = [Box() for i in range(10)]
    cells = [Cell() for i in range(5)]

    cone = Cone()
    stick = Stick()
    crashed = Crashed()
    tree = Tree()

    ufo = Ufo()
    question = Question()

    volume = Volume()
    wasted = Wasted()

    obstacle = Obstacle()
    font = load_font('PWChalk.TTF', 25)
    state = load_image('state.png')

    back = load_image('back.png')
    frame = load_image('frame.png')

    game_framework.reset_time()

def createWorld():
    global carX, carY, roadX, roadY, drift_state, mouseCount, driftCount, stageEnd, life, moveBack
    global tempT, tempTime, mileage, tempx, tempy, questionMark, carMoveStatus, carMoveLine, wasted_state, tempRe
    global boxCount, clear_state, soundCount, cellCount, beerCount, beers, boxes, cells, ufoCount, stealth_state

    # -------------------------------------
    carX, carY = 237, 130  # 차량 초기화
    roadX, roadY = 280, 0  # 도로 초기화
    # -------------------------------------
    drift_state = 0  # 드리프트 상태 초기화
    stageEnd = 0  # 스테이지 상태
    # -------------------------------------
    driftCount = 0  # 드리프트 횟수 카운트
    mouseCount = 0  # 클릭 횟수 카운트
    # -------------------------------------
    life = 1
    moveBack = 0
    carMoveStatus, carMoveLine = 0, 0
    tempT, tempTime = 0, 0
    mileage = 0
    # -------------------------------------
    tempx, tempy = 0, 0
    questionMark = 0
    # --------------------------------------
    wasted_state = 0
    tempRe = 0
    car.explode_frame = 0
    ufo.explode_frame = 0
    # ---------------------------------------
    boxCount = 0
    clear_state = 0
    soundCount = 0
    cellCount, boxCount, beerCount = 0, 0, 0
    road1.time = 0
    tempTime = 0
    tempT = 0
    road1.speed = 320
    stealth_state = 0
    ufoCount = 0
    beers = [Beer() for i in range(5)]
    boxes = [Box() for i in range(10)]
    cells = [Cell() for i in range(5)]

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global roadMoveRAD, PI, angle_0, angle_1
    global carX, carY, roadX, roadY
    global drift_state, volume_state, carMoveStatus
    global mouseCount, driftCount
    global carMoveLine, life, stageEnd, tempRe
    global tempS, stealth_state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(pause_state)

        if life == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):        # 드리프트
                Car.drift.play()
                if mouseCount % 2 == 1:
                    drift_state, driftCount = 1, 1
                    roadMoveRAD = -5
                    angle_0 = 90

                elif mouseCount % 2 == 0:
                    drift_state, driftCount = 2, 2
                    roadMoveRAD = 6
                    angle_1 = 270

            if drift_state == 2 or drift_state == 0:
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):                            # 칼치기
                        carMoveStatus = 1

                elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
                    carMoveStatus = 0

                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):                            # 칼치기
                    carMoveStatus = 2
                elif (event.type, event.key) == (SDL_KEYUP, SDLK_x):
                    carMoveStatus = 0


            if (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
                mouseCount += 1

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
                road.speed += 100

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                road.speed -= 100

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_v):
            volume_state = 1


        if (event.type, event.key) == (SDL_KEYUP, SDLK_v):
            volume_state = 0

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            life = 0
            stageEnd = 1
            drift_state = 0


        if wasted_state == 1:
            if event.type == SDL_MOUSEMOTION:
                if event.x > 310 and event.x < 495 and event.y > 228 and event.y < 271:
                    tempRe = 1

        if clear_state == 1:
            if event.type == SDL_MOUSEMOTION:
                if event.x > 310 and event.x < 495 and event.y > 228 and event.y < 271:
                    tempRe = 1

        if tempRe == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                    createWorld()


        if stealth_mode == 1:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT):
                stealth_state = 1

def update(frame_time):
    global roadX, roadY
    global carX, carY
    global angle_0, angle_1, PI, roadMoveRAD
    global life
    global moveBack, stageEnd
    global drift_state
    global questionMark
    global boxCount, beerCount, cellCount
    global clear_state
    global cell, beer, box
    global roadX, roadY, driftCount, life, distance
    global tempT, mileage, tempTime, stealth_mode, tempS, stealth_state

    if cellCount == 5:
        stealth_mode = 1

    if stealth_state == 1:
        cellCount = 0
        if tempS > 0.5:
            tempS -= 0.1

    start_state.bgm.set_volume(start_state.volume)
    if start_state.volume > 20:
        start_state.volume -= 1
    car.update(frame_time)
    ufo.update(frame_time)
    volume.update(frame_time)
    wasted.update(frame_time)

    if driftCount == 1:
        roadX += roadMoveRAD * cos(-angle_0 * (PI / 180))
        roadY += roadMoveRAD * sin(-angle_0 * (PI / 180))
        angle_0 += 10

        if angle_0 > 180:
            roadMoveRAD = 0

    if driftCount == 2:
        roadX += roadMoveRAD * sin(angle_1 * (PI / 180))
        roadY += roadMoveRAD * cos(angle_1 * (PI / 180))
        angle_1 += 10

        if angle_1 > 360:
            roadMoveRAD = 0

    if roadY > 20300:           # 종료 조건
        carY += distance
        stageEnd = 1
        clear_state = 1

    if stageEnd == 0:
        if carMoveStatus == 1:      # 칼치기 조건
            roadX += 5
        if carMoveStatus == 2:
            roadX -= 5
        moveBack += 3

    if collide(car, question):
        questionMark = 1

    for box in boxes:
        if collide(car, box):
            boxes.remove(box)
            boxCount += 1

    for beer in beers:
        if collide(car, beer):
            beers.remove(beer)
            beerCount += 1

    for cell in cells:
        if collide(car, cell):
            cells.remove(cell)
            cellCount += 1

    if collide(car, ufo):
        if stealth_mode == 0:
            life = 0
            drift_state = 3


    if stageEnd == 0:
        road1.time += frame_time

        if carX > 9900 - roadY and carX < 15500 - roadY:
            tempT += frame_time

        if carX > 15500 - roadY and carX < 20300 - roadY:
            tempTime += frame_time

        distance = road1.speed * frame_time

        if driftCount == 0 or driftCount == 2:
            roadY += distance
        elif driftCount == 1:
            roadX -= distance

        if carX < 9900 - roadY:
            mileage = road1.speed / 5 * road1.time

        ufo.x, ufo.y = 0, 0

def draw(frame_time):
    global moveBack
    global tempT, tempTime
    global mileage
    global frame
    global questionMark
    global stageEnd
    global box, cell, beer
    clear = load_image('clear.png')

    clear_canvas()

    for i in range(100):
        back.draw(400, 300 + (i * 600) - moveBack)

    # --------------------------------------------
    road1.draw()
    road2.draw()
    road4.draw()
    road3.draw()

    speedup.draw()
    car.draw()
    car.draw_bb()
    # --------------------------------------------
    obstacle.draw()
    cone.draw()
    stick.draw()
    crashed.draw()
    tree.draw()
    # --------------------------------------------
    for box in boxes:
        box.draw()
        box.draw_bb()

    for beer in beers:
        beer.draw()
        beer.draw_bb()

    for cell in cells:
        cell.draw()
        cell.draw_bb()

    if questionMark == 0:
        question.draw()
        question.draw_bb()

    if questionMark == 1:
        ufo.draw()
        ufo.draw_bb()

    # --------------------------------------------
    volume.draw()
    wasted.draw()
    state.draw(875, 300)

    if clear_state == 1:
        clear.draw(400, 380)

    frame.draw(500, 300)

    font.draw(740, 550, "SPEED", (255, 255, 255))
    font.draw(870, 550, "%3.0f" % (road1.speed / 5), (255, 0, 0))
    font.draw(920, 550, "KM/H", (255, 255, 255))

    font.draw(740, 500, "TIME", (255, 255, 255))
    font.draw(880, 500, "%3.0f" % road1.time, (255, 0, 0))
    font.draw(940, 500, "HR", (255, 255, 255))

    font.draw(740, 450, "SCORE", (255, 255, 255))
    if carX > 9900 - roadY:
        font.draw(860, 450, "%3.0f" % ((road1.speed / 5 * tempT) + mileage + (tempTime * road1.speed)), (255, 0, 0))
    else:
        font.draw(860, 450, "%3.0f" % mileage, (255, 0, 0))
    font.draw(940, 450, "KM", (255, 255, 255))


    font.draw(830, 255, " X %d" % boxCount, (0,255,255))
    font.draw(830, 175, " X %d" % cellCount, (0, 255, 255))
    font.draw(830, 95, " X %d" % beerCount, (0, 255, 255))

    update_canvas()

def collide (a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True
