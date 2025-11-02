#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
up_motor= Motor(Port.D)
down_motor= Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=95)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
Color_sensor = ColorSensor(Port.S4)
Color2_sensor = ColorSensor(Port.S1)

def rstop(wait_ms=35):
    left_motor.brake()
    right_motor.brake()
    wait(wait_ms)

def pid_to_X(speed=70, p=0.3, i=0.0005, d=5, stoplevel=50):
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
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

def to_white2(speed=40, stoplevel=70):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while left_sensor.reflection()+right_sensor.reflection()<stoplevel: pass

def pid_to_motor(speed=70, p=0.3, i=0.0005, d=5, distance=100):
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
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

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

def pid_right_in_to_motor(speed=50, p=0.2, i=0.0006, d=5, distance=100, bw=60):
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
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

def pid_left_in_to_motor(speed=50, p=0.2, i=0.0006, d=5, distance=100, bw=60):
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
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

def pid_left_to_rightX(speed=50, p=0.2, i=0.0006, d=5, stoplevel=40, bw=60):
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
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

def pid_right_to_leftX(speed=50, p=0.2, i=0.0006, d=5, stoplevel=40, bw=60):
    integral = errold = 0
    ls = bw
    rs = right_sensor.reflection()
    while left_sensor.reflection()>stoplevel:
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs 
        left_motor.dc(speed+round(prop + integral + diff))
        right_motor.dc(speed-round(prop + integral + diff))

def to_white_left(speed=30, stoplevel=50):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while left_sensor.reflection()<stoplevel: pass

def to_white_right(speed=30, stoplevel=50):
    left_motor.dc(speed)
    right_motor.dc(speed)
    while right_sensor.reflection()<stoplevel: pass

def rgb_to_hsv(r,g,b):
    h = s = v = 0
    r, g, b = r/255.0 , g/255.0 , b/255.0
    mx = max(r,g,b)
    mn = min(r,g,b)
    df = mx-mn
    if mx==mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s=(df/mx)*100
    v = mx*100
    return h,s,v

def rgb_to_hsv_tuple(rgb):
    return rgb_to_hsv(rgb[0], rgb[1], rgb[2])

def pid_straight(speed=50, p=0.2, i=0.001, d=5, distance=100):
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
        while right_motor.angle()<distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            prop = (ls-rs)*p
            integral = integral + (ls-rs)*i
            diff = (ls-rs-errold)*d
            errold = ls-rs 
            left_motor.dc(speed-round(prop + integral + diff))
            right_motor.dc(speed+round(prop + integral + diff))

def turn_motor(a=90):
    robot.settings(500,1000,100,1000)
    robot.turn(a)
    robot.stop()

def pid_run(speed=50 ,distance=100):
    robot.settings(speed,1000,100,1000)
    robot.straight(distance)
    robot.drive(0,0)
    robot.stop()

def pid_up_motor(up=False, speed=500, distance=245):
    if up == True:
        up_motor.run_angle(speed,-distance)
    elif up == False:
        up_motor.run_angle(speed,distance)

def pid_down_motor(down=False, speed=350, distance=-155):
    if down == True:
        down_motor.run_angle(speed,-distance)
    elif down == False:
        down_motor.run_angle(speed,distance)

# (39.0, 76.92307692307693, 10.19607843137255) жол. куб
# (223.6363636363636, 40.74074074074074, 10.58823529411765) ничего
# (134.1176470588235, 73.91304347826086, 9.019607843137255) зел. дом
# (220.5882352941177, 85.0, 15.68627450980392) син. дом
# (44.21052631578948, 76.00000000000001, 19.6078431372549) жол. дом
# (60.0, 100.0, 0.392156862745098) ничего
while ev3.buttons.pressed()==[]: pass
home1 = [0,0]
home2 = [0,0]
home3 = [0,0]
plus = 0
pid_run(speed=175, distance=350)
turn_motor(a=-90)
pid_run(speed=175, distance=217)
pid_run(distance=-20)
pid_down_motor(down=True)
turn_motor()
colorbook=rgb_to_hsv_tuple(Color2_sensor.rgb())
print(colorbook)
pid_run(speed=175, distance=420)
pid_down_motor()
pid_run(distance=-25)
turn_motor(a=-91)
pid_run(speed=175, distance=-160)
color1= rgb_to_hsv_tuple(Color_sensor.rgb())
print(color1)
if color1[0]<160 and color1[0]>110 and color1[2]>1:
    print('green')
    home1[0]=3
    pid_run(distance=-65)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160 and color1[0]>110 and color1[2]>1:
        print('green')
        home1[1]=3
    elif color1[0]<235 and color1[0]>200 and color1[2]>1:
        print('blue')
        home1[1]=2
    elif color1[0]<50 and color1[0]>35 and color1[2]>1:
        print('yollew')
        home1[1]=4
    else:
        print('NO')
