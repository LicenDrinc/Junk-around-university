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
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=122)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
side_sensor = ColorSensor(Port.S1)
hand_sensor = ColorSensor(Port.S4)
# dist_sensor = InfraredSensor(Port.S1)
# gyro_sensor = GyroSensor(Port.S1, Direction.CLOCKWISE)
hand_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
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


def watch_container(ID, start=0, end=100):
    dcolors={}
    archivecolors=[]
    hsv=()
    d=h=s=v=0
    while True:
        angle=robot.distance()
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
                    if h==0 and s<50:
                        c=Color.BLACK
                    else:
                        c=Color.RED
                elif h>=35 and h<60:
                    c=Color.YELLOW
                else: 
                    c=Color.BLACK
            elif h>=35 and h<60:
                c=Color.YELLOW
            elif (h>=0 and h<35) or h>330:
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
hasRightBottle=True
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
robot.settings(400,1000,300,1000)

# hand_motor.run_until_stalled(-1500,Stop.BRAKE,50)
# hand_motor.reset_angle(0)

def watch_marking_block(roomID, start=0, end=100):
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
                if s>=50:
                    if 110<h<202:
                        c = Color.GREEN
                    elif 202<=h<250:
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

def watch_laundry_block(roomID):
    # returns red, yellow, black or None
    dcolors={}
    archivecolors=[]
    h=s=v=0
    c = None
    while len(archivecolors)<11:
        h,s,v=rgb_to_hsv_tuple(hand_sensor.rgb())
        if s>=50:
            if 25<h<65:
                c = Color.YELLOW
            elif 330<h<360 or 0<=h<=25:
                c = Color.RED
            else:
                c = Color.BLACK
        else:
            if v>3 and 200<h<250:
                c = None
            elif (h==0 and s==0) or (s>30):
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
    global hospital
    hospital[roomID].laundryBlockColor = None if c not in [Color.RED, Color.YELLOW, Color.BLACK] else c
    return hospital[roomID].laundryBlockColor


def hand_motor_run(speed=1500,turn=90):
    hand_motor.run_until_stalled(speed,Stop.HOLD,turn)


def getBottles():
    # # start
    # pid_sensors(p=2,i=0.0005,d=5,targetposition=0)
    rs=right_sensor.reflection()
    t = _thread.start_new_thread(hand_motor.run_until_stalled,(-1500,Stop.BRAKE,50))
    gate_motor.reset_angle(0)
    robot.reset()
    robot.drive(-200,-48) #-200, -48
    while robot.angle()>-45: pass
    robot.reset()
    robot.drive(-200,0)
    while robot.distance()>-130: pass
    robot.drive(-100,0)
    while robot.distance()>-265: pass #185
    rstop()
    
    gate_motor.run_target(1500,-180)
    hand_motor.reset_angle(0)

    robot.turn(-46) #-55
    robot.reset()
    robot.drive(400,0)
    while robot.distance()<200: pass
    while right_sensor.reflection()>30: pass
    while right_sensor.reflection()<50: pass
    while right_sensor.reflection()>30: pass
    while right_sensor.reflection()<50: pass
    robot.reset()
    robot.drive(200,0)
    while robot.distance()<50: pass
    rstop()
    # robot.straight(50)
    # wait(1000)
    robot.turn(-45) #-43

def toRedRoom():
    # to room
    gate_motor.reset_angle(-180)
    pid_to_X(speed=200,p=0.3,i=0.0005,d=5,stoplevel=40)
    robot.reset()
    robot.drive(100,0)
    while robot.distance()<57: pass
    rstop()
    robot.settings(350,1000,300,1000)
    robot.turn(-90)

