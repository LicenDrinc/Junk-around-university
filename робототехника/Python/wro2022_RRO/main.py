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
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
# robot = DriveBase(left_motor, right_motor, 98, 116.7)
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=124)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
side_sensor = ColorSensor(Port.S1)
hand_sensor = ColorSensor(Port.S4)
# dist_sensor = InfraredSensor(Port.S1)
# gyro_sensor = GyroSensor(Port.S1, Direction.CLOCKWISE)positive_direction=Direction.COUNTERCLOCKWISE,
hand_motor = Motor(Port.A)
gate_motor = Motor(Port.D, gears=[20,12])#gears=[12,28,20]

def rstop(wait_ms=35):
    robot.stop()
    left_motor.dc(0)
    right_motor.dc(0)
    left_motor.brake()
    right_motor.brake()
    wait(wait_ms)

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
        
def gyropid_to_motor(speed=50,p=0.3,i=0.0005,d=5,distance=100, head=180):
    integral = errold = 0
    right_motor.reset_angle(0)
    while right_motor.angle()<distance:
        curhead=gyro_sensor.angle()
        # print(curhead)
        prop = (head-curhead)*p
        integral = integral + (head-curhead)*i
        diff = (head-curhead-errold)*d
        errold = head-curhead
        left_motor.dc(speed+round(prop+integral+diff))
        right_motor.dc(speed-round(prop+integral+diff))

def gyroturn(speed=50, heading=180):
    curhead=gyro_sensor.angle()
    if (curhead<heading):
        #turn right
        # robot.settings(15*speed,1000,100,1000)
        # robot.straight(distance)
        # robot.stop()
        robot.drive(0,speed)
        while curhead<heading: 
            curhead=gyro_sensor.angle()
            if heading-curhead<15:
                robot.drive(0,10)
        robot.stop()  
    elif curhead>heading:
        robot.drive(0,-speed)
        while curhead>heading: 
            curhead=gyro_sensor.angle()
            if curhead-heading<15:
                robot.drive(0,-10)
        robot.stop() 
    else: pass       

def to_wall(speed=-200, distance=-200, time_limit=5000):

    # robot.distance_control.stall_tolerances(50,200)  #13, 200
    # print(robot.distance_control.stall_tolerances())
    robot.reset()
    robot.drive(speed,0)
    tl = StopWatch()
    while not(robot.distance_control.stalled()) and abs(robot.distance())<abs(distance) and tl.time()<time_limit: pass
    robot.stop()


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
        self.__markingBlockColor=mbc if mbc in [Color.WHITE, Color.GREEN] else None

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

hospital = {
    Color.RED:   HospitalRoom(Color.RED), 
    Color.YELLOW:HospitalRoom(Color.YELLOW), 
    Color.GREEN: HospitalRoom(Color.GREEN), 
    Color.BLUE:  HospitalRoom(Color.BLUE)
}
print(hospital)
handsClosed=False
# hasRightBottle=False
hasRightBottle=True
# hasLeftBottle=False
hasLeftBottle=True
laundry_in_robot = [] #first to last
laundry_containers  = [None, None, None] # left to right

# right_motor.control.limits(1500,5000,100)
# left_motor.control.limits(1500,5000,100)
hand_motor.control.limits(1500,5000,100)
gate_motor.control.limits(1000,5000,100)

# robot.distance_control.pid(150,200,1,17,4,20)
# robot.distance_control.limits(1500,6144,100)

ev3.speaker.beep()
watch = StopWatch()
robot.settings(200,500,200,500)

# hand_motor.run_until_stalled(-1500,Stop.BRAKE,50)
# hand_motor.reset_angle(0)


def hand_motor_run(speed=1500,turn=90):
    hand_motor.run_until_stalled(speed,Stop.HOLD,turn)

def watch_marking_block_moving(roomID, start=0, end=100):
    #returns green, white or none
    print('marking')
    dcolors={}
    archivecolors=[]
    h=s=v=0
    c = None
    while True:
        angle=robot.distance()
        if angle>start:
            h,s,v=rgb_to_hsv_tuple(hand_sensor.rgb())
            if v>3:
                if 180<h<250:
                    c = Color.WHITE
                else:
                    c = Color.GREEN 
            else:
                if s>50:
                    if 110<h<170:
                        c = Color.GREEN
                    elif 170<=h<250:
                        c = Color.WHITE
                    else:
                        c = None
                else: 
                    c = None

            archivecolors.append((angle,c,h,s,v))
            if c in dcolors:
                dcolors[c]+=1
            else:
                dcolors[c]=1
        if angle>=end: break
    print('------------')
    print(dcolors)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors)>0 else None
    print('marking in',roomID, 'color is', c )
    global hospital
    hospital[roomID].markingBlockColor = None if c not in [Color.WHITE, Color.GREEN] else c


