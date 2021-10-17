from djitellopy import tello
from time import sleep

me = tello.Tello() # set the tello library
me.connect() # connect function
print(me.get_battery())
print(me.get_temperature())

#me.takeoff()
#me.send_rc_control(0,50,0,0) #move forward for at speed of 50
#sleep(1)

#me.send_rc_control(0,0,0,50) #turn right for at speed of 50 （45 degree)
#sleep(1)

#me.send_rc_control(0,0,0,0) # stop drone
#me.land()