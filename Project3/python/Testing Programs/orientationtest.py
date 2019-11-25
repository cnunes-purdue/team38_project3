import brickpi3
import time

BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D
CONVEYOR_PORT = BP.PORT_B

powerM = int(input("Enter Motor Power: "))
powerC = int(input("Enter Conveyor Power: "))


try:
    BP.set_motor_power(LEFT_PORT, powerM)
    BP.set_motor_power(RIGHT_PORT, powerM)
    time.sleep(3)
    BP.set_motor_power(CONVEYOR_PORT, powerC)
    time.sleep(1.5)
    BP.set_motor_power(LEFT_PORT, 0)
    BP.set_motor_power(RIGHT_PORT, 0)
    BP.set_motor_power(CONVEYOR_PORT, 0)
except KeyboardInterrupt:
    BP.reset_all()
