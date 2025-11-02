#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import _thread


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
# robot = DriveBase(left_motor, right_motor, 98, 155)
robot = DriveBase(left_motor, right_motor, wheel_diameter=68.8, axle_track=203.1)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
center_sensor = ColorSensor(Port.S4)
left_s_motor = Motor(Port.A)
right_s_motor = Motor(Port.D)

def rstop(wait_ms=35):
    robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
    left_motor.brake()
    right_motor.brake()
    wait(wait_ms)

def pid_color_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100):
    integral = errold = 0
    rs = rgb_to_hsv_tuple(right_sensor.rgb())[1]
    ls = rgb_to_hsv_tuple(left_sensor.rgb())[1]
    robot.reset()
    # right_motor.reset_angle(0)
    while robot.distance()<distance:
        rs = rgb_to_hsv_tuple(right_sensor.rgb())[1]
        ls = rgb_to_hsv_tuple(left_sensor.rgb())[1]
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_to_X(speed=50,p=0.3,i=0.0005,d=5,stoplevel=50):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = right_sensor.reflection()
    while ls+rs>stoplevel:
        ls = left_sensor.reflection()
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_right_to_leftX(speed=35,p=0.3,i=0.0005,d=5,stoplevel=40, bw=60):
    integral = errold = 0
    ls = bw
    rs = right_sensor.reflection()
    while left_sensor.reflection()>stoplevel:
        ls = bw
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_left_to_rightX(speed=35,p=0.3,i=0.0005,d=5,stoplevel=40, bw=60):
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
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def to_white2(speed=35,stoplevel=70):
    # left_motor.dc(speed)
    # right_motor.dc(speed)
    robot.drive(speed,0)
    while left_sensor.reflection()+right_sensor.reflection()<stoplevel: pass

def to_wall(distance=200, speed=-200, time_limit=5000):
    robot.reset()    
    robot.drive(speed,0)
    tl=StopWatch()
    while abs(robot.distance())<abs(distance) and not robot.distance_control.stalled() and tl.time()<time_limit: pass
    rstop()
    print('to_wall dist=', robot.distance(),'of',distance,  ', tl=', tl.time(), 'of' ,time_limit)

def to_white_left(speed=35,stoplevel=50):
    # left_motor.dc(speed)
    # right_motor.dc(speed)
    robot.drive(speed,0)
    while left_sensor.reflection()<stoplevel: pass 

def to_white_right(speed=35,stoplevel=50):
    # left_motor.dc(speed)
    # right_motor.dc(speed)
    robot.drive(speed,0)
    while right_sensor.reflection()<stoplevel: pass

def pid_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = right_sensor.reflection()
    robot.reset()
    # right_motor.reset_angle(0)
    while robot.distance()<distance:
        ls = left_sensor.reflection()
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_left_in_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100,bw=55):
    integral = errold = 0
    ls = left_sensor.reflection()
    rs = bw
    # right_motor.reset_angle(0)
    robot.reset()
    while robot.distance()<distance:
        ls = left_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_right_in_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100,bw=55):
    integral = errold = 0
    ls = bw
    rs = right_sensor.reflection()
    # right_motor.reset_angle(0)
    robot.reset()
    while robot.distance()<distance:
        rs = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_left_out_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100,bw=55):
    integral = errold = 0
    rs = left_sensor.reflection()
    ls = bw
    # right_motor.reset_angle(0)
    robot.reset()
    while robot.distance()<distance:
        rs = left_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))
        # print(ls)

def pid_right_out_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100,bw=55):
    integral = errold = 0
    rs = bw
    ls = right_sensor.reflection()
    # right_motor.reset_angle(0)
    robot.reset()
    while robot.distance()<distance:
        ls = right_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))

