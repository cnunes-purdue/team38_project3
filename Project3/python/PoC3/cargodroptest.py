# For cargo drop-off test

import brickpi3
import time

BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D
CONVEYOR_PORT = BP.PORT_B
HALL_PORT = BP.PORT_1
powerM = 30
powerC = 80
x = True


BP.set_sensor_type(HALL_PORT, BP.SENSOR_TYPE.CUSTOM, [(BP.SENSOR_CUSTOM.PIN1_ADC)])
time.sleep(5)


try:
    BP.set_motor_power(LEFT_PORT, powerM)
    BP.set_motor_power(RIGHT_PORT, powerM)
    while x:
        try:
            value = BP.get_sensor(BP.PORT_1)[0]
            if value >= 2100:
                time.sleep(2.25)
                BP.set_motor_power(CONVEYOR_PORT, powerC)
                time.sleep(3)
                BP.set_motor_power(LEFT_PORT, 0)
                BP.set_motor_power(RIGHT_PORT, 0)
                BP.set_motor_power(CONVEYOR_PORT, 0)
                x = False
        except brickpi3.SensorError as error:
            print(error)


except KeyboardInterrupt:
    BP.reset_all()