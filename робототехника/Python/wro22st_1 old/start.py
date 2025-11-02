#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import _thread

ev3 = EV3Brick()

left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
UD_motor = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE)
claw_motor = Motor(Port.D,positive_direction=Direction.COUNTERCLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=181.5)

left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
left_p_sensor = ColorSensor(Port.S1)
right_p_sensor = ColorSensor(Port.S4)


def rstop(wait_ms=35):
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    wait(wait_ms)

def pid_to_X(speed=65, p=0.2, i=0.0002, d=2, stoplevel=50):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = right_sensor.reflection()
    while ls+rs > stoplevel:
        ls = left_sensor.reflection()
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs 
        robot.drive(speed,round(prop + integral + diff))

def to_white2(speed=40, stoplevel=70):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while left_sensor.reflection()+right_sensor.reflection()<stoplevel: pass

def pid_to_motor(speed=70, p=0.2, i=0.0002, d=2, distance=100):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = right_sensor.reflection()
    right_motor.reset_angle(0)
    while right_motor.angle()<distance:
        ls = left_sensor.reflection()
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop + integral + diff))

def turn_left(speed=45, distance=35, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    robot.drive(0,-speed*3)
    while left_sensor.reflection()<bw+10: pass
    while left_sensor.reflection()>bw-10: pass
    while left_sensor.reflection()<bw+10: pass
    robot.stop()

def turn_right(speed=45, distance=35, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    robot.drive(0,speed*3)
    while right_sensor.reflection()<bw+10: pass
    while right_sensor.reflection()>bw-10: pass
    while right_sensor.reflection()<bw+10: pass
    robot.stop()

def pid_right_in_to_motor(speed=50, p=0.2, i=0.0002, d=2, distance=100, bw=60):
    integral = errold = 0
    ls = bw
    rs = right_sensor.reflection()
    right_motor.reset_angle(0)
    while right_motor.angle()<distance:
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop + integral + diff))

def pid_left_in_to_motor(speed=50, p=0.2, i=0.0002, d=2, distance=100, bw=60):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = bw
    right_motor.reset_angle(0)
    while right_motor.angle()<distance:
        ls = left_sensor.reflection()
        rs = bw
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop + integral + diff))

def pid_left_to_rightX(speed=50, p=0.2, i=0.0002, d=2, stoplevel=40, bw=60):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = bw
    while right_sensor.reflection()>stoplevel:
        ls = left_sensor.reflection()
        rs = bw
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop + integral + diff))

def pid_right_to_leftX(speed=50, p=0.2, i=0.0002, d=2, stoplevel=40, bw=60):
    integral = errold = 0
    ls = bw
    rs = right_sensor.reflection()
    while left_sensor.reflection()>stoplevel:
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop + integral + diff))

def to_white_left(speed=30, stoplevel=50):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while left_sensor.reflection()<stoplevel: pass

def to_white_right(speed=30, stoplevel=50):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while right_sensor.reflection()<stoplevel: pass

def pid_straight(speed=50, p=0.2, i=0.0002, d=2, distance=100):
    integral = errold = 0
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    ls = left_motor.angle()
    rs = right_motor.angle()
    if distance>=0:
        while right_motor.angle()<distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            prop = (rs-ls)*p
            integral = integral + (rs-ls)*i
            diff = (rs-ls-errold)*d
            errold = rs-ls
            left_motor.dc(speed+round(prop + integral + diff))
            right_motor.dc(speed-round(prop + integral + diff))
    else:
        while right_motor.angle()>distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            prop = (ls-rs)*p
            integral = integral + (ls-rs)*i
            diff = (ls-rs-errold)*d
            errold = ls-rs 
            left_motor.dc(-speed-round(prop + integral + diff))
            right_motor.dc(-speed+round(prop + integral + diff))

def turn_motor(a=90):
    robot.settings(100,1000,100,1000)
    robot.turn(a)
    robot.stop()

def motor_elevator(speed=50,distance=100):
    UD_motor.run_angle(speed,distance)

def motor_claw(speed=50,distance=50):
    if speed<0:
        claw_motor.run_until_stalled(speed,Stop.HOLD)
    elif speed>0:
        claw_motor.stop()
        claw_motor.run_angle(speed,distance)
        claw_motor.stop()

def turn_motor_senser(a=50,bw=25):
    robot.drive(0,a)
    if a>0:
        while left_sensor.reflection()>bw: pass
    elif a<0:
        while right_sensor.reflection()>bw: pass
    rstop()
    turn_motor(a=-1*a/6)


