import random
import json
import os

from pico2d import *
from math import *

import game_framework
import start_state
import title_state
import pause_state
import press_state

name = "DriftState"

font = None
car, road = None, None
roadMoveRAD = None           # 반지름
distance = None             # 거리
back, frame = None, None                 #배경
obstacle = None             #장애물
state = None                #상태
beer, box, cell, question, ufo = None, None, None, None, None
# -------------------------------------
carX, carY = 237, 130       # 차량 초기화
roadX, roadY = 280, 0       # 도로 초기화
angle_0, angle_1 = 0, 0     # 각도 초기화
PI = 3.14                   # 3.14 pi
# -------------------------------------
drift_state = 0             # 드리프트 상태 초기화
stageEnd = 0              # 스테이지 상태
# -------------------------------------
driftCount = 0              # 드리프트 횟수 카운트
mouseCount = 0              # 클릭 횟수 카운트
# -------------------------------------
life = 1
moveBack = 0
carMoveStatus, carMoveLine = 0, 0
tempT = 0
tempTime = 0
mileage = 0
# -------------------------------------
tempx, tempy = 0, 0
ufoDirX = 1
ufoDirY = 1

class Road:
    road1, road2, road3, road4, speedup = None, None, None, None, None
    def __init__(self):
        self.time = 0.0                         # 시간 초기화
        self.speed = 420                        # 처음 속도 320 - 200 = 120km
        self.down = load_image('down.png')

        if Road.road1 == None:
            Road.road1 = load_image('road1.png')

        if Road.road2 == None:
            Road.road2 = load_image('road2.png')

        if Road.road3 == None:
            Road.road3 = load_image('road3.png')

        if Road.road4 == None:
            Road.road4 = load_image('road4.png')

        if Road.speedup == None:
            Road.speedup = load_image('speedup.png')

    def update(self, frame_time):
        global roadX, roadY, driftCount, life, distance
        global tempT, mileage, tempTime

        if stageEnd == 0:
            self.time += frame_time

            if carX > 9900 - roadY and carX < 15500 - roadY:
                tempT += frame_time

            if carX > 15500 - roadY and carX < 20300 - roadY:
                tempTime += frame_time

        distance = self.speed * frame_time

        if driftCount == 0 or driftCount == 2:
            if stageEnd == 0:
                roadY += distance
        if driftCount == 1:
            roadX -= distance

        if carX < 9900 - roadY:
            mileage = road.speed / 5 * road.time

    def draw(self):
        for i in range(10):
            Road.road1.draw(roadX, 75 + (i * 150) - roadY)

        # 1번
        Road.road2.draw(roadX + 1, 1575 - roadY)
        Road.road3.draw(roadX + 181, 1575 - roadY)

        for i in range(8):
            Road.road1.draw(roadX + 181, 1755 + (i * 150) - roadY)

        # 2번
        Road.road2.draw(roadX + 182, 2901 - roadY)
        Road.road3.draw(roadX + 362, 2901 - roadY)

        for i in range(5):
            Road.road1.draw(roadX + 362, 3075 + (i * 150) - roadY)

        # 3번
        Road.road2.draw(roadX + 362, 3800 - roadY)
        Road.road3.draw(roadX + 542, 3800 - roadY)


        for i in range(5):
            Road.road1.draw(roadX + 542, 3975 + (i * 150) - roadY)

        # 4번
        Road.road2.draw(roadX + 542, 4700 - roadY)
        Road.road4.draw(roadX + 720, 4700 - roadY)
        Road.road3.draw(roadX + 800, 4700 - roadY)

        for i in range(6):
            Road.road1.draw(roadX + 800, 4875 + (i * 150) - roadY)

        # 5번
        Road.road2.draw(roadX + 800, 5700 - roadY)
        Road.road4.draw(roadX + 980, 5700 - roadY)
        Road.road4.draw(roadX + 1060, 5700 - roadY)
        Road.road3.draw(roadX + 1240, 5700 - roadY)

        for i in range(3):
            Road.road1.draw(roadX + 1239, 5880 + (i * 150) - roadY)

        # 6번
        Road.road2.draw(roadX + 1240, 6325 - roadY)
        Road.road3.draw(roadX + 1420, 6325 - roadY)
        Road.road2.draw(roadX + 1420, 6505 - roadY)
        Road.road3.draw(roadX + 1600, 6505 - roadY)

        for i in range(5):
            Road.road1.draw(roadX + 1600, 6680 + (i * 150) - roadY)

        # 7번
        Road.road2.draw(roadX + 1600, 7400 - roadY)
        Road.road3.draw(roadX + 1780, 7400 - roadY)
        Road.road2.draw(roadX + 1780, 7580 - roadY)
        Road.road4.draw(roadX + 1960, 7580 - roadY)
        Road.road4.draw(roadX + 2140, 7580 - roadY)
        Road.road3.draw(roadX + 2320, 7580 - roadY)

        for i in range(55): # feel the speed 구간
            Road.road1.draw(roadX + 2320, 7760 + (i * 150) - roadY)

        #8번
        Road.road2.draw(roadX + 2320, 15980 - roadY)
        Road.road4.draw(roadX + 2500, 15980 - roadY)
        Road.road4.draw(roadX + 2680, 15980 - roadY)
        Road.road3.draw(roadX + 2860, 15980 - roadY)
        Road.road2.draw(roadX + 2860, 16160 - roadY)
        Road.road3.draw(roadX + 3040, 16160 - roadY)
        Road.road2.draw(roadX + 3040, 16340 - roadY)
        Road.road4.draw(roadX + 3220, 16340 - roadY)
        Road.road3.draw(roadX + 3400, 16340 - roadY)

        for i in range(7):
            Road.road1.draw(roadX + 3400, 16520 + (i * 150) - roadY)

        Road.road2.draw(roadX + 3400, 17600 - roadY)
        Road.road4.draw(roadX + 3580, 17600 - roadY)
        Road.road3.draw(roadX + 3760, 17600 - roadY)
        Road.road1.draw(roadX + 3760, 17780 - roadY)

        Road.road2.draw(roadX + 3760, 17960 - roadY)

        Road.road4.draw(roadX + 3940, 17960 - roadY)
        Road.road4.draw(roadX + 4120, 17960 - roadY)
        Road.road3.draw(roadX + 4300, 17960 - roadY)

        Road.road1.draw(roadX + 4300, 18140 - roadY)
        Road.road1.draw(roadX + 4300, 18320 - roadY)
        Road.road2.draw(roadX + 4300, 18500 - roadY)
        Road.road3.draw(roadX + 4480, 18500 - roadY)


        for i in range(20):
            Road.road1.draw(roadX + 4480, 18680 + (i * 150) - roadY)

        #speedup 구간
        Road.speedup.draw(roadX, 400 - roadY)
        Road.speedup.draw(roadX + 180, 2000 - roadY)
        Road.speedup.draw(roadX + 540, 4000 - roadY)
        Road.speedup.draw(roadX + 800, 5000 - roadY)
        Road.speedup.draw(roadX + 1235, 6000 - roadY)
        Road.speedup.draw(roadX + 2320, 7900 - roadY)
        Road.speedup.draw(roadX + 2320, 9900 - roadY)
        Road.speedup.draw(roadX + 3390, 16500 - roadY)
        Road.speedup.draw(roadX + 3760, 17800 - roadY)

        #slowdonw구간
        self.down.draw(roadX + 2320, 15500 - roadY)  # slow down

