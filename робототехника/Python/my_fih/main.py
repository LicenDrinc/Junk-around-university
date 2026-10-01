#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
x=ev3.screen.width/2
y=ev3.screen.height/2
ev3.speaker.set_volume(100)

def picture(x,y):
    ev3.screen.draw_box(x,y,x+10,y+10)
    ev3.screen.draw_line(x,y,x+5,y-5)
    ev3.screen.draw_line(x+5,y-5,x+10,y)

while(True):
    btns=ev3.buttons.pressed()
    while (btns==[]):
        btns=ev3.buttons.pressed()
    print(btns)
    ev3.speaker.beep()
    if (Button.RIGHT in btns):
        x+=5
    if (Button.LEFT in btns):
        x-=5
    if (Button.DOWN in btns):
        y+=5
    if (Button.UP in btns):
        y-=5
    ev3.screen.clear()
    picture(x,y)
    wait(10)
    