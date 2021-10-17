from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello() # set the tello library
me.connect() # connect function
print(me.get_battery())
print(me.get_temperature())

me.streamon() # turn the stream on

while True:
    img = me.get_frame_read().frame # fitch every image from drone
    img = cv2.resize(img, (360,240)) # size down the image
    cv2.imshow("Image", img) # show the img
    cv2.waitKey(1) # delay of window in 1 ms