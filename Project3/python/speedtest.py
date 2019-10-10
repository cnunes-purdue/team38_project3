import time
import brickpi3

BP = brickpi3.BrickPi3()
LEFT = BP.PORT_A
RIGHT = BP.PORT_D
SONIC_PORT = BP.PORT_1

BP.set_sensor_type(SONIC_PORT, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

pwr = int(input("Enter Motor Power: "))

def power(port, power):
    BP.set_motor_power(port, power)

time.sleep(5)

z = []
try:
    try:
        d = BP.get_sensor(SONIC_PORT)
    except brickpi3.SensorError as error:
        print(error)
    power(LEFT, -pwr)
    power(RIGHT, -(pwr-3))
    print("set motor power")
    while d > 30:
        try:
            value1 = BP.get_sensor(SONIC_PORT)
            print("took value 1")
            time.sleep(0.1)
            value2 = BP.get_sensor(SONIC_PORT)
            print("took value 2")
            v = (value2 - value1)/0.1
            print(v)
        except brickpi3.SensorError as error:
            print(error)
        except KeyboardInterrupt():
            BP.reset_all()
except KeyboardInterrupt():
    BP.reset_all()