elif color1[0]<235 and color1[0]>200 and color1[2]>1:
    print('blue')
    home1[0]=2
    pid_run(distance=-65)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160 and color1[0]>110 and color1[2]>1:
        print('green')
        home1[1]=3
    elif color1[0]<235 and color1[0]>200 and color1[2]>1:
        print('blue')
        home1[1]=2
    elif color1[0]<50 and color1[0]>35 and color1[2]>1:
        print('yollew')
        home1[1]=4
    else:
        print('NO')
elif color1[0]<50 and color1[0]>35 and color1[2]>1:
    print('yollew')
    home1[0]=4
    pid_run(distance=-65)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160 and color1[0]>110 and color1[2]>1:
        print('green')
        home1[1]=3
    elif color1[0]<235 and color1[0]>200 and color1[2]>1:
        print('blue')
        home1[1]=2
    elif color1[0]<50 and color1[0]>35 and color1[2]>1:
        print('yollew')
        home1[1]=4
    else:
        print('NO')
else:
    print('NO')
    pid_run(distance=-65)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160  and color1[0]>110 and color1[2]>5:
        print('green')
        home1[1]=3
    elif color1[0]<235 and color1[0]>200 and color1[2]>5:
        print('blue')
        home1[1]=2
    elif color1[0]<50 and color1[0]>35 and color1[2]>5:
        print('yollew')
        home1[1]=4
