#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.B, positive_direction = Direction.COUNTERCLOCKWISE); rm = Motor(Port.C)
r = DriveBase(lm, rm, 55.1, 200)
ls = ColorSensor(Port.S2); rs = ColorSensor(Port.S3)

inte = errold = pr = ls1 = rs1 = diff = 0

def pid_drive(s = 200, p = 0.3, i = 0.00005, d = 5):
    global inte, errold, pr, diff, ls1, rs1
    err = ls1 - rs1; pr = err * p; inte = inte + err * i
    diff = (err - errold) * d; errold = err; r.drive(s, round(pr + inte + diff))

def pid_reset(): global inte, errold; inte = errold = 0; r.reset()


def rstop(): r.stop(); lm.dc(0); rm.dc(0); lm.brake(); rm.brake()

def pid_to_motor(s = 200, p = 0.3, i = 0.00005, d = 5, di = 100):
    global ls1, rs1; pid_reset()
    while r.distance()<di: ls1 = ls.reflection(); rs1 = rs.reflection(); pid_drive(s, p, i, d)

def pid_to_X(s = 200, p = 0.3, i = 0.00005, d = 5, sl = 30):
    global ls1, rs1; pid_reset(); ls1 = 50; rs1 = 50
    while ls1 + rs1 > sl: ls1 = ls.reflection(); rs1 = rs.reflection(); pid_drive(s, p, i, d)
    
def pid_left_in_to_motor(s = 200, p = 0.3, i = 0.00005, d = 5, di = 100, bw = 50):
    global ls1, rs1; pid_reset(); rs1 = bw
    while r.distance() < di: ls1 = ls.reflection(); pid_drive(s, p, i, d)

def pid_left_in_to_rightX(s = 200, p = 0.3, i = 0.00005, d = 5, sl = 25, bw = 50):
    global ls1, rs1; pid_reset(); rs1 = bw
    while rs.reflection() > sl: ls1 = ls.reflection(); pid_drive(s, p, i, d)

def pid_right_in_to_motor(s = 200, p = 0.3, i = 0.00005, d = 5, di = 100, bw = 50):
    global ls1, rs1; pid_reset(); ls1 = bw
    while r.distance() < di: rs1 = rs.reflection(); pid_drive(s, p, i, d)

def pid_right_in_to_leftX(s = 200, p = 0.3, i = 0.00005, d = 5, sl = 25, bw = 50):
    global ls1, rs1; pid_reset(); ls1 = bw
    while ls.reflection() > sl: rs1 = rs.reflection(); pid_drive(s, p, i, d)

ev3.speaker.beep(); wait(100)

while ev3.buttons.pressed()==[]: pass

# pid_to_motor(s = 1000, di = 1000)
# pid_to_X(s = 1000)
# pid_left_in_to_motor(s = 1000, di = 1000)
# pid_left_in_to_rightX(s = 1000)
# pid_right_in_to_motor(s = 1000, di = 1000)
# pid_right_in_to_leftX(s = 1000)

# rstop()

# L --------------------------------------------------------------------------------------------

# L3 in mainL3

# L1 1 =================================

r.settings(1000, 500, 1000, 500)

# r.turn(360)
# while ev3.buttons.pressed()==[]: pass
# r.turn(-360)
# while ev3.buttons.pressed()==[]: pass

if (Button.UP in ev3.buttons.pressed()):
    r.turn(15)
    r.straight(50)
    r.drive(100, 0)
    while ls.reflection() > 20: pass
    r.turn(-15)
    pid_left_in_to_motor(s = 300, di = 200)
    pid_left_in_to_motor(s = 1000, di = 600)
    pid_left_in_to_rightX(s = 1000)
    rstop()
    r.straight(40); r.turn(90)
    pid_to_motor(s = 300, di = 70)
    rstop()
    r.turn(195)
    # 1
    r.straight(40); r.turn(95)
    pid_left_in_to_motor(s = 300, di = 200)
    pid_left_in_to_rightX(s = 1000)
    rstop()
    r.straight(50); r.turn(95)
    pid_to_motor(s = 1000, di = 800)
    pid_to_X(s = 1000)
    rstop()
    r.straight(40); r.turn(95)
    pid_left_in_to_motor(s = 300, di = 200)
    pid_left_in_to_rightX(s = 1000)
    rstop()
    r.straight(50); r.turn(95)
    pid_to_motor(s = 300, di = 70)
    rstop()
    r.turn(195)
    # 13
    r.straight(50); r.turn(-85)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_motor(s = 1000, di = 400)
    pid_right_in_to_leftX(s = 1000)
    rstop()
    r.turn(195)
    # 131
    pid_left_in_to_motor(s = 300, di = 300)
    pid_left_in_to_motor(s = 1000, di = 1500)
    pid_left_in_to_rightX(s = 1000)
    rstop()
    r.straight(50); r.turn(95)
    pid_to_motor(s = 300, di = 200)
    pid_to_X(s = 1000)
    rstop()
    r.straight(180)
    r.turn(90)
else:
    r.turn(-15)
    r.straight(50)
    r.drive(100, 0)
    while rs.reflection() > 20: pass
    r.turn(15)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_leftX(s = 1000)
    rstop()
    r.straight(40); r.turn(-85)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_motor(s = 1000, di = 1200)
    pid_right_in_to_motor(s = 300, di = 300)
    pid_right_in_to_leftX(s = 500)
    rstop()
    r.turn(190)
    # 1
    pid_left_in_to_motor(s = 300, di = 600)
    pid_left_in_to_rightX(s = 1000)
    rstop()
    r.straight(40); r.turn(90)
    pid_to_motor(s = 300, di = 70)
    rstop()
    r.turn(190)
    # 13
    r.straight(40); r.turn(-85)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_leftX(s = 1000)
    rstop()
    r.straight(40); r.turn(-85)
    pid_to_motor(s = 1000, di = 800)
    pid_to_X(s = 1000)
    rstop()
    r.straight(40); r.turn(-85)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_leftX(s = 1000)
    rstop()
    r.straight(40); r.turn(-85)
    pid_to_motor(s = 300, di = 70)
    rstop()
    r.turn(190)
    # 131
    r.straight(40); r.turn(-85)
    pid_right_in_to_motor(s = 300, di = 200)
    pid_right_in_to_motor(s = 1000, di = 760)
    pid_to_X(s = 1000)
    rstop()
    r.straight(180)
    r.turn(90)

# L9 in main