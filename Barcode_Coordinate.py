#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank,follow_for_ms
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep
import sys

Right_Moter = OUTPUT_B
Left_Motor = OUTPUT_A
gyro = GyroSensor(INPUT_2)
#Initializing the robot 
robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
robotDrive.gyro = GyroSensor()
robotDrive.gyro.calibrate()



def Drive(distance):
    #returns what barcode it reads
    Right_Moter = OUTPUT_B
    Left_Motor = OUTPUT_A
    gyro = GyroSensor(INPUT_2)
    #Initializing the robot 
    robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
    robotDrive.gyro = GyroSensor()
    robotDrive.gyro.calibrate()
    velocity = 5.9055
    time = distance/velocity
    robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)


def coordinates(Shelving, Box):
    #Only returns the coordinate system no movement in (x,y) format
    NewCoordinates = [0,0]
    if Shelving == 'A1' or Shelving == 'B1':
        if Shelving =='A1':
            NewCoordinates = [0,9]
        else:
            NewCoordinates = [54,9]
    elif Shelving == 'A2' or Shelving == 'B2':
        if Shelving == 'A2':
            NewCoordinates = [0,33]
        else:
            NewCoordinates = [54,33]
    elif Shelving == 'C1' or Shelving == 'D1':
        if Shelving == 'C1':
            NewCoordinates = [0,57]
        else:
            NewCoordinates = [54,57]
    elif Shelving == 'C2' or Shelving == 'D2':
        if Shelving == 'C2':
            NewCoordinates = [0,81]
        else:
            NewCoordinates = [54,81]

    if (Box > 6) and (Shelving != 'C2' or Shelving != 'D2'):
        Yvalue= NewCoordinates[1] + 24
        NewCoordinates[1] =Yvalue
    
    if (Box == 2 or Box == 8):
        Xvalue = NewCoordinates[0]+6
        NewCoordinates[0] = Xvalue
    elif (Box == 3 or Box == 9):
        Xvalue = NewCoordinates[0]+12
        NewCoordinates[0] = Xvalue
    elif (Box == 4 or Box == 10 ):
        Xvalue = NewCoordinates[0]+18
        NewCoordinates[0] = Xvalue
    elif (Box == 5 or Box == 11):
        Xvalue = NewCoordinates[0] +24
        NewCoordinates[0] = Xvalue
    elif (Box == 6 or Box == 12):
        Xvalue = NewCoordinates[0] + 30
        NewCoordinates[0] = Xvalue

    Newx= NewCoordinates[0]+6
    NewCoordinates[0] = Newx

    return NewCoordinates


def barcode():
    def Drive(distance):
        #returns what barcode it reads
        Right_Moter = OUTPUT_B
        Left_Motor = OUTPUT_A
        gyro = GyroSensor(INPUT_2)
        #Initializing the robot 
        robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
        robotDrive.gyro = GyroSensor()
        robotDrive.gyro.calibrate()
        velocity = 15
        time = distance/velocity
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)

    color_sensor= ColorSensor(INPUT_4) #initilize color sesnor

    def move_until_first(): #moves to black sensor to begin
        Right_Moter = OUTPUT_B
        Left_Motor = OUTPUT_A
        robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
        while True:
            robotDrive.on(20,20)
            color=[]
            color =color_sensor.rgb
            #print("R",file=sys.stderr)
            #print(color[0],file=sys.stderr)
            #print("G",file=sys.stderr)
            #print(color[1], file=sys.stderr )
            #print("B",file=sys.stderr)
            #print(color[2], file=sys.stderr )
            #if (color_sensor.color == ColorSensor.COLOR_BLACK or color_sensor.color == ColorSensor.COLOR_WHITE):
                #break

        robotDrive.stop()
        sleep(2)



        return

    move_until_first()

    # 1 = black 0 = white
    BarcodeArray = []
    for i in range(1,4):
        if color_sensor.color == ColorSensor.COLOR_BLACK:
            BarcodeArray.append(1)
            print("Black",file=sys.stderr)
        else:
            BarcodeArray.append(0)
            print("White",file=sys.stderr)
        Drive(2)
        print('Drove', file=sys.stderr)
        sleep(1.5)
        
    if color_sensor.color == ColorSensor.COLOR_BLACK:
            BarcodeArray.append(1)
            print("Black",file=sys.stderr)
    else:
        BarcodeArray.append(0)
        print("White",file=sys.stderr)

    if BarcodeArray == [1,0,0,0] or BarcodeArray == [0,0,0,1]:
        return "Type 1"
    elif BarcodeArray == [1,0,1,0] or BarcodeArray == [0,1,0,1]:
        return "Type 2"
    elif BarcodeArray == [1,1,0,0] or BarcodeArray == [0,0,1,1]:
        return "Type 3"
    elif BarcodeArray == [1,0,0,1]:
        return "Type 4"
    else:
        return "error"

#print(barcode())
#sleep(10)
navigate=coordinates('A1', 11)
Drive(navigate[1]+3)
robotDrive.turn_degrees(SpeedPercent(10),target_angle=-86.5)
robotDrive.gyro.reset()
Drive(navigate[0]+6)
sleep(5)
Drive(90-navigate[0])
robotDrive.turn_degrees(SpeedPercent(10),target_angle=-86.5)
robotDrive.gyro.reset()
Drive(navigate[1])