def watch_marking_block(roomID, start=0, end=100):
    #returns green, white or none
    print('marking')
    dcolors={}
    archivecolors=[]
    h=s=v=0
    c = None
    while len(archivecolors)<11:
        # angle=robot.distance()
        # if angle>start:
        h,s,v=rgb_to_hsv_tuple(hand_sensor.rgb())
        if v>3:
            if 180<h<250:
                c = Color.WHITE
            else:
                c = Color.GREEN 
        else:
            if s>50:
                if 110<h<170:
                    c = Color.GREEN
                elif 170<=h<250:
                    c = Color.WHITE
                else:
                    c = None
            else: 
                c = None

        archivecolors.append((c,h,s,v))
        if c in dcolors:
            dcolors[c]+=1
        else:
            dcolors[c]=1
        # if angle>=end: break
    print('------------')
    print(dcolors)
    print(archivecolors)
    c= max(dcolors,key=dcolors.get) if len(dcolors)>0 else None
    print('marking in',roomID, 'color is', c )
    global hospital
    hospital[roomID].markingBlockColor = None if c not in [Color.WHITE, Color.GREEN] else c

def watch_laundry_block(roomID, learn=True):
    # returns red, yellow, black or None
    dcolors={}
    archivecolors=[]
    h=s=v=0
    c = None
    while len(archivecolors)<11:
        h,s,v=rgb_to_hsv_tuple(hand_sensor.rgb())
        if s>60:
            if 25<h<65:
                c = Color.YELLOW
            elif 330<h<360 or 0<=h<=25:
                c = Color.RED
            else:
                c = Color.BLACK
        else:
            if v>3 and 200<h<250:
                c = None
            elif (h==0 and s==0) or s>30:
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
    c= max(dcolors,key=dcolors.get) if len(dcolors)>0 else None
    print('laundry in ', roomID, 'color is', c )
    if learn:
        global hospital
        hospital[roomID].laundryBlockColor = None if c not in [Color.RED, Color.YELLOW, Color.BLACK] else c
        return hospital[roomID].laundryBlockColor
    else:
        return None if c not in [Color.RED, Color.YELLOW, Color.BLACK] else c




def getBottles():
    # # start
    # pid_sensors(p=2,i=0.0005,d=5,targetposition=0)
    rs=right_sensor.reflection()
    t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
    gate_motor.reset_angle(0)
    robot.reset()
    robot.drive(-200,-48) #-200, -48
    while robot.angle()>-43: pass

    robot.reset()
    robot.drive(-200,0)
    while robot.distance()>-130: pass
    robot.drive(-100,0)
    while robot.distance()>-185: pass #185
    t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
    while robot.distance()>-245: pass #185
    rstop()
    hand_motor.reset_angle(0)

    robot.turn(-52) #-55
    
    rstop()
    # wait(400) #rr

    robot.reset()
    robot.drive(400,0)
    while robot.distance()<200: pass

    while right_sensor.reflection()>20: pass

    while right_sensor.reflection()<45: pass

    while right_sensor.reflection()>20: pass

    while right_sensor.reflection()<45: pass

   

    robot.reset()
    robot.drive(200,0)
    while robot.distance()<50: pass
    robot.stop()
    # robot.straight(50)
    # wait(1000)
    robot.turn(-40) #-43

def toRedRoom():
    # to room
    gate_motor.reset_angle(-180)
    pid_to_X(speed=200,p=0.3,i=0.0005,d=5,stoplevel=40)
    robot.reset()
    robot.drive(100,0)
    while robot.distance()<57: pass
    rstop()
    robot.settings(300,1000,300,1000)
    robot.turn(-90)

