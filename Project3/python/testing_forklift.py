import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH)

x = True
try:
    while x:
        try:
            print("Press touch sensor on port 2 to run forklift motor")
            value = 0
            while not value:
                try:
                    value = BP.get_sensor(BP.PORT_2)
                except brickpi3.SensorError:
                    pass

            speed = 0
            adder = 1
            while value:
                try:
                    value = BP.get_sensor(BP.PORT_2)
                except brickpi3.SensorError as error:
                    print(error)
                    value = 0

                if value:
                    if speed <= -15 or speed >= 15:
                        adder = -adder
                    speed += adder
                else:
                    speed = 0
                    adder = 1

                BP.set_motor_power(BP.PORT_C, speed)

                try:
                    print("Encoder C: %6d" % (BP.get_motor_encoder(BP.PORT_C)))
                except IOError as error:
                    print(error)

                time.sleep(0.02)
        except KeyboardInterrupt:
            x = False

except KeyboardInterrupt:
    BP.reset_all()