def pid_left_out_to_motor_container(speed=50,p=0.3,i=0.0005,d=5,distance=100,bw=55,ID=0, start=0, end=100, isStop=False):
    dcolors={}
    # global archivecolors
    archivecolors=[]
    # distarray=[]
    hsv=()
    d=h=s=v=0
    c = None
    integral = errold = 0
    rs = left_sensor.reflection()
    ls = bw
    # right_motor.reset_angle(0)
    robot.reset()
    angle = robot.distance()
    while angle<distance:
        angle=robot.distance()
        rs = left_sensor.reflection()
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        robot.drive(speed,round(prop+integral+diff))
        if end>angle>start:
            # c = side_sensor.color()
            h,s,v=rgb_to_hsv_tuple(side_sensor.rgb())
            #laundry
            #(120.0, 100.0, 0.392156862745098) - black
            #(49.09090909090913, 61.11111111111112, 7.058823529411764) - yellow
            # (10.0, 100.0, 2.352941176470588) - red
            # (51.42857142857145, 50.0, 5.490196078431373) - yellow
            c=None
            if s>=75:
                if (h>=0 and h<35) or h>330:
                    c=Color.RED
                elif h>=35 and h<60:
                    c=Color.YELLOW
                else: 
                    c=Color.BLACK
            elif h>=35 and h<60:
                c=Color.YELLOW
            elif (h>0 and h<35) or h>330:
                c=Color.RED
            else:
                c=Color.BLACK
            archivecolors.append((angle,d,c,h,s,v))
            if c in dcolors:
                dcolors[c]+=1
            else:
                dcolors[c]=1
        # left_motor.dc(speed+round(prop+integral+diff))
        # right_motor.dc(speed-round(prop+integral+diff))
        # print(ls)
    if isStop: rstop()
    print('------------')
    print(dcolors)
    # print(distarray)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors)>0 else None
    print(ID, 'container color is', c )
    global laundry_containers
    laundry_containers[ID]=None if c not in [Color.RED, Color.YELLOW, Color.BLACK] else c
    tmpl=[laundry_containers[0], laundry_containers[1]]
    if tmpl==[Color.YELLOW, Color.RED] or tmpl==[Color.RED, Color.YELLOW]: laundry_containers[2]=Color.BLACK
    elif tmpl==[Color.BLACK, Color.RED] or tmpl==[Color.RED, Color.BLACK]: laundry_containers[2]=Color.YELLOW
    elif tmpl==[Color.BLACK, Color.YELLOW] or tmpl==[Color.YELLOW, Color.BLACK]: laundry_containers[2]=Color.RED


