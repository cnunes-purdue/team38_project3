import time
import brickpi3

BP = brickpi3.BrickPi3()
LEFT = BP.PORT_A
RIGHT = BP.PORT_D
reset = BP.reset_all()
def setMotorPower(L, R):
    BP.set_motor_power(LEFT, -L)
    BP.set_motor_power(RIGHT, -R)
    return

setMotorPower(50, 50)
time.sleep(1)

setMotorPower(-50, -50)
time.sleep(1)

setMotorPower(50, -50)
time.sleep(1)

setMotorPower(-50, 50)
time.sleep(1)

setMotorPower(100, 100)
time.sleep(1)

setMotorPower(100, 50)
time.sleep(8.1)

setMotorPower(50, -50)
time.sleep(1)

setMotorPower(0, 0)

reset