def RedOrBlueRoom(roomColor):
    # # room
    global hasRightBottle
    global hasLeftBottle
    global laundry_in_robot


    t = _thread.start_new_thread(hand_motor.run_target, (1500, 100))

    pid_to_X(speed=-100,p=0,i=0,d=0,stoplevel=40)

    gate_motor.reset_angle(-180)
    robot.reset()
    pid_left_in_to_motor(speed=100,p=0.3,i=0.0005,d=5,distance=115,bw=40)
    rstop()
    watch_marking_block(roomColor,5,30);
    # wait(5000)
    # robot.reset()
    # robot.drive(70,0)
    # t = _thread.start_new_thread(watch_marking_block,(roomColor,5,30))
    # while robot.distance()<30: pass
    # robot.drive(150,0)
    # while robot.distance()<100: pass
    # rstop()
    # hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
    # print('laundry is',current_laundry)
    # while hospital[roomColor].markingBlockColor==Color.PURPLE: pass
    # not (hand_motor.angle()>255 or current_laundry==None)

    #laundry block in hands 
    #we need to get laundry block inside
    if hospital[roomColor].markingBlockColor==Color.WHITE:
        #bottle
        pid_left_in_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=40,bw=40)

        robot.reset()
        robot.drive(70,0)
        while robot.distance()<45: pass
        rstop()
        
        hand_motor.run_until_stalled(1500,Stop.HOLD,70)
        # wait(4000) # rr

        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        while hospital[roomColor].markingBlockColor==Color.PURPLE: pass
        if hasRightBottle:
            gate_motor.run_target(1500,-270)
        else:
            gate_motor.run_target(1500,-90)
        robot.straight(54)
        robot.reset()
        gate_motor.run_target(1500,-180)
        robot.drive(600,140)
        while robot.angle()<169: pass # 171
        rstop()
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
        if current_laundry == None:
            robot.straight(120)
        else:
            gate_motor.run_target(1500,180)
            robot.straight(120)
            gate_motor.run_target(1500,-180)
            laundry_in_robot.append(current_laundry)
        robot.reset()
        robot.drive(50,250)
        while robot.angle()<76: pass
        rstop()
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<(50 + int(not hasRightBottle)*95): pass
        rstop()
        robot.reset()
        robot.drive(-100,0)
        while robot.distance()>-15: pass #back to get bottle
        rstop()
        # robot.straight(40 + int(not hasRightBottle)*90)
        hand_motor.run_until_stalled(1500,Stop.HOLD,80)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-50-int(not hasRightBottle)*95: pass
        while right_sensor.reflection()>15: pass
        rstop()
        gate_motor.run_target(1500,180*7)
        robot.turn(105)  # 110
        robot.straight(110)
        # gate_motor.run_target(1500,180*6)
        # hand_motor.run_target(1500,200)
        # wait(10)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,50)
        robot.turn(-20)
        robot.straight(-110)
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-50: pass
        while right_sensor.reflection()>30: pass
        rstop()
        robot.reset()
        robot.drive(300,-180)
        while robot.angle()>-80: pass
        rstop()
        pid_to_motor(speed=150,p=0.5,i=0.0005,d=5,distance=150)
        pid_to_X(speed=150,p=0.5,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(150,0)
        while robot.distance()<45: pass
        rstop()
        robot.turn(-90)
        if hasRightBottle: 
            hasRightBottle = False
        else:
            hasLeftBottle = False 


    else:
        #basketball
        # robot.straight(-35)
        t = _thread.start_new_thread(hand_motor_run,(1500,65))
        wait(200)
        robot.turn(-60)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        wait(200)
        robot.turn(60)
        robot.straight(95)
        hand_motor.run_until_stalled(1500,Stop.HOLD,65)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        robot.stop()
        robot.settings(700,500,700,1000)
        robot.reset()
        if current_laundry == None:
            t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
            robot.straight(165)
            rstop()
        else:
            t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
            gate_motor.run_target(1500,180)
            robot.straight(165)
            rstop()
            laundry_in_robot.append(current_laundry)
        t = _thread.start_new_thread(hand_motor.run_target,(1000,120))
        gate_motor.run_target(1500,180*3)
        robot.settings(300,300,100,300)
        robot.straight(35)
        rstop()
        robot.settings(700,800,700,1000)
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.HOLD,70))
        gate_motor.run_target(1500,180*7)
        robot.turn(70)
        robot.straight(240)
        # gate_motor.run_target(1500,180*6)
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
        robot.straight(-235)
        gate_motor.run_target(1500,-180)
        robot.turn(107)
        # robot.straight(210)
        robot.reset()
        robot.drive(350,0)
        while robot.distance()<100: pass
        robot.drive(300,0)
        while robot.distance()<130: pass
        robot.drive(250,0)
        while robot.distance()<170: pass
        pid_to_X(speed=200,p=0.9,i=0.0005,d=20,stoplevel=40)
        pid_to_motor(speed=150,p=0.6,i=0.0005,d=20,distance=50)
        rstop()

