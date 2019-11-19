#   For speed test, hill test, obstacle test

import brickpi3
import time

BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D

power = int(input("Enter Motor Power"))
t = float(input("Enter Time to run:"))
try:
    BP.set_motor_power(LEFT_PORT, power)
    BP.set_motor_power(RIGHT_PORT, power)
    time.sleep(t)
    BP.set_motor_power(LEFT_PORT, 0)
    BP.set_motor_power(RIGHT_PORT, 0)
except KeyboardInterrupt:
    BP.reset_all()