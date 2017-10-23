# coding=utf-8
# 1
from tkinter import *
from Character import *

HEIGHT = 700
WIDTH = 1000
window = Tk()
window.title("Game")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
c.pack()

# 2
c.create_text(950, 690, text='By Ilya Ermakov', fill='white')
ball = c.create_oval(40, 40, 80, 80, fill='#FFDAB9')
# Вот тут идет создание твоего персонажа.
# Почему бы взаимодействие с ним не вынести в отдельный класс?
character = Character(WIDTH / 2, HEIGHT / 2)
arm1 = c.create_line(35, 100, 20, 140)
arm2 = c.create_line(80, 100, 100, 140)
pykav1 = c.create_polygon(40, 80, 40, 110, 20, 100, fill='white')
pykav2 = c.create_polygon(80, 80, 80, 110, 100, 100, fill='white')
leg1 = c.create_line(47, 180, 47, 220)
leg2 = c.create_line(72, 180, 72, 220)
botinok1 = c.create_rectangle(35, 220, 47, 225, fill='grey')
botinok2 = c.create_rectangle(72, 220, 85, 225, fill='grey')
shorti1 = c.create_rectangle(55, 120, 65, 160, fill='#1E90FF', outline='#1E90FF')
shorti2 = c.create_rectangle(40, 140, 55, 180, fill='#1E90FF', outline='#1E90FF')
shorti3 = c.create_rectangle(65, 140, 80, 180, fill='#1E90FF', outline='#1E90FF')
body = c.create_rectangle(40, 80, 80, 140, fill='white', outline='white')
BODY_R = 60
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2


# 3
def unior_guy_control(event):
    key = event.keysym
    if key == "Up":
        # А тут все заменить простым,
        # Смещая человечка на 0 по x и на -5 по y
        character.move_on(0, -5)
        # Вместо вот этого всего
        # и так при каждом из нажатий
        c.move(ball, 0, -5)
        c.move(arm1, 0, -5)
        c.move(arm2, 0, -5)
        c.move(pykav1, 0, -5)
        c.move(pykav2, 0, -5)
        c.move(leg1, 0, -5)
        c.move(leg2, 0, -5)
        c.move(botinok1, 0, -5)
        c.move(botinok2, 0, -5)
        c.move(shorti1, 0, -5)
        c.move(shorti2, 0, -5)
        c.move(shorti3, 0, -5)
        c.move(body, 0, -5)

    elif key == "Down":
        c.move(ball, 0, 5)
        c.move(arm1, 0, 5)
        c.move(arm2, 0, 5)
        c.move(pykav1, 0, 5)
        c.move(pykav2, 0, 5)
        c.move(leg1, 0, 5)
        c.move(leg2, 0, 5)
        c.move(botinok1, 0, 5)
        c.move(botinok2, 0, 5)
        c.move(shorti1, 0, 5)
        c.move(shorti2, 0, 5)
        c.move(shorti3, 0, 5)
        c.move(body, 0, 5)

    elif key == "Left":
        c.move(ball, -5, 0)
        c.move(arm1, -5, 0)
        c.move(arm2, -5, 0)
        c.move(pykav1, -5, 0)
        c.move(pykav2, -5, 0)
        c.move(leg1, -5, 0)
        c.move(leg2, -5, 0)
        c.move(botinok1, -5, 0)
        c.move(botinok2, -5, 0)
        c.move(shorti1, -5, 0)
        c.move(shorti2, -5, 0)
        c.move(shorti3, -5, 0)
        c.move(body, -5, 0)

    elif key == "Right":
        c.move(ball, 5, 0)
        c.move(arm1, 5, 0)
        c.move(arm2, 5, 0)
        c.move(pykav1, 5, 0)
        c.move(pykav2, 5, 0)
        c.move(leg1, 5, 0)
        c.move(leg2, 5, 0)
        c.move(botinok1, 5, 0)
        c.move(botinok2, 5, 0)
        c.move(shorti1, 5, 0)
        c.move(shorti2, 5, 0)
        c.move(shorti3, 5, 0)
        c.move(body, 5, 0)


c.bind_all('<Key>', unior_guy_control)

# 4
from random import randint

coin_id = list()
coin_r = list()
coin_speed = list()
MIN_COIN_R = 10
MAX_COIN_R = 30
MAX_COIN_SPD = 10
GAP = 100


def create_coin():
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    r = 15
    id1 = c.create_oval(x - r, y - r, x + r, y + r, fill='yellow')
    coin_id.append(id1)
    coin_r.append(r)
    coin_speed.append(10)


# 5
def move_coin():
    for i in range(len(coin_id)):
        c.move(coin_id[i], -coin_speed[i], 0)


# 7
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


# 8
def del_coin(i):
    del coin_r[i]
    del coin_speed[i]
    c.delete(coin_id[i])
    del coin_id[i]


# 9
def clean_up_coin():
    for i in range(len(coin_id) - 1, -1, -1):
        x, y = get_coords(coin_id[i])
        if x < -100:
            del_coin(i)


# 11
from math import sqrt


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 12
def collision():
    points = 0
    for coin in range(len(coin_id) - 1, -1, -1):
        if distance(body, coin_id[coin]) < (BODY_R + coin_r[coin]):
            points += (coin_r[coin] + coin_speed[coin])
            del_coin(coin)
    return points


# 14
c.create_text(50, 30, text='Time', fill='white')
c.create_text(150, 30, text='Score', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')


def show_score(score):
    c.itemconfig(score_text, text=str(score))


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


# 6 - 10 - 13
from time import sleep, time

COIN_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT
while time() < end:
    if randint(1, COIN_CHANCE) == 1:
        create_coin()
    move_coin()
    clean_up_coin()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

# 17
c.create_text(MID_X, MID_Y, \
              text='Game Over', fill='white', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 30, \
              text='Score: ' + str(score), fill='white')
c.create_text(MID_X, MID_Y + 45, \
              text='Bonus time: ' + str(bonus * TIME_LIMIT), fill='white')