def GreenOrYellowRoom(roomColor):
    # # room
    global hasRightBottle
    global hasLeftBottle
    global laundry_in_robot

    t = _thread.start_new_thread(hand_motor.run_target, (1500, 100))

    pid_to_X(speed=-100,p=0,i=0,d=0,stoplevel=40)

    gate_motor.reset_angle(-180)
    robot.reset()
    pid_right_in_to_motor(speed=100,p=0.3,i=0.0005,d=5,distance=115,bw=40)
    rstop()
    watch_marking_block(roomColor,5,30)
    # pid_right_in_to_motor(speed=100,p=0.3,i=0.0005,d=5,distance=52,bw=40)
    # robot.reset()
    # robot.drive(70,0)
    # t = _thread.start_new_thread(watch_marking_block,(roomColor,5,30))
    # while robot.distance()<30: pass
    # robot.drive(150,0)
    # while robot.distance()<100: pass
    # rstop()
    # hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
    # print('laundry is',current_laundry)
    # while hospital[roomColor].markingBlockColor==Color.PURPLE: pass
    # not (hand_motor.angle()>255 or current_laundry==None)

    #laundry block in hands 
    #we need to get laundry block inside
    if hospital[roomColor].markingBlockColor==Color.WHITE:
        #bottle
        pid_left_in_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=40,bw=40)

        robot.reset()
        robot.drive(70,0)
        while robot.distance()<45: pass
        rstop()
        
        hand_motor.run_until_stalled(1500,Stop.HOLD,70)
        # wait(4000) # rr

        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        while hospital[roomColor].markingBlockColor==Color.PURPLE: pass
        if hasRightBottle:
            gate_motor.run_target(1500,-270)
        else:
            gate_motor.run_target(1500,-90)
        robot.straight(50)
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(600,-140)
        while robot.angle()>-169: pass
        rstop()
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
        if current_laundry == None:
            robot.straight(115)
        else:
            gate_motor.run_target(1500,180)
            robot.straight(115)
            gate_motor.run_target(1500,-180)
            laundry_in_robot.append(current_laundry)
        robot.reset()
        robot.drive(50,-250)
        while robot.angle()>-76: pass
        rstop()
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<(50 + int(hasRightBottle)*100): pass
        rstop()
        robot.reset()
        robot.drive(-100,0)
        while robot.distance()>-15: pass #back to get bottle
        rstop()
        hand_motor.run_until_stalled(1500,Stop.HOLD,80)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-50-int(hasRightBottle)*100: pass
        while right_sensor.reflection()>15: pass
        rstop()
        gate_motor.run_target(1500,180*7)
        robot.turn(-107)
        robot.straight(100)
        # gate_motor.run_target(1500,180*6)
        # hand_motor.run_target(1500,200)
        # wait(10)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,50)
        robot.turn(20)
        robot.straight(-100)
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-50: pass
        while right_sensor.reflection()>30: pass
        rstop()
        robot.reset()
        robot.drive(300,180)
        while robot.angle()<80: pass
        rstop()
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=150)
        pid_to_X(speed=200,p=0.3,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(200,0)
        while robot.distance()<57: pass
        rstop()
        # robot.turn(-90)
        if hasRightBottle: 
            hasRightBottle = False
        else:
            hasLeftBottle = False 


    else:
        #basketball
        t = _thread.start_new_thread(hand_motor_run,(1500,65))
        wait(200)
        robot.turn(60)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        wait(200)
        robot.turn(-60)
        robot.straight(90)
        hand_motor.run_until_stalled(1500,Stop.HOLD,65)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        robot.stop()
        robot.settings(700,500,700,1000)
        robot.reset()
        if current_laundry == None:
            t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
            robot.straight(165)
            rstop()
        else:
            t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
            gate_motor.run_target(1500,180)
            robot.straight(165)
            rstop()
            laundry_in_robot.append(current_laundry)
        t = _thread.start_new_thread(hand_motor.run_target,(1000,120))
        gate_motor.run_target(1500,180*3)
        robot.settings(300,300,100,300)
        robot.straight(35)
        rstop()
        robot.settings(700,1000,700,1000)
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.HOLD,70))
        gate_motor.run_target(1500,180*7)
        robot.turn(-70)
        robot.straight(225)
        # gate_motor.run_target(1500,180*6)
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
        robot.straight(-215)
        gate_motor.run_target(1500,-180)
        robot.turn(-111)
        # robot.straight(210)
        robot.reset()
        robot.drive(350,0)
        while robot.distance()<100: pass
        robot.drive(300,0)
        while robot.distance()<130: pass
        robot.drive(250,0)
        while robot.distance()<170: pass
        pid_to_X(speed=200,p=0.9,i=0.0005,d=20,stoplevel=40)
        pid_to_motor(speed=150,p=0.6,i=0.0005,d=20,distance=50)
        robot.turn(-90)
        rstop()


def fromGreenToBlueRoom():
    pid_to_motor(speed=150,p=0.9,i=0.0005,d=20,distance=100)
    pid_right_to_leftX(speed=300,p=0.9,i=0.0005,d=20,stoplevel=40,bw=45)
    pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=20)
    pid_right_in_to_motor(speed=300,p=0.6,i=0.0005,d=20,distance=190)
    pid_to_motor(speed=400,p=0,i=0.0000,d=0,distance=240)
    pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=100) #romb
    pid_to_X(speed=250,p=0.9,i=0.0005,d=20,stoplevel=40)
    pid_to_motor(speed=250,p=0,i=0.0000,d=0,distance=30)
    pid_to_X(speed=200,p=0.6,i=0.0005,d=20,stoplevel=40)
    robot.reset()
    robot.drive(100,0)
    while robot.distance()<57: pass
    rstop()
    robot.settings(300,1000,300,1000)
    robot.turn(-90)
    rstop()
    # pid_right_in_to_motor(speed=200,p=0.9,i=0.0005,d=20,distance=100)
    # pid_right_to_leftX(speed=300,p=0.9,i=0.0005,d=20,stoplevel=40,bw=45)
    # pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=20)
    # pid_right_in_to_motor(speed=300,p=0.6,i=0.0005,d=20,distance=190)
    # pid_to_motor(speed=400,p=0,i=0.0000,d=0,distance=340) #romb
    # pid_to_motor(speed=200,p=0.6,i=0.0005,d=20,distance=30)
    # pid_to_X(speed=350,p=0.9,i=0.0005,d=20,stoplevel=40)
    # pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=30)
    # pid_to_X(speed=200,p=0.6,i=0.0005,d=20,stoplevel=40)
    # robot.reset()
    # robot.drive(100,0)
    # while robot.distance()<57: pass
    # rstop()
    # robot.settings(300,1000,300,1000)
    # robot.turn(-90)
    # rstop()

