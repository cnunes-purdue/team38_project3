import brickpi3
import time

BP = brickpi3.BrickPi3()

CONVEYOR_PORT = BP.PORT_B

power = int(input("Enter Motor Power"))
t = float(input("Enter Time to run:"))
try:
    BP.set_motor_power(CONVEYOR_PORT, power)
    time.sleep(t)
    BP.set_motor_power(CONVEYOR_PORT, 0)
except KeyboardInterrupt:
    BP.reset_all()