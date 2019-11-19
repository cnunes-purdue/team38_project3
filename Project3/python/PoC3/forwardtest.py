import brickpi3
import time

BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D
CONVEYOR_PORT = BP.PORT_B

power = int(input("Enter Motor Power"))
t = float(input("Enter Time to run:"))
cTest = input("Do you want to test conveyor? Y or N")
try:
    BP.set_motor_power(LEFT_PORT, power)
    BP.set_motor_power(RIGHT_PORT, power)
    time.sleep(t)
    BP.set_motor_power(LEFT_PORT, 0)
    BP.set_motor_power(RIGHT_PORT, 0)
except KeyboardInterrupt:
    BP.reset_all()

if cTest == "Y":
    try:
        BP.set_motor_power(CONVEYOR_PORT, power)
        time.sleep(t)
        BP.set_motor_power(CONVEYOR_PORT, 0)
    except KeyboardInterrupt:
        BP.reset_all()