def laundryAndFinish():
    #laundry blocks to containers
    global laundry_containers
    global laundry_in_robot
    if len(laundry_in_robot)<3:
        if laundry_in_robot==[Color.YELLOW,Color.RED] or laundry_in_robot==[Color.RED,Color.YELLOW]:
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.YELLOW,Color.BLACK] or laundry_in_robot==[Color.BLACK,Color.YELLOW]:
            laundry_in_robot.append(Color.RED)
        elif laundry_in_robot==[Color.BLACK,Color.RED] or laundry_in_robot==[Color.RED,Color.BLACK]:
            laundry_in_robot.append(Color.YELLOW)
        elif laundry_in_robot==[Color.YELLOW]:
            laundry_in_robot.append(Color.RED)
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.RED]:
            laundry_in_robot.append(Color.YELLOW)
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.BLACK]:
            laundry_in_robot.append(Color.RED)
            laundry_in_robot.append(Color.YELLOW)
        elif laundry_in_robot==[]:
            laundry_in_robot=[Color.YELLOW, Color.RED, Color.BLACK]
    
    gate_motor.reset_angle(-180)
    
    pid_to_X(speed=200,p=0.5,i=0.0005,d=10,stoplevel=35)
    t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
    pid_to_motor(speed=250,p=0.5,i=0.0005,d=10,distance=225)
    
    robot.reset()
    robot.drive(300,0)
    while robot.distance()<115: pass
    robot.reset()
    robot.drive(200,128)
    while robot.angle()<80: pass
    hand_motor.reset_angle(0)
    pid_to_X(speed=200,p=0.6,i=0.0005,d=20,stoplevel=35)
    pid_to_motor(speed=150,p=0,i=0.0000,d=0,distance=19)
    rstop()
    robot.settings(300,1000,200,1000)
    robot.turn(90)
    pid_left_out_to_motor_container(speed=150,p=0.3,i=0.0005,d=5,distance=85,bw=35,ID=1, start=20, end=75)
    # rstop()
    # wait(3000)
    pid_left_out_to_motor_container(speed=150,p=0.3,i=0.0005,d=5,distance=190,bw=35,ID=0, start=10, end=75, isStop=True)
    # t = _thread.start_new_thread(watch_container,(1,10,90))  

    # pid_left_out_to_motor(speed=50,p=0.3,i=0.0005,d=15,distance=100,bw=45)
    # rstop()
    # wait(1000)
    # t = _thread.start_new_thread(watch_container,(0,10,90))

    # pid_left_out_to_motor(speed=50,p=0.3,i=0.0005,d=15,distance=190,bw=45)
    rstop()
    t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
    gate_motor.run_target(1500,180) #maybe parallel
    robot.straight(-160)
    rstop()
    hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # print(watch_laundry_block(0, learn=False))
    # laundry_in_robot = [Color.YELLOW, Color.RED, Color.BLACK] #first to last
    # laundry_containers  = [ Color.RED,Color.YELLOW, Color.BLACK,] # left to right
    print(laundry_containers)
    
    #first block
    target_laundry=laundry_containers.index(laundry_in_robot[0])
    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-250)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        # wait(50)
        robot.turn(90)
        robot.straight(280)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==1:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-130)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        # wait(50)
        robot.turn(90)
        robot.straight(160)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()
    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-35)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,50))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        # wait(50)
        robot.turn(90)
        robot.straight(70)
        while gate_motor.angle()>200: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)
    hand_motor.run_until_stalled(1500,Stop.HOLD,70),
    # print(watch_laundry_block(1, learn=False))

    #second block
    # target_laundry = 2
    target_laundry=laundry_containers.index(laundry_in_robot[1])
    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-275)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,120))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        # wait(50)
        robot.turn(90)
        robot.straight(310)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==1:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-165)
        while gate_motor.angle()<180*4: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,120))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        # wait(50)
        robot.turn(90)
        robot.straight(200)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()
    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-70)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        # t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        
        robot.turn(90)
        robot.straight(110)
        while gate_motor.angle()>200: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)
    hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # print(watch_laundry_block(2, learn=False))

    #third block
    # target_laundry = 2
    target_laundry=laundry_containers.index(laundry_in_robot[2])
    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-305)
        while gate_motor.angle()<180*4: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-190: pass
        
        robot.reset()
        robot.drive(-200,-125)
        while robot.angle()>-37: pass
        
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,70))
        while gate_motor.angle()>-170: rstop()
        robot.reset()
        robot.drive(-200,0)
        while right_sensor.reflection()<45 and robot.distance()>-40: print("refl", right_sensor.reflection(), "dist", robot.distance())
        # while right_sensor.reflection()<45 and robot.distance()>-40: pass
        robot.reset()
        while robot.distance()>-63: pass
        rstop()
        # robot.turn(90)
        # robot.straight(-95)
        
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==1:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-210)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        # wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-200: pass
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,50))
        while robot.distance()>-310: pass
        rstop()
        robot.turn(-45)
        robot.straight(120)
        while gate_motor.angle()>-150: pass
        robot.reset()
        robot.drive(-200,0)
        # while right_sensor.reflection()<45 or robot.distance()>-40:pass
        while right_sensor.reflection()<45 and robot.distance()>-40: print("refl", right_sensor.reflection(), "dist", robot.distance())
        robot.reset()
        while robot.distance()>-64: pass
        rstop()
        # hand_motor.run_until_stalled,(1500,Stop.BRAKE,70)
        
        
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()
    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-100)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(60)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        # wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-190: pass
        
        robot.reset()
        robot.drive(-200,125)
        while robot.angle()<42: pass
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,70))
        while gate_motor.angle()>-170: rstop()

        robot.reset()
        robot.drive(-200,0)
        while right_sensor.reflection()<45 and robot.distance()>-40: print("refl", right_sensor.reflection(), "dist", robot.distance())
        robot.reset()
        while robot.distance()>-65: pass
        rstop()
        # robot.turn(90)
        # robot.straight(-95)
        # while gate_motor.angle()>-150: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)