class Car:
    def __init__(self):
        self.image = load_image('car.png')
        self.right = load_image('moveR.png')
        self.direct = load_image('moveD.png')
        self.explode = load_image('explode.png')
        self.right_frame, self.direct_frame, self.explode_frame = 0, 0, 0


    def update(self, frame_time):

        if carX > 400 - roadY:
            road.speed = 420
        if carX > 2000 - roadY:
            road.speed = 520
        if carX > 4000 - roadY:
            road.speed = 620
        if carX > 5000 - roadY:
            road.speed = 720
        if carX > 6000 - roadY:
            road.speed = 820
        if carX > 7900 - roadY:
            road.speed = 920

        if carX > 9900 - roadY:
            road.speed = 1400

        if carX > 15500 - roadY:
            road.speed = 720
        if carX > 16450 - roadY:
            road.speed = 820
        if carX > 17850 - roadY:
            road.speed = 920

    def draw(self):
        global drift_state, roadMoveRAD, carX, carY

        if drift_state == 0:
            if life >= 1:
                self.image.draw(carX, carY)

        elif drift_state == 1:
            self.right.clip_draw(self.right_frame * 100, 0, 100, 100, carX, carY)
            if self.right_frame < 5:
                self.right_frame += 1
            if self.right_frame > 5:
                self.right_frame = 6
            self.direct_frame = 0

        elif drift_state == 2:
            self.direct.clip_draw(self.direct_frame * 100, 0, 100, 100, carX, carY)
            if self.direct_frame < 5:
                self.direct_frame += 1
            if self.direct_frame > 5:
                self.direct_frame = 6
            self.right_frame = 0

        if life == 0:
            self.explode.clip_draw(self.explode_frame * 100, 0, 90, 100, carX, carY)
            self.explode_frame += 1
            delay(0.01)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if driftCount == 0 or driftCount == 2:
            return carX - 35, carY - 50, carX + 35, carY + 50
        if driftCount == 1:
            return carX - 50, carY - 35, carX + 50, carY + 35

