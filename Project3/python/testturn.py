import time
import brickpi3
import linefindertest

BP = brickpi3.BrickPi3()
LEFT = BP.PORT_A
RIGHT = BP.PORT_D


pwr = int(input("Enter turn power"))

linefindertest.power(LEFT, -pwr)
linefindertest.power(RIGHT, pwr)