if colorbook[0]<100:
    plus = 4
    print('yollew cube')
    pid_run(speed=150, distance=325)
    turn_motor()
    pid_down_motor(down=True)
    pid_run(distance=-175)
    turn_motor(a=-88)
    pid_run(speed=200,distance=1500)
    turn_motor()
    pid_run(speed=175,distance=150)
    pid_down_motor()
    pid_run(distance=30)
    pid_run(distance=-40)
    turn_motor(a=-90)
    pid_run(speed=175, distance=-180)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160 and color1[0]>110 and color1[2]>1:
        print('green')
        home2[0]=3
        pid_run(distance=-65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[1]=2
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yollew')
            home2[1]=4
        else:
            print('NO')
    elif color1[0]<235 and color1[0]>200 and color1[2]>1:
        print('blue')
        home2[0]=2
        pid_run(distance=-65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[1]=2
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home2[1]=4
        else:
            print('NO')
    elif color1[0]<50 and color1[0]>35 and color1[2]>1:
        print('yellow')
        home2[0]=4
        pid_run(distance=-65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home2[1]=4
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[1]=2
        else:
            print('NO')
    else:
        print('NO')
        pid_run(distance=-65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home2[1]=4
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[1]=2
    pid_run(speed=175,distance=200)
    turn_motor(a=-90)
    pid_run(speed=175,distance=600)
    turn_motor(a=-90)
    pid_run(speed=175,distance=200)
    color1= rgb_to_hsv_tuple(Color_sensor.rgb())
    print(color1)
    if color1[0]<160 and color1[0]>110 and color1[2]>1:
        print('green')
        home3[0]=3
        pid_run(distance=65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home3[1]=3
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[1]=2
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yollew')
            home3[1]=4
        else:
            print('NO')
    elif color1[0]<235 and color1[0]>200 and color1[2]>1:
        print('blue')
        home3[0]=2
        pid_run(distance=65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[1]=2
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home3[1]=4
        else:
            print('NO')
    elif color1[0]<50 and color1[0]>35 and color1[2]>1:
        print('yellow')
        home3[0]=4
        pid_run(distance=65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home3[1]=4
        elif color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[1]=2
        else:
            print('NO')
    else:
        print('NO')
        pid_run(distance=65)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[1]=3
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home3[1]=4
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[1]=2
    pid_run(distance=150)
    turn_motor(a=-90)
    pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=500)
else:
    pid_run(speed=175,distance=200)
    turn_motor(a=-90)
    pid_run(speed=175,distance=300)
    turn_motor(a=88)
    pid_run(speed=200, distance=800)
    pid_run(distance=-20)
    pid_down_motor(down=True)
    turn_motor()
    colorbook=rgb_to_hsv_tuple(Color2_sensor.rgb())
    turn_motor(a=-90)
    pid_run(speed=200, distance=500)
    if colorbook[0]<200:
        plus=3
        print('green cube')
        turn_motor()
        pid_run(distance=200)
        turn_motor(a=-90)
        pid_run(speed=175,distance=300)
        turn_motor()
        pid_run(speed=200,distance=150)
        pid_down_motor()
        pid_run(distance=-25)
        turn_motor(a=-90)
        pid_run(speed=175,distance=-170)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[0]=3
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[0]=2
            pid_run(distance=-65)
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yollew')
            home2[0]=4
            pid_run(distance=-65)
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        else:
            print('NO')
            pid_run(distance=-65)
            print(color1)
            if color1[0]<160  and color1[0]>110 and color1[2]>5:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>5:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>5:
                print('yollew')
                home2[1]=4
        pid_run(speed=175,distance=200)
        turn_motor(a=-90)
        pid_run(speed=200,distance=750)
        turn_motor(a=-90)
        pid_run(speed=175,distance=200)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home3[0]=3
            pid_run(distance=65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home3[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home3[1]=4
            else:
                print('NO')
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[0]=2
            pid_run(distance=65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yellow')
                home3[1]=4
            else:
                print('NO')
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yellow')
            home3[0]=4
            pid_run(distance=65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yellow')
                home3[1]=4
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            else:
                print('NO')
        else:
            print('NO')
            pid_run(distance=65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yellow')
                home3[1]=4
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
        pid_run(distance=150)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=500)
    else:
        pid_down_motor()
        turn_motor(a=-90)
        pid_run()
        pid_run(distance=-20)
        pid_down_motor(down=True)
        plus=2
        print('blue cube')
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        turn_motor()
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=300)
        pid_down_motor()
        pid_run(distance=-25)
        turn_motor(a=-90)
        pid_run(speed=175,distance=-170)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home3[0]=3
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home3[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home3[1]=4
            else:
                print('NO')
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home3[0]=2
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home3[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home3[1]=4
            else:
                print('NO')
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yollew')
            home3[0]=4
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home3[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home3[1]=4
            else:
                print('NO')
        else:
            print('NO')
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160  and color1[0]>110 and color1[2]>5:
                print('green')
                home3[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>5:
                print('blue')
                home3[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>5:
                print('yollew')
                home3[1]=4
        pid_run(speed=175, distance=350)
        turn_motor()
        pid_run(distance=25)
        pid_down_motor(down=True)
        pid_run(speed=200,distance=-500)
        turn_motor()
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=450)
        turn_motor()
        pid_run(speed=175,distence=150)
        pid_down_motor()
        pid_run(distence=-20)
        turn_motor(a=-90)
        pid_run(speed=175,distance=-170)
        color1= rgb_to_hsv_tuple(Color_sensor.rgb())
        print(color1)
        if color1[0]<160 and color1[0]>110 and color1[2]>1:
            print('green')
            home2[0]=3
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        elif color1[0]<235 and color1[0]>200 and color1[2]>1:
            print('blue')
            home2[0]=2
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        elif color1[0]<50 and color1[0]>35 and color1[2]>1:
            print('yollew')
            home2[0]=4
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160 and color1[0]>110 and color1[2]>1:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>1:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>1:
                print('yollew')
                home2[1]=4
            else:
                print('NO')
        else:
            print('NO')
            pid_run(distance=-65)
            color1= rgb_to_hsv_tuple(Color_sensor.rgb())
            print(color1)
            if color1[0]<160  and color1[0]>110 and color1[2]>5:
                print('green')
                home2[1]=3
            elif color1[0]<235 and color1[0]>200 and color1[2]>5:
                print('blue')
                home2[1]=2
            elif color1[0]<50 and color1[0]>35 and color1[2]>5:
                print('yollew')
                home2[1]=4
        pid_run(speed=175,distance=200)
        turn_motor(a=-90)
        pid_run(distance=130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=450)
        turn_motor(a=-90)
print('cube finished')
if home2 == [2,2] or (home2 == [0,2] or home2 == [2,0]):
    pid_run(speed=175,distance=-300)
    turn_motor(a=-90)
    pid_up_motor(distance=180)
    pid_run(speed=200,distance=500)
    pid_up_motor(up=True, distance=90)
    pid_run(distance=-100)
    turn_motor()
    pid_run(speed=200,distance=450)
    pid_up_motor(distance=155)
    pid_run(speed=175,distance=-130)
    turn_motor()
    pid_run(speed=200,distance=450)
    pid_up_motor(up=True)
elif home2 == [3,3] or (home2 == [0,3] or home2 == [3,0]):
    pid_run(distance=-50)
    turn_motor()
    pid_run(speed=175,distance=250)
    pid_up_motor(distance=180)
    turn_motor(a=-90)
    pid_run(distance=100)
    pid_up_motor(up=True, distance=30)
    pid_run(distance=30)
    pid_up_motor(up=True, distance=60)
    pid_run(distance=-50)
    turn_motor()
    pid_run(speed=200, distance=700)
    turn_motor()
    pid_run(speed=175,distance=130)
    pid_up_motor(distance=90)
    pid_run(speed=175,distance=-130)
    turn_motor()
    pid_run(speed=200,distance=450)
    pid_up_motor(up=True)
elif home2 == [4,4] or (home2 == [0,4] or home2 == [4,0]):
    pid_run(speed=175,distance=-300)
    turn_motor()
    pid_run(speed=175,distance=250)
    turn_motor()
    pid_down_motor(down=True)
    pid_run(speed=175,distance=-300)
    turn_motor()
    pid_run(speed=200,distance=800)
    turn_motor()
    pid_run(distance=50)
    pid_down_motor()
    pid_run(distance=80)
    pid_run(speed=175,distance=-130)
    turn_motor()
    pid_run(speed=200,distance=450)
elif (home2 == [3,4] or home2 == [4,3]) or (home2 == [2,4] or home2 == [4,2]):
    pid_run(speed=175,distance=-300)
    turn_motor()
    pid_run(speed=175,distance=250)
    turn_motor()
    pid_down_motor(down=True)
    pid_run(speed=175,distance=-300)
    turn_motor()
    pid_run(speed=200,distance=800)
    turn_motor()
    pid_run(distance=50)
    pid_down_motor()
    pid_run(distance=80)
    pid_run(speed=175,distance=-130)
    turn_motor()
    pid_run(speed=200,distance=450)
elif home2 == [2,3] or home2 == [3,2]:
    if plus == 2 or plus == 3:
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=700)
        turn_motor()
        pid_run(speed=175,distance=130)
        pid_up_motor(distance=90)
        pid_run(speed=175,distance=-130)
        turn_motor()
        pid_run(speed=200,distance=450)
        pid_up_motor(up=True)
    elif plus == 4:
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_up_motor(distance=180)
        pid_run(distance=500)
        pid_up_motor(up=True, distance=90)
        pid_run(distance=-100)
        turn_motor()
        pid_run(speed=200,distance=450)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-130)
        turn_motor()
        pid_run(speed=200,distance=450)
        pid_up_motor(up=True)
print('home2 finished')
if puls>0:
    if (home1==[2,2] and (plus==2 or plus==3)) or (home1==[0,2] or home1==[2,0]) and ((plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2])):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=150, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=155)
        pid_run(speed=200,distance=-700)
        turn_motor(a=-90)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=1500)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=120)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,2] and plus==4) or ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2==[0,3] or home2==[3,0])) or ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2])) or ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2])) or ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0])):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[3,3] and (plus==2 or plus==3)) or ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3)):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-180)
        turn_motor(a=-90)
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_up_motor(up=True, distance=60)
        pid_run(distance=50)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=90)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[3,3] and plus==4) or ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0])) or ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0])) or ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2])) or ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2])) or ((home1==[0,3] or home1==[3,0]) and plus==4):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[4,4] and (plus==2 or plus==3)) or ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2])):
        turn_motor(a=-90)
        pid_run(speed=175,distance=-300)
        turn_motor()
        pid_run(speed=175,distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_run(speed=200,distance=800)
        turn_motor(a=-90)
        pid_run(distance=50)
        pid_down_motor()
        pid_run(distance=80)
        pid_run(speed=200, distance=-600)
        turn_motor(a=-90)
        pid_run(speed=175,distance=150)
        turn_motor(a=-90)
        pid_run(distance=30)
        pid_down_motor(down=True)
        pid_run(speed=200, distance=-500)
        turn_motor()
        pid_run(speed=175,distance=150)
        turn_motor()
        pid_down_motor()
        pid_run()
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[4,4] and plus==4) or ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2])) or ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[0,3] or home2==[3,0])) or ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2])):
        turn_motor(a=-90)
        pid_run(speed=175,distance=-300)
        turn_motor()
        pid_run(speed=175,distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_run(speed=200,distance=800)
        turn_motor(a=-90)
        pid_run(distance=50)
        pid_down_motor()
        pid_run(distance=80)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0])):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=200,distance=-700)
        turn_motor(a=-90)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=150, distance=1500)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=120)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2==[0,3] or home2==[3,0]):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=150, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-180)
        turn_motor(a=-90)
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_up_motor(up=True, distance=60)
        pid_run(distance=50)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=90)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=200,distance=-500)
        turn_motor(a=-90)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=1500)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=500)
        pid_up_motor(distance=120)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2]):
        turn_motor(a=-90)
        pid_run(speed=175,distance=-300)
        turn_motor()
        pid_run(speed=175,distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_run(speed=200,distance=800)
        turn_motor(a=-90)
        pid_run(distance=50)
        pid_down_motor()
        pid_run(distance=80)
        pid_run(speed=200,distance=-700)
        turn_motor(a=-90)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=1500)
        pid_up_motor(up=True, distance=60)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=120)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=155)
        pid_run(speed=200, distance=-600)
        turn_motor(a=-90)
        pid_run(speed=175,distance=150)
        turn_motor(a=-90)
        pid_run(distance=30)
        pid_down_motor(down=True)
        pid_run(speed=200, distance=-500)
        turn_motor()
        pid_run(speed=175,distance=150)
        turn_motor()
        pid_down_motor()
        pid_run()
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=600)
        pid_up_motor(distance=155)
        pid_run(speed=200, distance=-600)
        turn_motor(a=-90)
        pid_run(speed=200,distance=700)
        turn_motor(a=-90)
        pid_run(distance=30)
        pid_down_motor(down=True)
        pid_run(speed=200, distance=-500)
        turn_motor()
        pid_run(speed=200,distance=700)
        turn_motor()
        pid_down_motor()
        pid_run()
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[0,3] or home2==[3,0]):
        turn_motor(a=-90)
        pid_run(speed=175,distance=-300)
        turn_motor()
        pid_run(speed=175,distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_run(speed=200,distance=800)
        turn_motor(a=-90)
        pid_run(distance=50)
        pid_down_motor()
        pid_run(distance=80)
        pid_run(speed=175,distance=-180)
        turn_motor(a=-90)
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_up_motor(up=True, distance=60)
        pid_run(distance=50)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=500)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=90)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=200, distance=-600)
        turn_motor(a=-90)
        pid_run(speed=175,distance=150)
        turn_motor(a=-90)
        pid_run(distance=30)
        pid_down_motor(down=True)
        pid_run(speed=200, distance=-500)
        turn_motor()
        pid_run(speed=175,distance=150)
        turn_motor()
        pid_down_motor()
        pid_run()
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif (home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]):
        turn_motor(a=-90)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=175,distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        turn_motor()
        pid_run(speed=200, distance=600)
        turn_motor()
        pid_run(speed=175,distance=180)
        pid_up_motor(distance=155)
        pid_run(speed=200, distance=-600)
        turn_motor(a=-90)
        pid_run(speed=200,distance=700)
        turn_motor(a=-90)
        pid_run(distance=30)
        pid_down_motor(down=True)
        pid_run(speed=200, distance=-500)
        turn_motor()
        pid_run(speed=200,distance=700)
        turn_motor()
        pid_down_motor()
        pid_run()
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2])) or ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2==[2,3] or home2==[3,2])):
        turn_motor(a=180)
        pid_run(speed=175,distance=250)
        turn_motor(a=-90)
        pid_run(speed=175,distance=350)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=90)
        pid_run(speed=200, distance=-1500)
        turn_motor()
        pid_run(speed=200, distance=750)
        pid_up_motor(distance=155)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
    elif ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2])) or ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2])):
        turn_motor(a=-90)
        pid_run(speed=175,distance=-300)
        turn_motor()
        pid_run(speed=200,distance=750)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(speed=175,distance=-300)
        turn_motor(a=-90)
        pid_run(speed=175,distance=150)
        turn_motor(a=-90)
        pid_run(distance=50)
        pid_down_motor()
        pid_run(distance=80)
        pid_run(speed=175,distance=-130)
        turn_motor(a=-90)
        pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=1000)
