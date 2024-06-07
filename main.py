import pygame as pg
from COLORS import *

import numpy as np

def gravitation(gravity, m1, m2, distance):
        return round(gravity*((m1*m2)/distance**2))

initX = input("What is the initial velocity of your celestial body in the x axis? ")
initY = input("What is the initial velocity of your celestial body in the y axis? ")

pg.init()

screen = pg.display.set_mode((1440, 800))
pg.display.set_caption("Orbit")

screen.fill(BLACK)

pg.display.flip()

running = True

radius1 = 90
radius2 = 30

pos = (0, 0)
target = np.array([720, 400], dtype=float)
x = 0
y = 0
initX = (initX, 0)[initX == '']
initY = (initY, 0)[initY == '']

initialVelocity = np.array([int(initX), -int(initY)], dtype=float)
velocity = np.copy(initialVelocity)
clock = pg.time.Clock()


while running:
    timeDelta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_EQUALS:
                radius2 += (0, 10) [radius2<=50]
            if event.key == pg.K_MINUS:
                radius2 -= (0, 10) [radius2>=20]
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_RIGHT:
                target[0] += 10
            if event.key == pg.K_LEFT:
                target[0] -= 10
            if event.key == pg.K_UP:
                target[1] -= 10
            if event.key == pg.K_DOWN:
                target[1] += 10

        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            velocity = np.copy(initialVelocity)

        
        if pg.mouse.get_pressed()[2]:
            rightPos = pg.mouse.get_pos()
            target[0] = rightPos[0]
            target[1] = rightPos[1]

    if pos != (0, 0):
        dirVector = target - np.array((x, y))
        dirVectorNorm = dirVector / np.linalg.norm(dirVector)

        if np.linalg.norm(dirVector) > 0:
            force = gravitation(6.673*(10**-11), radius1*1e+13, radius2*1000000, np.linalg.norm(dirVector))

            acceleration = dirVectorNorm * (force/(radius2*1000000))
            velocity += acceleration

            x += velocity[0]
            y += velocity[1]

    screen.fill(BLACK)
    pg.draw.circle(screen, BLUE, (x, y), radius2)
    pg.draw.circle(screen, GREEN, (target[0], target[1]), radius1)
    pg.display.update()

    clock.tick(60)

pg.quit()