def turn_right2(speed=45, distance=30, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    left_motor.dc(speed)
    right_motor.dc(-speed)
    while right_sensor.reflection()<bw+10: pass
    while right_sensor.reflection()>bw-10: pass
    while right_sensor.reflection()<bw+10: pass
    left_motor.brake()
    right_motor.brake()

def turn_left2(speed=45, distance=30, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    left_motor.dc(-speed)
    right_motor.dc(speed)
    while left_sensor.reflection()<bw+10: pass
    while left_sensor.reflection()>bw-10: pass
    while left_sensor.reflection()<bw+10: pass
    left_motor.brake()
    right_motor.brake()

def turn_left(speed=45, distance=45, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    robot.drive(0,-210)
    while left_sensor.reflection()<bw+10: pass
    while left_sensor.reflection()>bw-10: pass
    robot.drive(0,-140)
    while left_sensor.reflection()<bw+10: pass
    robot.stop()
    
def turn_right(speed=45, distance=45, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    robot.drive(0,210)
    while right_sensor.reflection()<bw+10: pass
    while right_sensor.reflection()>bw-10: pass
    robot.drive(0,140)
    while right_sensor.reflection()<bw+10: pass
    robot.stop()

def turn_right_1_wheel(speed=45, distance=30, bw=50):
    robot.settings(15*speed,1000,100,1000)
    robot.straight(distance)
    robot.stop()
    left_motor.dc(speed)
    right_motor.dc(0)
    while right_sensor.reflection()<bw+10: pass
    while right_sensor.reflection()>bw-10: pass
    while right_sensor.reflection()<bw+10: pass
    left_motor.brake()
    right_motor.brake()

def pid_straight(speed=50,p=0.3,i=0.005,d=5,distance=100):
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
            left_motor.dc(speed+round(prop+integral+diff))
            right_motor.dc(speed-round(prop+integral+diff))
    else:
        while right_motor.angle()>distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            prop = (ls-rs)*p
            integral = integral + (ls-rs)*i
            diff = (ls-rs-errold)*d
            errold = ls-rs
            left_motor.dc(-speed-round(prop+integral+diff))
            right_motor.dc(-speed+round(prop+integral+diff))

def pid_curve(speed=50,p=0.3,i=0.005,d=5,distance=100, turn=1):
    integral = errold = 0
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    ls = left_motor.angle()
    rs = right_motor.angle()
    while right_motor.angle()<distance:
        ls = left_motor.angle()
        rs = right_motor.angle()
        k=rs-ls if ls==0 else (rs/ls-turn)*10
        print(k, rs, ls)
        prop = k*p
        integral = integral + k*i
        diff = (k-errold)*d
        errold = k
        left_motor.dc(speed+turn*2+round(prop+integral+diff))
        right_motor.dc(speed-turn*2-round(prop+integral+diff))

def rgb_to_hsv(r, g, b):
    h = s = v = 0
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
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
        s = (df/mx)*100
    v = mx*100
    return h, s, v

def rgb_to_hsv_tuple(rgb):
    return rgb_to_hsv(rgb[0],rgb[1],rgb[2])

def pid_straight_accel(speed=50,p=0.3,i=0.005,d=5,distance=100, acceleration=5):
    accel=0.3
    accel_dist=0
    starting=True
    integral = errold = 0
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    ls = left_motor.angle()
    rs = right_motor.angle()
    if distance>=0:
        while right_motor.angle()<distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            if starting:
                if rs>distance-accel_dist:
                    starting=False
            if starting:
                if accel<1:
                    accel+=acceleration*0.001
                    accel_dist=rs
                else:
                    accel=1
            else:
                if accel>0.3:
                    accel-=acceleration*0.0015
                    # print('stop')    
            prop = (rs-ls)*p
            integral = integral + (rs-ls)*i
            diff = (rs-ls-errold)*d
            errold = rs-ls
            left_motor.dc((speed+round(prop+integral+diff))*accel)
            right_motor.dc((speed-round(prop+integral+diff))*accel)
            # print(accel, right_motor.angle(), right_motor.speed())
    else:
        while right_motor.angle()>distance:
            ls = left_motor.angle()
            rs = right_motor.angle()
            if starting:
                if rs<distance-accel_dist:
                    starting=False
            if starting:
                if accel<1:
                    accel+=acceleration*0.001
                    accel_dist=rs
                else:
                    accel=1
            else:
                if accel>0.3:
                    accel-=acceleration*0.0015
            prop = (ls-rs)*p
            integral = integral + (ls-rs)*i
            diff = (ls-rs-errold)*d
            errold = ls-rs
            left_motor.dc((-speed-round(prop+integral+diff))*accel)
            right_motor.dc((-speed+round(prop+integral+diff))*accel)

def pid_to_X_accel(speed=50,p=0.3,i=0.0005,d=5,stoplevel=50, acceleration=15):
    integral = errold = 0
    accel=0.3
    ls = left_sensor.reflection()
    rs = right_sensor.reflection()
    while ls+rs>stoplevel:
        ls = left_sensor.reflection()
        rs = right_sensor.reflection()
        if accel<1:
            accel+=acceleration*0.001
        else:
            accel=1
        prop = (ls-rs)*p
        integral = integral + (ls-rs)*i
        diff = (ls-rs-errold)*d
        errold = ls-rs
        left_motor.dc((speed+round(prop+integral+diff))*accel)
        right_motor.dc((speed-round(prop+integral+diff))*accel)

def pid_curve2(speed=50,p=0.3,i=0.005,d=5,distanceleft=500, distanceright=1000, acceleration=15):
    accel=0.3
    accel_dist=0
    starting=True
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    if speed>0:
        if distanceleft<distanceright:
            while right_motor.angle()<distanceright:
                rs=right_motor.angle()
                if starting:
                    if rs>distanceright-accel_dist:
                        starting=False
                if starting:
                    if accel<1:
                        accel+=acceleration*0.001
                        accel_dist=rs
                    else:
                        accel=1
                else:
                    if accel>0.3:
                        accel-=acceleration*0.0015
                right_motor.dc(speed*accel)
                left_motor.track_target(right_motor.angle()*distanceleft/distanceright)
        else:
            # left_motor.dc(speed)
            while left_motor.angle()<distanceleft:
                ls=left_motor.angle()
                if starting:
                    if ls>distanceleft-accel_dist:
                        starting=False
                if starting:
                    if accel<1:
                        accel+=acceleration*0.001
                        accel_dist=ls
                    else:
                        accel=1
                else:
                    if accel>0.3:
                        accel-=acceleration*0.0015
                left_motor.dc(speed*accel)
                right_motor.track_target(left_motor.angle()*distanceright/distanceleft)
    else:
        if distanceleft<distanceright:
            while right_motor.angle()>-distanceright:
                rs=right_motor.angle()
                if starting:
                    if rs<-distanceright+accel_dist:
                        starting=False
                if starting:
                    if accel<1:
                        accel+=acceleration*0.001
                        accel_dist=rs
                    else:
                        accel=1
                else:
                    if accel>0.3:
                        accel-=acceleration*0.0015
                right_motor.dc(speed*accel)
                left_motor.track_target(right_motor.angle()*distanceleft/distanceright)
        else:
            while left_motor.angle()>-distanceleft:
                ls=left_motor.angle()
                if starting:
                    if ls<-distanceleft+accel_dist:
                        starting=False
                if starting:
                    if accel<1:
                        accel+=acceleration*0.001
                        accel_dist=ls
                    else:
                        accel=1
                else:
                    if accel>0.3:
                        accel-=acceleration*0.0015
                left_motor.dc(speed*accel)
                right_motor.track_target(left_motor.angle()*distanceright/distanceleft)
        
def watch_container(ID, start=0, end=100):
    dcolors={}
    # global archivecolors
    archivecolors=[]
    # distarray=[]
    hsv=()
    d=h=s=v=0
    while True:
        angle=robot.distance()
        # distarray.append(angle)
        if angle>start:
            # c = side_sensor.color()
            h,s,v=rgb_to_hsv_tuple(side_sensor.rgb())
            #laundry
            #(120.0, 100.0, 0.392156862745098) - black
            #(49.09090909090913, 61.11111111111112, 7.058823529411764) - yellow
            # (10.0, 100.0, 2.352941176470588) - red
            # (51.42857142857145, 50.0, 5.490196078431373) - yellow
            c=None
            if s>=75:
                if (h>=0 and h<35) or h>330:
                    c=Color.RED
                elif h>=35 and h<60:
                    c=Color.YELLOW
                else: 
                    c=Color.BLACK
            elif h>=35 and h<60:
                c=Color.YELLOW
            elif (h>0 and h<35) or h>330:
                c=Color.RED
            else:
                c=Color.BLACK
            archivecolors.append((angle,d,c,h,s,v))
            if c in dcolors:
                dcolors[c]+=1
            else:
                dcolors[c]=1
        if angle>=end: break
    print('------------')
    print(dcolors)
    print(distarray)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors)>0 else None
    print(ID, 'container color is', c )
    global laundry_containers
    laundry_containers[ID]=None if c not in [Color.RED, Color.YELLOW, Color.BLACK] else c
    tmpl=[laundry_containers[0], laundry_containers[1]]
    if tmpl==[Color.YELLOW, Color.RED] or tmpl==[Color.RED, Color.YELLOW]: laundry_containers[2]=Color.BLACK
    elif tmpl==[Color.BLACK, Color.RED] or tmpl==[Color.RED, Color.BLACK]: laundry_containers[2]=Color.YELLOW
    elif tmpl==[Color.BLACK, Color.YELLOW] or tmpl==[Color.YELLOW, Color.BLACK]: laundry_containers[2]=Color.RED

class HospitalRoom: 
    def __init__(self, roomColor, markingBlockColor, laundryBlockColor, ballColor, tableColor, basketColor):
        self.__roomColor = roomColor
        self.__markingBlockColor = markingBlockColor
        self.__laundryBlockColor = laundryBlockColor
        self.__ballColor = ballColor
        self.__tableColor = tableColor
        self.__basketColor = basketColor

    def __init__(self, roomColor):
        self.__roomColor = roomColor
        self.__markingBlockColor = Color.PURPLE
        self.__laundryBlockColor = Color.PURPLE
        self.__ballColor = Color.RED
        self.__tableColor = roomColor
        self.__basketColor = roomColor

    @property
    def roomColor(self):
        return self.__roomColor
    @roomColor.setter
    def roomColor(self, rc):
        self.__roomColor=rc if rc in [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE] else None
    
    @property
    def markingBlockColor(self):
        return self.__markingBlockColor
    @markingBlockColor.setter
    def markingBlockColor(self, mbc):
        self.__markingBlockColor=mbc if mbc in [Color.RED, Color.YELLOW] else None

    @property
    def laundryBlockColor(self):
        return self.__laundryBlockColor
    @laundryBlockColor.setter
    def laundryBlockColor(self, lbc):
        self.__laundryBlockColor=lbc if lbc in [Color.RED, Color.YELLOW, Color.BLACK] else None

    @property
    def ballColor(self):
        return self.__ballColor
    @ballColor.setter
    def ballColor(self, bc):
        self.__ballColor=bc if bc in [Color.RED, Color.BLUE] else None

    @property
    def tableColor(self):
        return self.__tableColor
    @tableColor.setter
    def tableColor(self, tc):
        self.__tableColor=tc if tc in [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE] else None

    @property
    def basketColor(self):
        return self.__basketColor
    @basketColor.setter
    def basketColor(self, bc):
        self.__basketColor=bc if bc in [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE] else None
    
    def __str__(self):
        return "room %s, mark %s, laundry %s, ball %s, table %s, basket %s\n" % (self.roomColor, self.markingBlockColor, self.laundryBlockColor, self.ballColor, self.tableColor, self.basketColor)
    def __repr__(self):
        return "room %s, mark %s, laundry %s, ball %s, table %s, basket %s\n" % (self.roomColor, self.markingBlockColor, self.laundryBlockColor, self.ballColor, self.tableColor, self.basketColor)



    # mountain = [
    #     MountainPlace(0,True,Color.BROWN),
    #     MountainPlace(1,True,Color.BROWN),
    #     MountainPlace(2,True,Color.BROWN),
    #     MountainPlace(3,True,Color.BROWN),
    #     MountainPlace(4,True,Color.BROWN),
    #     MountainPlace(5,True,Color.BROWN),
    #     MountainPlace(5,True,Color.BROWN),
    #     MountainPlace(5,True,Color.BROWN)

    # ]


hospital = {
    Color.RED:   HospitalRoom(Color.RED), 
    Color.YELLOW:HospitalRoom(Color.YELLOW), 
    Color.GREEN: HospitalRoom(Color.GREEN), 
    Color.BLUE:  HospitalRoom(Color.BLUE)
}
indicator = [None,None] # left => right
rostenie = [None,None,None,None,None,None] # left => right
print(hospital)
handsClosed=False
# hasRightBottle=False
hasRightBottle=True
# hasLeftBottle=False
hasLeftBottle=True


robot.settings(400,1000,225,1000)




def YellowAndRed(roomID, learn=True):
    dcolors = {}
    archivecolors = []
    h = s = v = 0
    c = None
    while len(archivecolors)<11:
        h,s,v = rgb_to_hsv_tuple(center_sensor.rgb())
        if h >= 0 and h < 20 and s > 0:
            c = Color.RED
        elif h > 35 and h < 60:
            c = Color.YELLOW
        else:
            c = None

        archivecolors.append((c,h,s,v))
        if c in dcolors:
            dcolors[c]+=1
        else:
            dcolors[c]=1
    print('------------')
    print(dcolors)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors) > 0 else None
    print('laundry in ', roomID, 'color is', c )
    if learn:
        global indicator
        indicator[roomID] = None if c not in [Color.RED, Color.YELLOW] else c
        return indicator[roomID]
    else:
        return None if c not in [Color.RED, Color.YELLOW] else c

def BlackAndGreen(roomID, learn=True):
    dcolors = {}
    archivecolors = []
    h = s = v = 0
    c = None
    while len(archivecolors)<11:
        h,s,v = rgb_to_hsv_tuple(center_sensor.rgb())
        if h > 120 and h < 155 and v > 3:
            c = Color.GREEN
        elif h > 110 and h < 250 and v < 3:
            c = Color.BLACK
        else:
            c = None

        archivecolors.append((c,h,s,v))
        if c in dcolors:
            dcolors[c]+=1
        else:
            dcolors[c]=1
    print('------------')
    print(dcolors)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors) > 0 else None
    print('laundry in ', roomID, 'color is', c )
    if learn:
        global rostenie
        rostenie[roomID] = None if c not in [Color.BLACK, Color.GREEN] else c
        return rostenie[roomID]
    else:
        return None if c not in [Color.BLACK, Color.GREEN] else c


# for i in range ( 10, 0, -1):


while ev3.buttons.pressed()==[]: pass
wait(400)

# robot.straight(400)

# robot.turn(360) # right
# robot.turn(-360) # left

# robot.stop()
# left_motor.dc(0)
# right_motor.dc(0)
# left_motor.brake()
# right_motor.brake()

# robot.reset()
# robot.drive(400,90)
# while right_sensor.reflection()>40: pass
# while robot.distance()<100: pass

right_s_motor.run_until_stalled(-1500,Stop.HOLD,70)
right_s_motor.reset_angle(0)
left_s_motor.run_until_stalled(-1500,Stop.HOLD,70)
left_s_motor.reset_angle(0)
right_s_motor.run_until_stalled(-1500,Stop.BRAKE,70)
left_s_motor.run_until_stalled(-1500,Stop.BRAKE,70)

# print(BlackAndGreen(0,True))
# print(YellowAndRed(0,True))


# while ev3.buttons.pressed()==[]: pass
# wait(400)

t = _thread.start_new_thread(right_s_motor.run_target,(1500,65))
left_s_motor.run_target(1500,65)

robot.turn(45)
rstop()
robot.reset()
robot.drive(250,0)
while right_sensor.reflection()>40: pass
rstop()
robot.straight(-15)
robot.turn(-45)
rstop()
robot.reset()
robot.drive(250,0)
while robot.distance()<100: pass
while left_sensor.reflection()>40: pass
rstop()
robot.straight(50)
rstop()


# while ev3.buttons.pressed()==[]: pass
# wait(400)


t = _thread.start_new_thread(right_s_motor.run_until_stalled,(-500,Stop.BRAKE,50))
left_s_motor.run_until_stalled(-500,Stop.BRAKE,50)

robot.straight(-65)
rstop()
left_s_motor.run_target(1500,65)
robot.turn(50)
rstop()
robot.straight(60)
rstop()


# while ev3.buttons.pressed()==[]: pass
# wait(400)


left_s_motor.run_until_stalled(-1500,Stop.BRAKE,50)

robot.turn(-50-65)
rstop()
robot.straight(-40)
rstop()

right_s_motor.run_target(-1500,65)

robot.straight(100)
rstop()


# while ev3.buttons.pressed()==[]: pass
# wait(400)


right_s_motor.run_until_stalled(-500,Stop.BRAKE,50)

robot.turn(65)
rstop()
robot.straight(-50)
rstop()
robot.reset()
robot.drive(-250,0)
while robot.distance()>-100: pass
while left_sensor.reflection()>40: pass
rstop()
robot.straight(100)
robot.turn(90)
rstop()
robot.straight(100)
rstop()

# pid_to_X(speed=-200,p=0,i=0,d=0,stoplevel=50)
# rstop()
robot.reset()
robot.drive(-250,0)
while right_sensor.reflection()>40: pass
while left_sensor.reflection()>40: pass
rstop()

# while ev3.buttons.pressed()==[]: pass
# wait(400)


for i in range(5,-1,-1):
    if i==5:
        pid_to_motor(speed=250,p=0.2,i=0.0005,d=5,distance=481)
    elif i==4:
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=173)
    elif i==3:
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=177)
    elif i==2:
        pid_to_motor(speed=250,p=0.2,i=0.0005,d=5,distance=477)
    elif i==1:
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=166)
    elif i==0:
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=177)


    rstop()
    robot.straight(0)
    if i==-5 or i==2:
        robot.turn(-92)
    else:
        robot.turn(-90)
    rstop()


    # while ev3.buttons.pressed()==[]: pass
    # wait(400)


    robot.reset()
    robot.drive(200,0)
    while left_sensor.reflection()>45: pass
    rstop()

    robot.straight(33)
    rstop()

    print(BlackAndGreen(i,True),i)


    # while ev3.buttons.pressed()==[]: pass
    # wait(400)

    if rostenie[i]==None:
        ev3.speaker.play_notes(['G3/8', 'E2/4', 'C2/2'],147)

    if rostenie[i]==Color.BLACK:
        robot.straight(100)
        robot.straight(-100)
        rstop()

    robot.straight(-80)
    robot.turn(90)
    rstop()

