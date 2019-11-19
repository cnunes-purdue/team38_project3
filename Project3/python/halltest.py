import time
import brickpi3

BP = brickpi3.BrickPi3()
HALLPORT = 0

BP.set_sensor_type(HALLPORT, BP.SENSOR_TYPE.NXT_MAGNETIC)


try:
    while True:
        try:
            hallvalue = BP.get_sensor(HALLPORT)
            print(hallvalue)
            time.sleep(1)
        except brickpi3.SensorError as error:
            print(error)

except KeyboardInterrupt:
    print("You pressed ctrl+C...")