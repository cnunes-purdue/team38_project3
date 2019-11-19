# For line finder cargo integration test

import brickpi3
import grovepi
import time

# Define new variable BP for ease of use and cleaner code
BP = brickpi3.BrickPi3()

# Define variables to store port data
RIGHTMOTOR = BP.PORT_A
LEFTMOTOR = BP.PORT_D
CONVEYOR_PORT = BP.PORT_B
HALL_PORT = BP.PORT_1
RIGHTFINDER = 3
LEFTFINDER = 4
powerM = 30
powerC = 80
x = True

# Intitialize sensors
grovepi.pinMode(RIGHTFINDER, "INPUT")
grovepi.pinMode(LEFTFINDER, "INPUT")
BP.set_sensor_type(HALL_PORT, BP.SENSOR_TYPE.CUSTOM, [(BP.SENSOR_CUSTOM.PIN1_ADC)])


# Set motor power function
def setpower(port, power):
    BP.set_motor_power(port, -power)


time.sleep(5)
print("Starting")

# All functional code exists within this try statement
try:
    while True:
        try:
            leftvalue = grovepi.digitalRead(LEFTFINDER)
            rightvalue = grovepi.digitalRead(RIGHTFINDER)
        except IOError:
            print("Error")
        if x:
            try:
                value = BP.get_sensor(BP.PORT_1)[0]
                if value >= 2100:
                    time.sleep(2.25)
                    BP.set_motor_power(CONVEYOR_PORT, powerC)
                    time.sleep(3)
                    x = False
            except brickpi3.SensorError as error:
                print(error)
        if leftvalue == 1 and rightvalue == 1:
            setpower(RIGHTMOTOR, 30)
            setpower(LEFTMOTOR, 30)
            time.sleep(0.01)
        if rightvalue == 0 and leftvalue == 1:
            setpower(RIGHTMOTOR, -30)
            setpower(LEFTMOTOR, 30)
            time.sleep(0.2)
        if leftvalue == 0 and rightvalue == 1:
            setpower(RIGHTMOTOR, 30)
            setpower(LEFTMOTOR, -30)
            time.sleep(0.2)
        if leftvalue == 0 and rightvalue == 0:
            setpower(RIGHTMOTOR, -30)
            setpower(LEFTMOTOR, 30)
            time.sleep(0.2)


except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    BP.reset_all()