def RedOrBlueRoom(roomColor):
    # # room
    global hasRightBottle
    global hasLeftBottle
    global laundry_in_robot
    robot.reset()
    pid_left_in_to_motor(speed=100,p=0.3,i=0.0005,d=5,distance=52,bw=40)
    robot.reset()
    robot.drive(70,0)
    t = _thread.start_new_thread(watch_marking_block,(roomColor,10,35))
    while robot.distance()<30: pass
    robot.drive(150,0)
    while robot.distance()<105: pass
    rstop()
    while hospital[roomColor].markingBlockColor==Color.PURPLE: pass

    # hand_motor.run_until_stalled(1500,Stop.HOLD,65)
    # current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
    # print('laundry is',current_laundry)
    # if current_laundry!=None:
    #     laundry_in_robot.append(current_laundry)
    
    # not (hand_motor.angle()>255 or current_laundry==None)

    #laundry block in hands 
    #we need to get laundry block inside
    if hospital[roomColor].markingBlockColor==Color.WHITE:
        #bottle
        hand_motor.run_until_stalled(1500,Stop.HOLD,65)
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        if current_laundry!=None:
            laundry_in_robot.append(current_laundry)
        rstop()
        if hasLeftBottle == True and hasRightBottle == False: gate_motor.run_target(1500,-90)
        else: gate_motor.run_target(1500,90*5)

        robot.straight(50)
        robot.reset()
        robot.drive(200,115)
        while robot.angle()<175 : pass
        rstop()
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        gate_motor.run_target(1500,90*2)
        robot.straight(170)
        gate_motor.run_target(1500,-180)
        robot.straight(-35)
        robot.turn(90)
        
        if hasLeftBottle == True and hasRightBottle == False: robot.straight(180)
        else: robot.straight(100)
        
        robot.straight(-15)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        
        robot.turn(140)
        
        gate_motor.run_target(1500,1260)
        
        if hasLeftBottle==True and hasRightBottle==False: robot.straight(250)
        else: robot.straight(170)
        
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        robot.straight(-30)
        
        robot.turn(-50)
        
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-57: pass
        while right_sensor.reflection()>25: pass
        rstop()
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()
        robot.turn(-90)
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=100)
        rstop()
        pid_to_X(speed=150,p=0.3,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<45: pass
        rstop()
        robot.turn(-90)
        if hasLeftBottle==True and hasRightBottle==False: hasLeftBottle=False
        else: hasRightBottle=False
    else:
        #basketball
        robot.straight(-30)
        t = _thread.start_new_thread(hand_motor_run,(1500,65))
        wait(200)
        robot.turn(-60)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        wait(200)
        robot.turn(60)
        robot.straight(35)
        hand_motor.run_until_stalled(1500,Stop.HOLD,65)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        if current_laundry!=None:
            laundry_in_robot.append(current_laundry)
            gate_motor.run_target(1500,180)
            rstop()
            robot.settings(100,1000,300,1000)
            robot.straight(135)
            gate_motor.run_target(1500,530)
            robot.straight(60)
            t = _thread.start_new_thread(hand_motor_run,(1500,90))
            rstop()
            wait(250)
        else:
            rstop()
            robot.settings(100,1000,300,1000)
            gate_motor.run_target(1500,530)
            robot.straight(60+135)
            t = _thread.start_new_thread(hand_motor_run,(1500,90))
            rstop()
            wait(250)
        robot.settings(400,1000,300,1000)
        robot.straight(-110)
        gate_motor.run_target(1500,1260)
        robot.straight(30)
        robot.turn(60)
        robot.straight(260)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        robot.straight(-100)
        robot.turn(-60)
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-327: pass
        while left_sensor.reflection()>25: pass
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()
        robot.turn(-90)
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=50)
        rstop()
        pid_to_X(speed=150,p=0.3,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<45: pass
        rstop()
        robot.turn(-90)        

def GreenOrYellowRoom(roomColor):
    # # room
    global hasRightBottle
    global hasLeftBottle
    global laundry_in_robot
    gate_motor.reset_angle(-180)
    robot.reset()
    pid_right_in_to_motor(speed=100,p=0.3,i=0.0005,d=5,distance=52,bw=40)
    robot.reset()
    robot.drive(70,0)
    t = _thread.start_new_thread(watch_marking_block,(roomColor,10,35))
    while robot.distance()<30: pass
    robot.drive(150,0)
    while robot.distance()<105: pass
    rstop()
    # hand_motor.run_until_stalled(1500,Stop.HOLD,70)
    # current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
    # print('laundry is',current_laundry)
    # if current_laundry!=None:
    #     laundry_in_robot.append(current_laundry)
    while hospital[roomColor].markingBlockColor==Color.PURPLE: pass
    # not (hand_motor.angle()>255 or current_laundry==None)

    #laundry block in hands 
    #we need to get laundry block inside
    if hospital[roomColor].markingBlockColor==Color.WHITE:
        #bottle
        hand_motor.run_until_stalled(1500,Stop.HOLD,70)
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        if current_laundry!=None:
            laundry_in_robot.append(current_laundry)
        rstop()
        if hasLeftBottle == False and hasRightBottle == True: gate_motor.run_target(1500,90*5)
        else: gate_motor.run_target(1500,-90)

        robot.straight(50)
        robot.reset()
        robot.drive(200,-110)
        while robot.angle()>-175 : pass
        rstop()
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        gate_motor.run_target(1500,90*2)
        robot.straight(200)
        gate_motor.run_target(1500,-180)
        robot.straight(-60)
        robot.turn(-90)
        
        if hasLeftBottle == False and hasRightBottle == True: robot.straight(180)
        else: robot.straight(105)
        
        robot.straight(-15)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        
        robot.turn(-140)
        
        gate_motor.run_target(1500,1260)
        
        if hasLeftBottle==False and hasRightBottle==True: robot.straight(250)
        else: robot.straight(170)
        
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        robot.straight(-30)
        
        robot.turn(50)
        
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-57: pass
        while left_sensor.reflection()>25: pass
        rstop()
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()
        robot.turn(90)
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=100)
        rstop()
        pid_to_X(speed=150,p=0.3,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()
        if hasLeftBottle==False and hasRightBottle==True: hasRightBottle=False
        else: hasLeftBottle=False
        pass
    else:
        #basketball
        robot.straight(-30)
        t = _thread.start_new_thread(hand_motor_run,(1500,65))
        wait(200)
        robot.turn(60)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        wait(200)
        robot.turn(-60)
        robot.straight(40)
        hand_motor.run_until_stalled(1500,Stop.HOLD,65)
        t = _thread.start_new_thread(hand_motor_run,(-1500,65))
        current_laundry = watch_laundry_block(roomColor) if hand_motor.angle()<255 else None
        print('laundry is',current_laundry)
        if current_laundry!=None:
            laundry_in_robot.append(current_laundry)
            gate_motor.run_target(1500,180)
            rstop()
            robot.settings(100,1000,300,1000)
            robot.straight(135)
            gate_motor.run_target(1500,530)
            robot.straight(60)
            t = _thread.start_new_thread(hand_motor_run,(1500,90))
            rstop()
            wait(250)
        else:
            rstop()
            robot.settings(100,1000,300,1000)
            gate_motor.run_target(1500,530)
            robot.straight(60+135)
            t = _thread.start_new_thread(hand_motor_run,(1500,90))
            rstop()
            wait(250)
        robot.settings(400,1000,300,1000)
        robot.straight(-90)
        gate_motor.run_target(1500,1260)
        robot.straight(30)
        robot.turn(-65)
        robot.straight(260)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        robot.straight(-100)
        robot.turn(65)
        gate_motor.run_target(1500,-180)
        robot.reset()
        robot.drive(-200,0)
        while robot.distance()>-327: pass
        while right_sensor.reflection()>25: pass
        rstop()
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()
        robot.turn(90)
        pid_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=50)
        rstop()
        pid_to_X(speed=150,p=0.3,i=0.0005,d=5,stoplevel=40)
        robot.reset()
        robot.drive(100,0)
        while robot.distance()<50: pass
        rstop()

