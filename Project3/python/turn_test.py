import brickpi3
import time

BP = brickpi3.BrickPi3()

i = 0
speed = int(input("Enter motor speed: "))
t = int(input("How long? "))
for i in range(t):
    BP.set_motor_power(BP.PORT_A, -speed)
    BP.set_motor_power(BP.PORT_D, -(speed-3))
    time.sleep(1)
    BP.reset_all()