print('home1 finished')
if plus == 2 or plus == 3:
    if home3==[2,2]:
        turn_motor()
        pid_run(distance=-300)
        turn_motor(a=-90)
        pid_up_motor(distance=180)
        pid_run(distance=500)
        pid_up_motor(up=True, distance=90)
        pid_run(distance=-500)
        turn_motor(a=-90)
        pid_run(distance=350)
        pid_up_motor(distance=155)
        pid_run(speed=80, distance=-750)
        turn_motor(a=-90)
        pid_run(speed=80,distance=750)
        trun_motor()
    elif home3==[3,3]:
        turn_motor()
        pid_run(distance=-50)
        turn_motor()
        pid_run(distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        pid_run(speed=100, distance=-600)
        turn_motor(a=-90)
        pid_run(distance=250)
        turn_motor(a=-90)
        pid_run(distance=200)
        pid_up_motor(distance=90)
        pid_run(speed=80,distance=-750)
        turn_motor(a=-90)
        pid_run(speed=80,distance=750)
        trun_motor()
        pid_up_motor(up=True)
    elif home3==[4,4]:
        turn_motor()
        pid_run(distance=-300)
        turn_motor()
        pid_run(distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(distance=-100)
        turn_motor()
        pid_run(distance=300)
        turn_motor(a=-90)
        pid_down_motor()
        pid_run(distance=150)
        pid_run(distance=-650)
        turn_motor(a=-90)
        pid_run(speed=80,distance=650)
        trun_motor()
    elif home3==[2,3] or home3==[3,2]:
        # green
        if (home2==[4,4] and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[0,2] or home2==[2,0]) and (home1==[4,4] and (plus==2 or plus==3))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # blue
        elif (home2==[4,4] and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[0,3] or home2==[3,0]) and (home1==[4,4] and (plus==2 or plus==3))) or((home2==[0,4] or home2==[4,0]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
        # top blue
        elif ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
    elif home3==[2,4] or home3==[4,2]:
        # yellow
        if (home2==[3,3] and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[0,2] or home2==[2,0]) and (home1==[3,3] and (plus==2 or plus==3))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2==[0,3] or home2==[3,0]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # blue
        elif (home2==[3,3] and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[0,3] or home2==[3,0]))) or ((home2==[0,4] or home2==[4,0]) and (home1==[3,3] and (plus==2 or plus==3))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
        # top blue
        elif ((home2==[0,4] or home2==[4,0]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
    elif home3==[4,3] or home3==[3,4]:
        # top green
        if ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,3] or home2==[3,0]) and h1_(2,4).p(2)==1) or ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # yellow
        elif (home2==[2,2] and ((home1==[0,3] or home1==[3,0]) and (plus==2 or plus==3))) or ((home2==[0,3] or home2==[3,0]) and (home1==[2,2] and (plus==2 or plus==3))) or ((home2==[0,2] or home2==[2,0]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # green
        elif (home2==[2,2] and ((home1==[0,4] or home1==[4,0]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and (home1==[2,2] and (plus==2 or plus==3))) or ((home2==[0,2] or home2==[2,0]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,2] or home1==[2,0]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
    elif home3==[2,0] or home3==[0,2]:
        # blue
        if (home2==[4,4] and (home1==[3,3] and (plus==2 or plus==3))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or (home2==[3,3] and (home1==[4,4] and (plus==2 or plus==3))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
        # top blue
        elif (home2==[3,3] and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,4] or home2==[4,2]) and (home1==[3,3] and (plus==2 or plus==3))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[2,3] or home2==[3,2]) and (home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0])) or ((home2==[2,3] or home2==[3,2]) and (home1==[4,4] and (plus==2 or plus==3))) or (home2==[4,4] and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
    elif home3==[0,3] or home3==[3,0]:
        # green
        if (home2==[4,4] and (home1==[2,2] and (plus==2 or plus==3))) or (home2==[2,2] and (home1==[4,4] and (plus==2 or plus==3))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # top green
        elif (home2==[4,4] and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or (home2==[2,2] and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[3,4] or home2==[3,4]) and (home1==[2,2] and (plus==2 or plus==3))) or ((home2==[3,4] or home2==[3,4]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
    elif home3==[0,4] or home3==[4,0]:
        # yellow
        if (home2==[2,2] and (home1==[3,3] and (plus==2 or plus==3))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0]))) or (home2==[3,3] and (home1==[2,2] and (plus==2 or plus==3))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # top yellow
        elif (home2==[3,3] and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or (home2==[2,2] and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,4] or home2==[4,2]) and (home1==[3,3] and (plus==2 or plus==3))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,4] or home1==[4,2]) and (plus==2 or plus==3) and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[3,4] or home1==[4,3]) and (plus==2 or plus==3) and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[4,3] or home2==[3,4]) and (home1==[2,2] and (plus==2 or plus==3))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,3] or home1==[3,2]) and (plus==2 or plus==3) and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