robot.straight(250)
robot.turn(-90)
rstop()
robot.straight(130)
right_s_motor.run_until_stalled(1500,Stop.BRAKE,50)
robot.straight(-130)
robot.straight(130)
robot.straight(-130)
robot.turn(90)
rstop()
robot.straight(-250)
right_s_motor.run_until_stalled(-1500,Stop.BRAKE,50)
robot.turn(90)
rstop()
robot.straight(600)
robot.turn(90)
rstop()
robot.straight(750)
left_s_motor.run_until_stalled(1500,Stop.BRAKE,50)
robot.straight(-250)
left_s_motor.run_until_stalled(-1500,Stop.BRAKE,50)


# black = 70 ~ 120, 100, 0 ~ 5

# (90.0, 100.0, 4.705882352941177)
# (120.0, 100.0, 0.392156862745098)
# (100.0, 100.0, 3.529411764705882)
# (73.33333333333335, 100.0, 3.529411764705882)
# (120.0, 100.0, 0.784313725490196)

# yellow = 40 ~ 55, 85 ~ 95, 5 ~ 30

# (46.00000000000001, 90.90909090909092, 12.94117647058824)
# (42.85714285714289, 93.33333333333334, 5.88235294117647)
# (50.84745762711868, 86.76470588235295, 26.66666666666667)
# (40.0, 94.52054794520548, 28.62745098039216)
# (45.88235294117647, 94.44444444444445, 7.058823529411764)

# red = 12 ~ 20, 90 ~ 100, 5 ~ 25

# (12.0, 92.5925925925926, 10.58823529411765)
# (13.58490566037733, 100.0, 20.7843137254902)
# (12.85714285714283, 100.0, 5.490196078431373)
# (18.26086956521738, 92.00000000000001, 19.6078431372549)
# (13.63636363636363, 95.65217391304349, 9.019607843137255)

# green = 100 ~ 125, 85 ~ 100, 2 ~ 15

# (122.4, 92.5925925925926, 10.58823529411765)
# (120.0, 100.0, 2.745098039215686)
# (104.0, 96.77419354838712, 12.15686274509804)
# (122.7272727272727, 88.00000000000001, 9.803921568627452)
# (123.5294117647059, 94.44444444444445, 7.058823529411764)