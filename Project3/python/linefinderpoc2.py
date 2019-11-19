import brickpi3
import grovepi
import time

# Define new variable BP for ease of use and cleaner code
BP = brickpi3.BrickPi3()

# Define variables to store port data
RIGHTMOTOR = BP.PORT_A
LEFTMOTOR = BP.PORT_D
RIGHTFINDER = 5
LEFTFINDER = 6

# Intitialize sensors
grovepi.pinMode(RIGHTFINDER, "INPUT")
grovepi.pinMode(LEFTFINDER, "INPUT")

# Set motor power function
def setPower(port, power):
    BP.set_motor_power(port, -power)

time.sleep(1)
print("Starting")

# All functional code exists within this try statement
try:
    while True:
        try:
            leftvalue = grovepi.digitalRead(LEFTFINDER)
            rightvalue = grovepi.digitalRead(RIGHTFINDER)
            time.sleep(0.01)
        except IOError:
            print("Error")
        if leftvalue == 0 and rightvalue == 0:
            setPower(RIGHTMOTOR, 30)
            setPower(LEFTMOTOR, 30)
            time.sleep(0.01)
        if rightvalue == 1 and leftvalue == 0:
            setPower(RIGHTMOTOR, -30)
            setPower(LEFTMOTOR, 30)
            time.sleep(0.2)
        if leftvalue == 1 and rightvalue == 0:
            setPower(RIGHTMOTOR, 30)
            setPower(LEFTMOTOR, -30)
            time.sleep(0.2)
        if leftvalue == 1 and rightvalue == 1:
            setPower(RIGHTMOTOR, -30)
            setPower(LEFTMOTOR, 30)
            time.sleep(0.2)




except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    BP.reset_all()