def laundryAndFinish2():
    #laundry blocks to containers
    global laundry_containers
    global laundry_in_robot
    if len(laundry_in_robot)<3:
        if laundry_in_robot==[Color.YELLOW,Color.RED] or laundry_in_robot==[Color.RED,Color.YELLOW]:
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.YELLOW,Color.BLACK] or laundry_in_robot==[Color.BLACK,Color.YELLOW]:
            laundry_in_robot.append(Color.RED)
        elif laundry_in_robot==[Color.BLACK,Color.RED] or laundry_in_robot==[Color.RED,Color.BLACK]:
            laundry_in_robot.append(Color.YELLOW)
        elif laundry_in_robot==[Color.YELLOW]:
            laundry_in_robot.append(Color.RED)
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.RED]:
            laundry_in_robot.append(Color.YELLOW)
            laundry_in_robot.append(Color.BLACK)
        elif laundry_in_robot==[Color.BLACK]:
            laundry_in_robot.append(Color.RED)
            laundry_in_robot.append(Color.YELLOW)
        elif laundry_in_robot==[]:
            laundry_in_robot=[Color.YELLOW, Color.RED, Color.BLACK]

    gate_motor.reset_angle(-180)

    gate_motor.run_target(1500,0)

    pid_to_X(speed=200,p=0.5,i=0.0005,d=10,stoplevel=35)
    t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
    gate_motor.run_target(1500,-180)
    pid_to_motor(speed=250,p=0.5,i=0.0005,d=10,distance=225)
    
    robot.reset()
    robot.drive(300,0)
    while robot.distance()<115: pass
    robot.reset()
    robot.drive(200,128)
    while robot.angle()<80: pass
    hand_motor.reset_angle(0)
    pid_to_X(speed=200,p=0.6,i=0.0005,d=20,stoplevel=35)
    pid_to_motor(speed=150,p=0,i=0.0000,d=0,distance=19)
    rstop()
    robot.settings(300,1000,200,1000)
    robot.turn(90)
    pid_left_out_to_motor_container(speed=150,p=0.3,i=0.0005,d=5,distance=85,bw=35,ID=1, start=20, end=75)
    # rstop()
    # wait(3000)
    pid_left_out_to_motor_container(speed=150,p=0.3,i=0.0005,d=5,distance=190,bw=35,ID=0, start=10, end=75, isStop=True)
    # t = _thread.start_new_thread(watch_container,(1,10,90))  

    # pid_left_out_to_motor(speed=50,p=0.3,i=0.0005,d=15,distance=100,bw=45)
    # rstop()
    # wait(1000)
    # t = _thread.start_new_thread(watch_container,(0,10,90))

    # pid_left_out_to_motor(speed=50,p=0.3,i=0.0005,d=15,distance=190,bw=45)
    rstop()
    t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
    gate_motor.run_target(1500,180) #maybe parallel
    robot.straight(-160)
    rstop()
    hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # print(watch_laundry_block(0, learn=False))
    # laundry_in_robot = [Color.YELLOW, Color.RED, Color.BLACK] #first to last
    # laundry_containers  = [ Color.RED,Color.YELLOW, Color.BLACK,] # left to right
    print(laundry_containers)




    check = [] # its just a date check
    
    #first block
    # target_laundry=laundry_containers.index(laundry_in_robot[0])
    target_laundry=laundry_containers.index(watch_laundry_block(1, learn=False)) if hand_motor.angle()<255 else None
    check.append(target_laundry)
    
    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-250)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        wait(50)
        robot.turn(90)
        robot.straight(280)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==0:

        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-35)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,50))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        wait(50)
        robot.turn(90)
        robot.straight(70)
        while gate_motor.angle()>200: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)


        
    elif target_laundry==None:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.straight(32)

    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-130)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        wait(50)
        robot.turn(90)
        robot.straight(160)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()
    hand_motor.run_until_stalled(1500,Stop.HOLD,70),
    # print(watch_laundry_block(1, learn=False))

    #second block
    # target_laundry = 2
    # target_laundry=laundry_containers.index(laundry_in_robot[1])
    target_laundry=laundry_containers.index(watch_laundry_block(1, learn=False)) if hand_motor.angle()<255 else None
    check.append(target_laundry)

    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-275)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,120))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        wait(50)
        robot.turn(90)
        robot.straight(310)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==1:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-165)
        while gate_motor.angle()<180*4: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,120))
        wait(50)# t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        wait(50)
        robot.turn(90)
        robot.straight(200)
        while gate_motor.angle()>200: pass
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()
    elif target_laundry==None:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.straight(32)
    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-70)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        t = _thread.start_new_thread(hand_motor.run_target,(1500,150))
        # t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        
        robot.turn(90)
        robot.straight(110)
        while gate_motor.angle()>200: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)
    hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # print(watch_laundry_block(2, learn=False))

    #third block
    # target_laundry = 2
    # target_laundry=laundry_containers.index(laundry_in_robot[2])
    target_laundry=laundry_containers.index(watch_laundry_block(1, learn=False)) if hand_motor.angle()<255 else None
    check.append(target_laundry)

    if target_laundry==2:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-305)
        while gate_motor.angle()<180*4: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-190: pass
        
        robot.reset()
        robot.drive(-200,-125)
        while robot.angle()>-37: pass
        
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,70))
        while gate_motor.angle()>-170: rstop()
        robot.reset()
        robot.drive(-200,0)
        while right_sensor.reflection()<45 and robot.distance()>-40: print("refl", right_sensor.reflection(), "dist", robot.distance())
        # while right_sensor.reflection()<45 and robot.distance()>-40: pass
        robot.reset()
        while robot.distance()>-63: pass
        rstop()
        # robot.turn(90)
        # robot.straight(-95)
        
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=225,bw=30)
        # rstop()
    elif target_laundry==0:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-100)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(60)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        # wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-190: pass
        
        robot.reset()
        robot.drive(-200,125)
        while robot.angle()<42: pass
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,70))
        while gate_motor.angle()>-170: rstop()

        robot.reset()
        robot.drive(-200,0)
        while right_sensor.reflection()<45 and robot.distance()>-40: print("refl", right_sensor.reflection(), "dist", robot.distance())
        robot.reset()
        while robot.distance()>-67: pass
        rstop()
        # robot.turn(90)
        # robot.straight(-95)
        # while gate_motor.angle()>-150: pass
        # robot.straight(17)
        
        # gate_motor.run_target(1500,-180)


        
    else:
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*6))
        robot.straight(-210)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        # hand_motor.run_target(1500,150) #maybe not needed, not accurate
        # hand_motor.run_until_stalled(-1500,Stop.BRAKE,70)
        # t = _thread.start_new_thread(hand_motor.run_target,(1500,140))
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,70))
        wait(50)
        
        robot.straight(60)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
        robot.straight(-60)
        
        # wait(50)
        robot.reset()
        robot.drive(-300,0)
        while robot.distance()>-200: pass
        t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.BRAKE,50))
        while robot.distance()>-310: pass
        rstop()
        robot.turn(-45)
        robot.straight(120)
        while gate_motor.angle()>-150: pass
        robot.reset()
        robot.drive(-200,0)
        # while right_sensor.reflection()<45 or robot.distance()>-40:pass
        while right_sensor.reflection()<48 and robot.distance()>-53: print("refl", right_sensor.reflection(), "dist", robot.distance())
        robot.reset()
        while robot.distance()>-62: pass
        rstop()
        # hand_motor.run_until_stalled,(1500,Stop.BRAKE,70)
        
        
        # pid_right_out_to_motor(speed=100,p=0.3,i=0.0005,d=20,distance=120,bw=30)
        # rstop()

    print(check)



