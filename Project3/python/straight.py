import time
import brickpi3

BP = brickpi3.BrickPi3()
LEFT = BP.PORT_A
RIGHT = BP.PORT_D
pwr = int(input("Enter Motor Power: "))

def power(port, power):
    BP.set_motor_power(port, power)

time.sleep(5)