class Obstacle:
    tree1, tree2, stop, cone = None, None, None, None
    def __init__(self):
        if Obstacle.cone == None:
            Obstacle.cone = load_image('cone.png')

        if Obstacle.tree1 == None:
            Obstacle.tree1 = load_image('tree1.png')

        if Obstacle.tree2 == None:
            Obstacle.tree2 = load_image('tree2.png')

        if Obstacle.stop == None:
            Obstacle.stop = load_image('stop.png')

        self.crashed = load_image('crashed.png')
        self.ac1 = load_image('ac1.png')
        self.ac2 = load_image('ac2.png')
        self.stick = load_image('stick.png')
        self.work = load_image('work.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Obstacle.cone.draw(roadX - 45, 800 - roadY)
        Obstacle.cone.draw(roadX + 40, 1400 - roadY)

        Obstacle.cone.draw(roadX + 1200, 5900 - roadY)


        Obstacle.cone.draw(roadX + 1560, 6980 - roadY)
        Obstacle.cone.draw(roadX + 1560, 7290 - roadY)

        Obstacle.cone.draw(roadX + 2360, 8200 - roadY)
        Obstacle.stop.draw(roadX + 2280, 8800 - roadY)
        Obstacle.stop.draw(roadX + 2360, 9200 - roadY)
        Obstacle.stop.draw(roadX + 2280, 9600 - roadY)

        for i in range(42):
            Obstacle.tree1.draw(roadX + 2190, 7850 + (i * 200) - roadY)
        for i in range(42):
            Obstacle.tree2.draw(roadX + 2190, 7750 + (i * 200) - roadY)

        self.crashed.draw(roadX + 100, 2500 - roadY)
        self.ac1.draw(roadX + 270, 3200 - roadY)
        self.ac2.draw(roadX + 400, 3500 - roadY)
        self.stick.draw(roadX + 500, 4200 - roadY)
        self.work.draw(roadX + 500, 4320 - roadY)
        self.stop.draw(roadX + 758, 5150 - roadY)
        self.stop.draw(roadX + 758, 5300 - roadY)

itemTime, itemDir = 1, 1
itemX, itemY = 100, 100

class Beer:
    image = None
    def __init__(self):
        if Beer.image == None:
            Beer.image = load_image('beer.png')

    def update(self, frame_time):
        global itemTime, itemDir

        itemTime -= 0.03 * itemDir
        if itemTime < 0.01:
            itemDir *= -1
        if itemTime > 1:
            itemTime = 1
            itemDir *= -1

    def draw(self):
        Beer.image.draw(800, itemY)
        Beer.image.opacify(itemTime)

    #def draw_bb(self):
    #    draw_rectangle(*self.get_bb())

    #def get_bb(self):
    #    return itemX - 25, itemY - 25, itemX + 25, itemY + 25

class Cell:
    image = None

    def __init__(self):
        if Cell.image == None:
            Cell.image = load_image('cell.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Cell.image.draw(800, 200)
        Cell.image.opacify(itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return itemX - 25, itemY - 25, itemX + 25, itemY + 25

class Box:
    image = None

    def __init__(self):
        if Box.image == None:
            Box.image = load_image('box.png')

    def update(self, frame_time):
        pass

    def draw(self):
        Box.image.draw(800, 300)
        Box.image.opacify(itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return itemX - 25, itemY - 25, itemX + 25, itemY + 25

class Question:
    image = None

    def __init__(self):
        self.image = load_image('question.png')
        self.x, self.y = 45, 500
    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(roadX - self.x, self.y - roadY)
        self.image.opacify(itemTime)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return roadX - self.x - 30, self.y - 30 - roadY, roadX - self.x + 30, self.y + 30 - roadY

class Ufo:
    image = None

    def __init__(self):
        if Ufo.image == None:
            Ufo.image = load_image('ufo.png')

        self.x, self.y = random.randint(0, 700), 300
        self.ufoRand = random.randint(1, 4)

    def update(self, frame_time):
        global tempx, tempy, ufoDirX, ufoDirY


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
        Ufo.image.draw(self.x + tempx, self.y + tempy)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return itemX - 25, itemY - 25, itemX + 25, itemY + 25






questionMark = 0


def enter():
    global car, road, font, back, obstacle, state, frame
    global beer, box, cell, question, ufo
    road = Road()
    car = Car()

    beer = Beer()
    box = Box()
    cell = Cell()
    ufo = Ufo()
    question = Question()

    obstacle = Obstacle()
    font = load_font('PWChalk.TTF', 25)
    state = load_image('state.png')

    back = load_image('back.png')
    frame = load_image('frame.png')

    game_framework.reset_time()

def exit():
    global road, car, font, question

    del(road)
    del(car)
    del(font)
    del(question)

def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    global roadMoveRAD, PI, angle_0, angle_1
    global carX, carY, roadX, roadY
    global drift_state, carMoveStatus
    global mouseCount, driftCount
    global carMoveLine, life, stageEnd

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(pause_state)

        if(life == 1):
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):        # 드리프트
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

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            life = 0
            stageEnd = 1
            drift_state = 0

def update(frame_time):
    global roadX, roadY
    global carX, carY
    global angle_0, angle_1, PI, roadMoveRAD
    global life
    global moveBack, stageEnd
    global drift_state
    global questionMark

    road.update(frame_time)
    car.update(frame_time)

    beer.update(frame_time)
    cell.update(frame_time)
    box.update(frame_time)
    ufo.update(frame_time)
    question.update(frame_time)


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

    if carMoveStatus == 1:      # 칼치기 조건
            roadX += 5

    if carMoveStatus == 2:
            roadX -= 5

    if stageEnd == 0:         # 배경 움직임
        moveBack += 3


    start_state.bgm.set_volume(start_state.volume)

    if start_state.volume > 15:
        start_state.volume -= 1


    if collide(car, question):
        print("collision")
        questionMark = 1


def draw(frame_time):
    global road, car, obstacle, beer, cell, box, ufo, question
    global moveBack
    global tempT, tempTime
    global mileage
    global frame
    global questionMark

    clear_canvas()

    for i in range(100):
        back.draw(400, 300 + (i * 600) - moveBack)

    road.draw()
    obstacle.draw()


    if(questionMark == 0):
        question.draw()
        question.draw_bb()

    if questionMark == 1:
        ufo.draw()

    car.draw()
    car.draw_bb()

    #beer.draw_bb()
    #cell.draw_bb()
    #box.draw_bb()

    #ufo.draw_bb()

    state.draw(875, 300)
    beer.draw()
    cell.draw()
    box.draw()


    frame.draw(500, 300)

    font.draw(740, 550, "SPEED", (255, 255, 255))
    font.draw(880, 550, "%3.0f" % (road.speed / 5), (255, 0, 0))
    font.draw(930, 550, "KM/S", (255, 255, 255))

    font.draw(740, 500, "TIME", (255, 255, 255))
    font.draw(890, 500, "%3.0f" % road.time, (255, 0, 0))
    font.draw(940, 500, "SEC", (255, 255, 255))

    font.draw(740, 450, "SCORE", (255, 255, 255))
    if carX > 9900 - roadY:
        font.draw(880, 450, "%3.0f" % ((road.speed / 5 * tempT) + mileage + (tempTime * road.speed)), (255, 0, 0))
    else:
        font.draw(880, 450, "%3.0f" % mileage, (255, 0, 0))
    font.draw(950, 450, "KM", (255, 255, 255))

    update_canvas()

def collide (a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