def pid_run(speed=50,distance=100):
    robot.settings(speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()

def rgb_to_hsv(r,g,b):
    h = s = v = 0
    r, g, b = r/255.0 , g/255.0 , b/255.0
    mx = max(r,g,b)
    mn = min(r,g,b)
    df = mx-mn
    if mx==mn: h = 0
    elif mx == r: h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g: h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b: h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0: s = 0
    else: s=(df/mx)*100
    v = mx*100
    return h,s,v

def rgb_to_hsv_tuple(rgb):
    return rgb_to_hsv(rgb[0], rgb[1], rgb[2])


def color_WM(ID,start=0, end=100):
    h=s=v=0
    c=None
    dcolors={}
    archivecolors=[]
    while True:
        angle = robot.distance()
        if angle>=start:
            h,s,v = rgb_to_hsv_tuple(right_p_sensor.rgb())
            if (h>350 or h<50) and s!=0 and s<=50: c=Color.YELLOW
            elif (h>250 or h<50) and s!=0: c=Color.RED
            else: c=Color.BLACK
            archivecolors.append((angle, c, h,s,v))
            if c in dcolors:
                dcolors[c]+=1
            else:
                dcolors[c]=1
        if angle>end: break
    print(dcolors)
    print(archivecolors)
    c = max(dcolors, key=dcolors.get) if len(dcolors)>0 else None
    global WM
    WM[ID]=c


# (180.0, 100.0, 0.392156862745098) чёр. - 1
# (30.21052631578948, 50.00000000000001, 19.6078431372549) жол. - 2
# (354.0, 81.08108108108109, 14.50980392156863) крас. - 3

# (134.1176470588235, 73.91304347826086, 9.019607843137255) зел. - 4
# (235.0, 62.06896551724139, 22.74509803921569) бел. - 5

# while ev3.buttons.pressed()==[]: pass

WM = [None,None,None]
Ward_R = [0,0]
Ward_Y = [0,0]
Ward_G = [0,0]
Ward_B = [0,0]

turn_motor(a=45)
pid_run(speed=200,distance=250)
turn_motor(a=88)
robot.reset()
robot.drive(100,0)
t = _thread.start_new_thread(color_WM,(0,10,80))
t = _thread.start_new_thread(color_WM,(1,110,180))
t = _thread.start_new_thread(color_WM,(2,210,280))
while robot.distance()<300: pass
while right_sensor.reflection()>25: pass
rstop()
pid_run(speed=200,distance=40)
rstop()

turn_motor(a=88)
rstop()
pid_run(speed=200,distance=140)
rstop()
turn_motor(a=90)
pid_run(speed=200,distance=-120)
rstop()

turn_motor(a=40)
W_B_P = rgb_to_hsv_tuple(left_p_sensor.rgb())
print(W_B_P)

turn_motor(a=-40)
pid_run(speed=200,distance=-110)
rstop()
motor_claw(speed=-1000)

motor_elevator(speed=1000,distance=-190)
W_B_WM = rgb_to_hsv_tuple(left_p_sensor.rgb())
print(W_B_WM)

pid_run(speed=200,distance=70)
turn_motor(a=-40)
pid_run(speed=200,distance=-200)
rstop()
motor_elevator(speed=1000,distance=175)
turn_motor(a=40)

pid_run(speed=200,distance=-50)
rstop()

turn_motor(a=-93)

if W_B_P[0]>200: Ward_B[1]=5
elif W_B_P[0]<200: Ward_B[1]=4

if W_B_WM[0]>0 and W_B_WM[0]<50 and W_B_WM[0]!=0: Ward_B[0]=2
elif (W_B_WM[0]>300 or W_B_WM[0]<50) and W_B_WM[1]!=0: Ward_B[0]=3
elif W_B_WM[0]>100 or W_B_WM[0]<300 and W_B_WM[1]!=0: Ward_B[0]=1

print(Ward_B[0],Ward_B[1])

motor_claw(speed=1000)

robot.reset()
robot.drive(200,0)
while robot.distance()<100: pass
while left_sensor.reflection()>25: pass
rstop()

pid_run(speed=200,distance=40)
rstop()

turn_motor(a=-90)

pid_to_X(speed=70)
rstop()
pid_run(speed=200,distance=-30)
rstop()

# turn_motor(a=-90)

# pid_run(speed=100,distance=-100)
# rstop()
# W_Y_P = rgb_to_hsv_tuple(right_p_sensor.rgb())
# print(W_Y_P)

# turn_motor(a=-10)
# pid_run(speed=100,distance=-120)
# rstop()
# W_Y_WM = rgb_to_hsv_tuple(right_p_sensor.rgb())
# print(W_Y_WM)

# if W_Y_P[0]>200: Ward_Y[1]=5
# elif W_Y_P[0]<200: Ward_Y[1]=4

# if W_Y_WM[0]>10 and W_Y_WM[0]<50 and W_Y_WM[0]!=0: Ward_Y[0]=2
# elif (W_Y_WM[0]>300 or W_Y_WM[0]<50) and W_Y_WM[1]!=0: Ward_Y[0]=3
# elif W_Y_WM[0]>100 or W_Y_WM[0]<300 and W_Y_WM[1]!=0: Ward_Y[0]=1

# print(Ward_Y[0],Ward_Y[1])

# pid_run(speed=100,distance=120)
# rstop()
# turn_motor(a=40)

# motor_elevator(speed=1000,distance=-175)

# pid_run(speed=100,distance=-350)
# rstop()

# motor_elevator(speed=1000,distance=175)

# pid_run(speed=100,distance=350)
# turn_motor(a=-30)
# robot.reset()
# robot.drive(200,0)
# while robot.distance()<75: pass
# while left_sensor.reflection()>25: pass
# rstop()

# pid_run(speed=100,distance=70)
# turn_motor_senser(a=-50)
# pid_to_motor(speed=150,distance=300)
# pid_to_X(speed=150)
# rstop()

# pid_run(speed=100,distance=75)
# rstop()
# turn_motor(a=-90)
# pid_run(speed=100,distance=400)
# rstop()

# turn_motor(a=90)
# motor_elevator(speed=1000,distance=-175)
# pid_run(speed=100,distance=1000)
# rstop()
# motor_elevator(speed=1000,distance=175)