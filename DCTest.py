#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f, busnum=7)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotors = [mh.getMotor(m) for m in range(1,5)]

for m in myMotors:
    # set the speed to start, from 0 (off) to 255 (max speed)
    m.setSpeed(150)
    m.run(Raspi_MotorHAT.FORWARD);
    # turn on motor
    m.run(Raspi_MotorHAT.RELEASE);


if __name__ == "__main__":

    try:

        while (True):
    	    print ("Forward! ")
            for m in myMotors:
    	        m.run(Raspi_MotorHAT.FORWARD)

    	    print ("\tSpeed up...")
	    for i in range(10,200,10):
                for m in myMotors:
	            m.setSpeed(i)
	        time.sleep(0.01)

            time.sleep(5)

	    print ("\tSlow down...")
	    for i in reversed(range(250,0,10)):
                for m in myMotors:
		    m.setSpeed(i)
	        time.sleep(0.01)

            """
	    print ("Backward! ")
	    myMotor.run(Raspi_MotorHAT.BACKWARD        

	    print ("\tSpeed up...")
	    for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)

	    print ("\tSlow down...")
	    for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)
            """

	    print ("Release")
            for m in myMotors:
	        m.run(Raspi_MotorHAT.RELEASE)
	    time.sleep(1.0)

    except KeyboardInterrupt:
        for m in myMotors:
	    m.run(Raspi_MotorHAT.RELEASE)

        print('fim')