# while ev3.buttons.pressed()==[]: pass
wait(400)


# ev3.speaker.beep(250)
# wait(500)
# ev3.speaker.beep(500)
# wait(500)
# ev3.speaker.beep(1000)
wait(500)

# gate_motor.reset_angle(-180)
# gate_motor.run_target(1500,180*9)
# wait(1000)
# gate_motor.run_target(1500,180*6)
# wait(1000)
# gate_motor.run_target(1500,180*9)
# wait(1000)
# gate_motor.run_target(1500,-180)

laundry_in_robot = [Color.BLACK,Color.YELLOW,Color.RED] #first to last
getBottles()
toRedRoom()
RedOrBlueRoom(Color.RED)
GreenOrYellowRoom(Color.GREEN)
fromGreenToBlueRoom()
RedOrBlueRoom(Color.BLUE)
GreenOrYellowRoom(Color.YELLOW)
print('in robot - ', laundry_in_robot)
print(hospital)
laundryAndFinish2()

# robot.turn(-360)
print('end')


# # this 0.8s slower
# gate_motor.reset_angle(0)
# hand_motor.run_until_stalled(1500,Stop.HOLD,70)
# gate_motor.run_target(1500,180*6)
# hand_motor.run_until_stalled(-1500,Stop.HOLD,50)
# gate_motor.run_target(1500,0)

# #this 0.8s faster 
# gate_motor.reset_angle(0)
# hand_motor.run(1500)
# while hand_motor.angle()<220 and not hand_motor.stalled(): pass
# hand_motor.stop()
# t = _thread.start_new_thread(hand_motor.run_until_stalled,(1500,Stop.HOLD,70))
# gate_motor.run_target(1500,180*6)
# hand_motor.run(-1500)
# while hand_motor.angle()>0 and not hand_motor.stalled(): pass
# hand_motor.stop()
# gate_motor.run_target(1500,0)


# robot.distance_control.stall_tolerances(300,200)
# print(robot.distance_control.stall_tolerances())
# to_wall(speed=-200, distance=-200, time_limit=5000)
# robot.straight(50)

# robot.reset()
# robot.drive(-200,0)
# while robot.distance()>-130: pass
# robot.drive(-100,0)
# while robot.distance()>-205: pass #185
# rstop()
# gate_motor.run_target(1500,-180)
# robot.straight(50)
# # wait(10000)
# gate_motor.run_target(1500,0)

