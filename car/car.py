#!/usr/bin/python
import time
import math
from threading import Thread

from car.motorhat.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor


class DCMotorAbstract:

    FORWARD = Raspi_MotorHAT.FORWARD
    BACKWARD = Raspi_MotorHAT.BACKWARD
    MAXSPEED = 75


class DCMotor(Thread, DCMotorAbstract):


    def __init__(self, channel, speed=0, initialDirection=DCMotorAbstract.FORWARD, forward=DCMotorAbstract.FORWARD, backward=DCMotorAbstract.BACKWARD, maxSpeed=DCMotorAbstract.MAXSPEED, addr=0x6f, busnum=7, sleepTime=0.000001):
        Thread.__init__(self)

        self.__label = str(channel)

        self.__addr = addr
        self.__busnum = busnum
        self.__channel = channel
        self.__speed = speed
        self.__direction = initialDirection
        self.__running = True
        self.__sleepTime = sleepTime
        self.__forward = forward
        self.__backward = backward
        self.__maxSpeed = maxSpeed

        self.__motor = Raspi_MotorHAT(addr=self.__addr, busnum=self.__busnum).getMotor(channel)
        
        self.__motor.setSpeed(self.__speed)
        self.__motor.run(Raspi_MotorHAT.RELEASE)


    @property
    def FORWARD(self):
        return self.__forward


    @property
    def BACKWARD(self):
        return self.__backward


    def __turnOff(self):
        self.__motor.run(Raspi_MotorHAT.RELEASE)


    def setSpeed(self, speed=1):
        speed = math.ceil(speed*self.__maxSpeed)
        self.__speed = speed


    def setDirection(self, direction):
        self.__direction = direction


    def shutdown(self):
        self.__running = False


    def loopSet(self):
        self.__motor.setSpeed(self.__speed)
        self.__motor.run(self.__direction)


    def run(self):


        while self.__running:

            try:
                self.loopSet()

                time.sleep(self.__sleepTime)

            except KeyboardInterrupt:
                pass

            finally:
                self.__turnOff()



class Car(Thread):

    def __init__(self, addr=0x6f, busnum=7, sleepTime=0.000001):
        Thread.__init__(self)

        self.__motorDD = DCMotor(1, speed=0)
        self.__motorTD = DCMotor(2, speed=0)
        self.__motorDE = DCMotor(4, speed=0)
        self.__motorTE = DCMotor(3, speed=0)

        self.__addr = addr
        self.__busnum = busnum
        self.__sleepTime = sleepTime
        self.__running = True


    def shutdown(self):
        self.__running = False


    def loopSet(self):
        pass


    @property
    def motorDD(self):
        return self.__motorDD

    @property
    def motorDE(self):
        return self.__motorDE

    @property
    def motorTD(self):
        return self.__motorTD

    @property
    def motorTE(self):
        return self.__motorTE


    def __turnOffMotors(self):
        self.__motorDD.shutdown()
        self.__motorTD.shutdown()
        self.__motorDE.shutdown()
        self.__motorTE.shutdown()


    def run(self):
        self.__motorDD.start()
        self.__motorTD.start()
        self.__motorDE.start()
        self.__motorTE.start()

        try:

            while self.__running:

                self.loopSet()

                time.sleep(self.__sleepTime)


        except KeyboardInterrupt:
            pass

        finally:
            self.__turnOffMotors()
            print('Car is shut down')


    def stop(self):
        self.motorDD.setSpeed(0)
        self.motorTD.setSpeed(0)
        self.motorDE.setSpeed(0)
        self.motorTE.setSpeed(0)


    def moveForward(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.FORWARD)
        self.motorDE.setDirection(self.motorDE.FORWARD)
        self.motorTD.setDirection(self.motorTD.FORWARD)
        self.motorTE.setDirection(self.motorTE.FORWARD)


    def moveBackward(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.BACKWARD)
        self.motorDE.setDirection(self.motorDE.BACKWARD)
        self.motorTD.setDirection(self.motorTD.BACKWARD)
        self.motorTE.setDirection(self.motorTE.BACKWARD)


    def strafeRight(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.BACKWARD)
        self.motorDE.setDirection(self.motorDE.FORWARD)
        self.motorTD.setDirection(self.motorTD.FORWARD)
        self.motorTE.setDirection(self.motorTE.BACKWARD)


    def strafeLeft(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.FORWARD)
        self.motorDE.setDirection(self.motorDE.BACKWARD)
        self.motorTD.setDirection(self.motorTD.BACKWARD)
        self.motorTE.setDirection(self.motorTE.FORWARD)


    def rotateRight(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.BACKWARD)
        self.motorDE.setDirection(self.motorDE.FORWARD)
        self.motorTD.setDirection(self.motorTD.BACKWARD)
        self.motorTE.setDirection(self.motorTE.FORWARD)


    def rotateLeft(self):
        self.motorDD.setSpeed()
        self.motorDE.setSpeed()
        self.motorTD.setSpeed()
        self.motorTE.setSpeed()

        self.motorDD.setDirection(self.motorDD.FORWARD)
        self.motorDE.setDirection(self.motorDE.BACKWARD)
        self.motorTD.setDirection(self.motorTD.FORWARD)
        self.motorTE.setDirection(self.motorTE.BACKWARD)
