#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=68, axle_track=121)
left_sensor = ColorSensor(Port.S3)
right_sensor = ColorSensor(Port.S4)

robot.settings(100,1000,100,1000)
robot.straight(0)
robot.drive(0,0)
robot.stop()
robot.turn(90)
robot.drive(100,25)
wait(3000)
robot.stop()