print(watch.time())





# gate_motor.run_target(1500,90)

# wait(2000)
# pid_sensors(p=2,i=0.0005,d=5,targetposition=3)
# pid_sensors(p=2,i=0.0005,d=5,targetposition=0)

# None - gray ground
# (120.0, 33.3, 1.17) handc= Color.BLACK
# (60.0, 50.0, 0.78) handc= Color.BLACK
# (90.0, 66.6, 1.17) handc= Color.BLACK 

#white cube
# (200.0, 35.29411764705883, 6.666666666666667) handc= Color.BLACK - center
# (192.0, 31.25, 6.274509803921569) handc= Color.BLACK
# (225.0, 48.00000000000001, 9.803921568627452) handc= Color.BLUE - beginning
# (232.0, 57.69230769230769, 10.19607843137255) handc= Color.BLUE
# (96.00000000000001, 62.5, 3.137254901960784) handc= Color.BLACK - ending
# (90.0, 75.0, 3.137254901960784) handc= Color.BLACK

#green cube
# (160.0, 60.0, 1.96078431372549) handc= Color.GREEN - center
# (140.0, 60.0, 1.96078431372549) handc= Color.BLACK
# (150.0, 80.0, 1.96078431372549) handc= Color.BLACK
# (160.0, 60.0, 1.96078431372549) handc= Color.BLACK - beginning
# (120.0, 66.66666666666666, 1.176470588235294) handc= Color.GREEN - ending, same numbers black!

#red cube
# (352.5, 88.88888888888889, 3.529411764705882) handc= Color.RED -in handsClosed
# (0.0, 88.88888888888889, 3.529411764705882) handc= Color.RED
# (348.0, 71.42857142857143, 2.745098039215686) handc= Color.RED - beginning
# (12.0, 100.0, 1.96078431372549) handc= Color.RED - ending

#yellow cube
# (38.18181818181819, 73.33333333333333, 5.88235294117647) handc= Color.BROWN - in handsClosed
# (36.0, 66.66666666666666, 5.88235294117647) handc= Color.BROWN
# (30.0, 66.66666666666666, 2.352941176470588) handc= Color.BLACK - beginning
# (45.0, 80.0, 1.96078431372549) handc= Color.BLACK
# (51.42857142857145, 87.5, 3.137254901960784) handc= Color.BLACK - ending
# (60.0, 85.71428571428571, 2.745098039215686) handc= Color.BLACK
# (60.0, 100.0, 2.745098039215686) handc= Color.BLACK

#black cube
# (210.0, 100.0, 0.784313725490196) handc= Color.BLACK
# (0, 0.0, 0.392156862745098) handc= Color.BLACK
# (240.0, 66.66666666666666, 1.176470588235294) handc= Color.BLACK
# (210.0, 100.0, 0.784313725490196) handc= Color.BLACK

#blue cube?
# (227.1428571428571, 93.33333333333334, 5.88235294117647) handc= Color.BLACK - in handsClosed
# (231.4285714285714, 93.33333333333334, 5.88235294117647) handc= Color.BLACK
# (235.0, 85.71428571428571, 5.490196078431373) handc= Color.BLACK - beginning
# (222.8571428571429, 100.0, 2.745098039215686) handc= Color.GREEN - ending
# (210.0, 100.0, 2.352941176470588) handc= Color.BLACK 

#white bottle
# (214.6153846153846, 44.82758620689656, 22.74509803921569) handc= Color.WHITE
# (216.0, 43.85964912280702, 22.35294117647059) handc= Color.WHITE
# (222.2222222222222, 49.0909090909091, 21.5686274509804) handc= Color.WHITE - beginning
# (180.0, 28.125, 12.54901960784314) handc= Color.YELLOW - ending
# (173.3333333333333, 28.125, 12.54901960784314) handc= Color.YELLOW

# red ball
# (1.538461538461547, 97.50000000000002, 15.68627450980392) handc= Color.RED 
# (3.076923076923094, 97.50000000000002, 15.68627450980392) handc= Color.RED

#blue ball
# (227.3684210526316, 79.16666666666666, 9.411764705882353) handc= Color.BLUE
# (0, 0, 0.0) handc= Color.GREEN sometimes

# empty closed hands 
# (200.0, 27.27272727272727, 4.313725490196078) handc= Color.BLACK
# (60.0, 25.0, 1.568627450980392) handc= Color.BLACK 
# (0.0, 20.0, 1.96078431372549) handc= Color.BLACK

# while True:
#     print('hand=',rgb_to_hsv_tuple(hand_sensor.rgb()),
#         'handc=',hand_sensor.color(),  
#         # ', left=',left_sensor.reflection(), 
#         # ', right =',right_sensor.reflection(), 
#         # ', side =',rgb_to_hsv_tuple(side_sensor.rgb())
#         )
#     wait(1000)


# robot.turn(-360)
# wait(10000)
#0 - opened back, closed front
#-180 - closed all
#180 - open front, closed back
#90 - closed left back, opened right back, front up but closed
#-90 - opened left back, closed right back, front lowest closed
# gate_motor.run_target(200,-90)
# wait(5000)
# gate_motor.run_target(200,0)
