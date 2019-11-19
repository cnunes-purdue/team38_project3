import brickpi3
import time

BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D

t = int(input("Enter time to run: "))
power = float(input("Enter the starting power: "))

try:
    for i in range(t):
        BP.set_motor_power(LEFT_PORT, power)
        BP.set_motor_power(RIGHT_PORT, power/2 - i)
        time.sleep(0.01)
except KeyboardInterrupt:
    BP.reset_all()
