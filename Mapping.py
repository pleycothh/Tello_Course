from djitellopy import tello
import KeyPressModel as kp
from time import sleep
import numpy as np
import cv2
import math

######## Parameters ##########
fSpeed = 117/10 # forward speed in cm/s (15cm/s)
aSpeed = 360/10 # Angular Speed Degrees/s (45c/s)
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval


#################################
x,y = 150,150
a = 0
yaw = 0


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

points = []


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    d = 0
    global yaw, x, y, a

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed


    if kp.getKey("a"):
        yv = -aspeed
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = aspeed
        yaw += aInterval


    if kp.getKey('q'):
        yv = me.land()
    if kp.getKey('e'):
        yv = me.takeoff()

    sleep(0.25) # same time of interval
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))


    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img,point,1,(0,255,0), cv2.FILLED)
        cv2.circle(img,point, 1, (0,0,255), cv2.FILLED)

    cv2.putText(img, f'({points[-1][0]-150},{points[-1][1 ]-150})cm',
                (points[-1][0]+10, points[-1][1]+30), cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)
    #print position with label

while True:
    vals = getKeyboardInput()
    print(a)
    try:
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    except:
        print('no action avilable')

    img = np.zeros((300,300,3), np.uint8) # un set integer 8
    # 2^8 = 256 = 0-255
    points.append((vals[4],vals[5]))
    drawPoints(img, points)
    cv2.imshow("output", img)
    cv2.waitKey(1)