elif plus == 4:
    if home3==[2,2]:
        turn_motor()
        pid_run(distance=-300)
        turn_motor(a=-90)
        pid_up_motor(distance=180)
        pid_run(distance=500)
        pid_up_motor(up=True, distance=90)
        pid_run(distance=-500)
        turn_motor(a=-90)
        pid_run(distance=350)
        pid_up_motor(distance=155)
        pid_run(distance=-150)
        turn_motor()
        pid_up_motor(distance=180)
        pid_run(distance=500)
        pid_up_motor(up=True, distance=90)
        pid_run(distance=-500)
        turn_motor(a=-90)
        pid_up_motor(distance=155)
        pid_run(distance=150)
        pid_run(speed=80, distance=-750)
        turn_motor(a=-90)
        pid_run(speed=80,distance=750)
        trun_motor()
    elif home3==[3,3]:
        turn_motor()
        pid_run(distance=-50)
        turn_motor()
        pid_run(distance=250)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        pid_run(speed=100, distance=-600)
        turn_motor(a=-90)
        pid_run(distance=250)
        turn_motor(a=-90)
        pid_run(distance=200)
        pid_up_motor(distance=90)
        pid_run(distance=-700)
        turn_motor()
        pid_run(distance=500)
        pid_up_motor(distance=180)
        turn_motor(a=-90)
        pid_run(distance=100)
        pid_up_motor(up=True, distance=30)
        pid_run(distance=30)
        pid_up_motor(up=True, distance=60)
        pid_run(distance=-50)
        pid_run(speed=100, distance=-600)
        turn_motor(a=-90)
        pid_run(distance=500)
        turn_motor(a=-90)
        pid_run(distance=200)
        pid_up_motor(distance=90)
        pid_run(speed=80,distance=-750)
        turn_motor(a=-90)
        pid_run(speed=80,distance=750)
        trun_motor()
        pid_up_motor(up=True)
    elif home3==[4,4]:
        turn_motor()
        pid_run(distance=-300)
        turn_motor()
        pid_run(distance=250)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(distance=-100)
        turn_motor()
        pid_run(distance=300)
        turn_motor(a=-90)
        pid_down_motor()
        pid_run(distance=150)
        pid_run(distance=-150)
        turn_motor(a=-90)
        pid_run(distance=750)
        turn_motor()
        pid_down_motor(down=True)
        pid_run(distance=-100)
        turn_motor()
        pid_run(distance=750)
        turn_motor(a=-90)
        pid_down_motor()
        pid_run(distance=150)
        pid_run(distance=-650)
        turn_motor(a=-90)
        pid_run(speed=80,distance=650)
        trun_motor()
    elif home3==[2,3] or home3==[3,2]:
        # green
        # 2 top bule
        if ((home2==[0,2] or home2==[2,0]) and (home1==[4,4] and plus==4)) or (home2==[4,4] and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(distance=-150)
            turn_motor()
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_up_motor(distance=155)
            pid_run(distance=150)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
        # blue
        # 2 top green
        elif (home2==[4,4] and ((home1==[0,3] or home1==[3,0]) and plus==4)) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[0,3] or home2==[3,0]) and (home1==[4,4] and plus==4)) or ((home2==[0,4] or home2==[4,0]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(distance=-700)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # top bule
        # 2 top green
        elif ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and plus==4)) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(distance=-700)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)           
    elif home3==[2,4] or home3==[4,2]:
        # yellow
        # 2 top bule
        if (home2==[3,3] and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2==[0,3] or home2==[3,0]))) or ((home2==[0,2] or home2==[2,0]) and (home1==[3,3] and plus==4)) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,3] or home1==[3,0]) and plus==4)):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-150)
            turn_motor()
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_up_motor(distance=155)
            pid_run(distance=150)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
        # blue
        # 2 top yellow
        elif (home2==[3,3] and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and (home1==[3,3] and plus==4)) or ((home2==[0,3] or home2==[3,0]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[0,3] or home2==[3,0]))) or ((home2==[3,4] or home2==[4,3]) and ((home1==[0,3] or home1==[3,0]) and plus==4)):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(distance=-150)
            turn_motor(a=-90)
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # top bule
        # 2 top yellow
        elif ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and plus==4)) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(distance=-150)
            turn_motor(a=-90)
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
    elif home3==[4,3] or home3==[3,4]:
        # yellow
        # 2 top green
        if (home2==[2,2] and ((home1==[0,3] or home1==[3,0]) and plus==4)) or ((home2==[0,3] or home2==[3,0]) and (home1==[2,2] and plus==4)) or ((home2==[0,2] or home2==[2,0]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2==[2,3] or home2==[3,2]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-700)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # green
        # 2 top yellow
        elif (home2==[2,2] and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and (home1==[2,2] and plus==4)) or ((home2==[0,2] or home2==[2,0]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(distance=-150)
            turn_motor(a=-90)
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # top yellow
        # 2 top green
        elif ((home2==[3,4] or home2==[4,3]) and ((home1==[0,2] or home1==[2,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[0,4] or home1==[4,0]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[0,4] or home2==[4,0]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[0,3] or home2==[3,0]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[0,2] or home2==[2,0]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[0,3] or home1==[3,0]) and plus==4)):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-700)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
    elif home3==[2,0] or home3==[0,2]:
        # bule
        # 2 top bule
        if (home2==[4,4] and (home1==[3,3] and plus==4)) or ((home2==[4,3] or home2==[3,4]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or (home2==[3,3] and (home1==[4,4] and plus==4)):
            turn_motor()
            pid_run(distance=-300)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=350)
            pid_up_motor(distance=155)
            pid_run(distance=-150)
            turn_motor()
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_up_motor(distance=155)
            pid_run(distance=150)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor() 
        # top bule
        elif (home2==[4,4] and (home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0])) or (home2==[3,3] and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,4] or home2==[4,2]) and (home1==[3,3] and plus==4)) or ((home2==[2,4] or home2==[4,2]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[2,3] or home2==[3,2]) and (home1==[4,4] and plus==4)):
            turn_motor()
            pid_run(distance=-450)
            turn_motor(a=-90)
            pid_up_motor(distance=180)
            pid_run(distance=500)
            pid_up_motor(up=True, distance=90)
            pid_run(distance=-500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=155)
            pid_run(speed=80, distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
    elif home3==[0,3] or home3==[3,0]:
        # green
        # 2 top green
        if (home2==[4,4] and (home1==[2,2] and plus==4)) or (home2==[2,2] and (home1==[4,4] and plus==4)):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=250)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=250)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(distance=-700)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
        # top green
        elif (home2==[4,4] and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or (home2==[2,2] and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[2,3] or home2==[3,2]) and (home1==[4,4] and plus==4)) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,4] or home2==[4,2]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[3,4] or home2==[3,4]) and (home1==[2,2] and plus==4)) or ((home2==[3,4] or home2==[3,4]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))) or ((home2==[3,4] or home2==[3,4]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2==[4,3] or home2==[3,4] or home2==[0,4] or home2==[0,4] or home2==[2,4] or home2==[4,2]))):
            turn_motor()
            pid_run(distance=-50)
            turn_motor()
            pid_run(distance=500)
            pid_up_motor(distance=180)
            turn_motor(a=-90)
            pid_run(distance=100)
            pid_up_motor(up=True, distance=30)
            pid_run(distance=30)
            pid_up_motor(up=True, distance=60)
            pid_run(distance=-50)
            pid_run(speed=100, distance=-600)
            turn_motor(a=-90)
            pid_run(distance=500)
            turn_motor(a=-90)
            pid_run(distance=200)
            pid_up_motor(distance=90)
            pid_run(speed=80,distance=-750)
            turn_motor(a=-90)
            pid_run(speed=80,distance=750)
            trun_motor()
            pid_up_motor(up=True)
    elif home3==[0,4] or home3==[4,0]:
        # yellow
        # 2 top yellow
        if (home2==[2,2] and (home1==[3,3] and plus==4)) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[2,0]))) or (home2==[3,3] and (home1==[2,2] and plus==4)):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=250)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=300)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-150)
            turn_motor(a=-90)
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
        # top yellow
        elif (home2==[2,2] and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or (home2==[3,3] and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2]))) or ((home2==[2,4] or home2==[4,2]) and (home1==[3,3] and plus==4)) or ((home2==[2,4] or home2==[4,2]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[2,4] or home1==[4,2]) and plus==4 and (home2==[2,3] or home2==[3,2] or home2==[0,2] or home2==[0,2]))) or ((home2==[2,3] or home2==[3,2]) and ((home1==[3,4] or home1==[4,3]) and plus==4 and (home2!=[4,3] and home2!=[3,4] and home2!=[0,4] and home2!=[0,4] and home2!=[2,4] and home2!=[4,2]))) or ((home2==[4,3] or home2==[3,4]) and (home1==[2,2] and plus==4)) or ((home2==[4,3] or home2==[3,4]) and ((home1==[2,3] or home1==[3,2]) and plus==4 and (home2!=[2,3] and home2!=[3,2] and home2!=[0,2] and home2!=[2,0] and home2!=[0,3] and home2!=[3,0]))):
            turn_motor()
            pid_run(distance=-300)
            turn_motor()
            pid_run(distance=750)
            turn_motor()
            pid_down_motor(down=True)
            pid_run(distance=-100)
            turn_motor()
            pid_run(distance=750)
            turn_motor(a=-90)
            pid_down_motor()
            pid_run(distance=150)
            pid_run(distance=-650)
            turn_motor(a=-90)
            pid_run(speed=80,distance=650)
            trun_motor()
print('home3 finished')
pid_to_motor(speed=80, p=0.0005 ,i=0.0013, distance=300)
turn_motor()
pid_run(speed=175,distance=200)
turn_motor(a=-90)
pid_run(distance=100)
turn_motor(a=-90)
pid_down_motor(down=True)
turn_motor(a=-90)
pid_run(distance=100)
turn_motor()
pid_run(speed=175,distance=150)
turn_motor()
pid_run(distance=20)
pid_down_motor()
pid_run(distance=-20)
turn_motor(a=-90)
pid_run(speed=175,distance=250)
turn_motor()
pid_run(distance=100)
turn_motor()
pid_down_motor(down=True)
turn_motor()
pid_run(distance=100)
turn_motor(a=-90)
pid_run(speed=175,distance=150)
turn_motor(a=-90)
pid_run(distance=20)
pid_down_motor()
pid_run(distance=-20)
turn_motor(a=-90)
pid_run(speed=200,distance=400)
turn_left()
pid_run(speed=175,distance=200)
pid_run(distance=-20)
print('graduated from the program')