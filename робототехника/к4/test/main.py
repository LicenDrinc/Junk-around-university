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
r = DriveBase(lm, rm, 55.1, 192)
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


# 1 --------------------------------------------------------------------------------------------

# x = ev3.screen.width / 2; y = ev3.screen.height / 2; ev3.speaker.set_volume(10)

# def picture(x, y):
#     ev3.screen.draw_box(x, y, x + 10, y + 10)
#     ev3.screen.draw_line(x, y, x + 5, y - 5)
#     ev3.screen.draw_line(x + 5, y - 5, x + 10, y)

# while (True):
#     b = ev3.buttons.pressed(); while (b == []): b = ev3.buttons.pressed()
#     x += (1 if (Button.RIGHT in b) else 0) - (1 if (Button.LEFT in b) else 0)
#     y += (1 if (Button.UP in b) else 0) - (1 if (Button.DOWN in b) else 0)
#     print(b); ev3.screen.clear(); picture(x, y); wait(10)


# 2 --------------------------------------------------------------------------------------------

# lmotor.run_target(1000, 0); rmotor.run_target(1000, 0); lmotor.stop(); rmotor.stop(); wait(100)

# for i in range(0, 30): lmotor.run_target(1000, i * (-1 if (i % 2 == 0) else 1)); rmotor.run_target(1000, lmotor.angle())

# while (True): rmotor.run_target(1000, -lmotor.angle()); wait(500)


# L --------------------------------------------------------------------------------------------

# L3 1 =================================

# uss = UltrasonicSensor(Port.S1)
# i = 5.0; ev3.speaker.set_volume(i); io = i
# while (True):
#     if (Button.UP in ev3.buttons.pressed()): i += 1
#     if (Button.DOWN in ev3.buttons.pressed()): i -= 1
#     if (i != io): ev3.speaker.set_volume(i); io = i
#     d = uss.distance(); print(d,' ',i)
#     ev3.speaker.beep(d); wait(150)

# L3 2 =================================

# db = DriveBase(lmotor, rmotor, 55.1, 192)
# db.settings(1000, 500, 1000, 500)

# while(True):
#     if (Button.DOWN in ev3.buttons.pressed()):
#         wait(1000); ev3.speaker.beep()
#         while(True):
#             if (Button.UP in ev3.buttons.pressed()): db.straight(1000); break
#             elif (Button.LEFT in ev3.buttons.pressed()): db.turn(360); break
#             elif (Button.RIGHT in ev3.buttons.pressed()): db.turn(-360); break
#         break
#     elif (Button.UP in ev3.buttons.pressed()):
#         wait(1000)
#         for i in range(4): db.straight(100); db.turn(90)
#         break
#     elif (Button.LEFT in ev3.buttons.pressed()):
#         wait(1000)
#         for i in range(3): db.straight(100); db.turn(120)
#         break
#     elif (Button.RIGHT in ev3.buttons.pressed()):
#         wait(1000)
#         for i in range(6): db.straight(100); db.turn(60)
#         break

# wait(100)

# L3 3 =================================

# db = DriveBase(lmotor, rmotor, 55.1, 192)

# while(not (Button.CENTER in ev3.buttons.pressed())): wait(100)
# ev3.speaker.beep(); wait(1000); s = []; r = []
# while(not (Button.CENTER in ev3.buttons.pressed())):
#     wait(50); d = db.state(); s += [d[1]]; r += [d[3]]
# ev3.speaker.beep(); wait(3000); ev3.speaker.beep()

# for i in range(len(s)): db.drive(s[i], r[i]); wait(50)
# db.stop()

# L3 4 =================================

# import random; ma = 1000; mi = 0; d = 0

# ev3.speaker.set_volume(100)
# ev3.speaker.set_speech_options('ru', 'm4', 1, 25)
# for i in range(10):
#     if (mi == ma): break
#     z = int((ma - mi) / 2 + mi); k = random.randint(0, 1); o = random.randint(0, 1)
#     if (k == 0 and z == ma): k == 1
#     if (k == 1 and z == mi): k == 0
#     l = "больше " if k == 0 else "меньше "; l += "или ровно " if o == 0 else ""
#     g = ""; ev3.screen.clear()
#     l1 = ">" if k == 0 else "<"; l1 += "=" if o == 0 else ""
#     ev3.screen.print("n " + l1 + " " + repr(z) + "\ni = " + repr(i) + 
#                      "\n" + repr(mi) + " <= n <= " + repr(ma))
#     ev3.speaker.say("хм " + l + repr(z)); ev3.speaker.beep()
#     while (True):
#         if (Button.UP in ev3.buttons.pressed()):
#             if (k == 0): mi = z if o == 0 else z + 1
#             else: ma = z if o == 0 else z - 1
#             break
#         elif (Button.DOWN in ev3.buttons.pressed()):
#             if (k == 0): ma = z - 1 if o == 0 else z
#             else: mi = z + 1 if o == 0 elsez 
#             break
#         wait(1)

# if (ma == mi): d = 1; z = ma
# else: z = random.randint(mi, ma)
# ev3.screen.clear()
# ev3.screen.print("n = " + repr(z) + "\n" + repr(mi) + " <= n <= " + repr(ma))
# ev3.speaker.say("хм это " + repr(z) if (ma != mi) else "это " + repr(z))
# if (ma != mi): ev3.speaker.beep()
# while (ma != mi):
#     if (Button.UP in ev3.buttons.pressed()): d = 1; break
#     elif (Button.DOWN in ev3.buttons.pressed()): break

# ev3.speaker.say("Победа" if (d == 1) else "Что это")

# L3 5 =================================