def fromGreenToBlueRoom():
    pid_right_in_to_motor(speed=300,p=0.9,i=0.0005,d=20,distance=100)
    pid_right_to_leftX(speed=300,p=0.9,i=0.0005,d=20,stoplevel=40)
    pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=20)
    pid_right_in_to_motor(speed=300,p=0.6,i=0.0005,d=20,distance=190)
    pid_to_motor(speed=400,p=0,i=0.0000,d=0,distance=340) #romb
    pid_to_X(speed=350,p=0.9,i=0.0005,d=20,stoplevel=40)
    pid_to_motor(speed=300,p=0,i=0.0000,d=0,distance=50)
    pid_to_X(speed=300,p=0.6,i=0.0005,d=20,stoplevel=40)
    robot.reset()
    robot.drive(100,0)
    while robot.distance()<57: pass
    rstop()
    robot.settings(400,1000,300,1000)
    robot.turn(-90)
    rstop()

def Finish():
    global laundry_containers
    global laundry_in_robot
    pid_to_X(speed=250,p=0.3,i=0.0005,d=5,stoplevel=40)
    pid_to_motor(speed=250,p=0.3,i=0.0005,d=5,distance=250)
    robot.reset()
    robot.drive(200,65)
    while robot.angle()<90: pass
    rstop()
    pid_to_motor(speed=250,p=0.3,i=0.0005,d=5,distance=100)
    robot.reset()
    robot.drive(200,0)
    while left_sensor.reflection()>25: pass
    while right_sensor.reflection()>25: pass
    rstop()
    robot.straight(16)
    robot.turn(90)
    t = _thread.start_new_thread(watch_container,(1, 0, 110))
    t = _thread.start_new_thread(watch_container,(0, 120, 180))
    pid_left_out_to_motor(speed=150,p=0.3,i=0.0005,d=5,distance=320,bw=55)
    rstop()
    gate_motor.run_target(1500,180)
    print('finish!', laundry_containers, ' in robot:', laundry_in_robot )
    if laundry_containers[0]==laundry_in_robot[0]:
        robot.straight(-165)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*7+90))
        robot.straight(-50)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)
    elif laundry_containers[0]==laundry_in_robot[1]:
        robot.straight(-130)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        rstop()
        robot.settings(100,1000,300,1000)
        robot.straight(-40)
        gate_motor.run_target(1500,180*7-90)
        robot.straight(35)
        rstop()
        robot.settings(400,1000,300,1000)
        robot.straight(-80)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)
    else:
        robot.straight(-100)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        robot.straight(95)
        gate_motor.run_target(1500,180*7+90)
        robot.straight(-215)
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)
    
    while gate_motor.angle()>200: pass

    if laundry_containers[2]==laundry_in_robot[0]:
        robot.straight(50)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*7+90))
        robot.straight(-250)
        while gate_motor.angle()<180*3: pass
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)
    elif laundry_containers[2]==laundry_in_robot[1]:
        robot.straight(85)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        rstop()
        robot.settings(100,1000,300,1000)
        robot.straight(-40)
        gate_motor.run_target(1500,180*7-90)
        robot.straight(35)
        rstop()
        robot.settings(400,1000,300,1000)
        robot.straight(-280)
        while gate_motor.angle()<180*3:pass
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)
    else:
        robot.straight(120)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        robot.straight(95)
        gate_motor.run_target(1500,180*7+90)
        robot.straight(-415)
        robot.turn(-90)
        hand_motor.run_until_stalled(-1500,Stop.BRAKE,65)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180))
        robot.turn(90)

    while gate_motor.angle()>200: pass

    if laundry_containers[1]==laundry_in_robot[0]:
        robot.straight(235)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*7+90))
        robot.straight(-150)
    elif laundry_containers[1]==laundry_in_robot[1]:
        robot.straight(270)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*7-90))
        robot.straight(-185)
    else:
        robot.straight(310)
        hand_motor.run_until_stalled(1500,Stop.HOLD,90)
        t = _thread.start_new_thread(gate_motor.run_target,(1500,180*7+90))
        robot.straight(-220)
    
    while gate_motor.angle()<180*3:pass
    robot.turn(-90)
    
    t = _thread.start_new_thread(hand_motor_run,(-1500,65))    
    wait(250)


    robot.straight(70)
    robot.straight(-100)
    robot.turn(180)
    t = _thread.start_new_thread(gate_motor.run_target,(1500,-180))
    pid_to_motor(speed=250,p=0.3,i=0.0005,d=5,distance=100)
    t = _thread.start_new_thread(hand_motor_run,(1500,65))
    robot.straight(200)
    gate_motor.run_target(1500,-180)
    rstop()
    wait(100)
    robot.turn(-45)
    robot.reset()
    robot.drive(100,0)
    while robot.distance()<20: pass
    while right_sensor.reflection()>25: pass
    robot.reset()
    robot.drive(-150,0)
    while robot.distance()>-80: pass
    rstop()

# gate_motor.reset_angle(-180)
# gate_motor.run_target(1500,980)
# wait(10000)
# gate_motor.reset_angle(-180)

while ev3.buttons.pressed()==[]: pass

wait(400)

# laundry_in_robot=[Color.YELLOW,Color.BLACK,Color.RED]

getBottles()
toRedRoom()
RedOrBlueRoom(Color.RED)
GreenOrYellowRoom(Color.GREEN)
fromGreenToBlueRoom()
RedOrBlueRoom(Color.BLUE)
GreenOrYellowRoom(Color.YELLOW)
Finish()

gate_motor.run_target(1500,-180)

# laundry_in_robot = [Color.YELLOW, Color.RED, Color.BLACK] #first to last