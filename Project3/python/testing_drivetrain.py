import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
x = True
try:
    while x:
        try:
            print("Press touch sensor on port 1 to run drive-train motors")
            value = 0
            while not value:
                try:
                    value = BP.get_sensor(BP.PORT_1)
                except brickpi3.SensorError:
                    pass

            speed = 0
            adder = 1
            while value:
                try:
                    value = BP.get_sensor(BP.PORT_1)
                except brickpi3.SensorError as error:
                    print(error)
                    value = 0

                if value:
                    if speed <= -100 or speed >= 100:
                        adder = -adder
                    speed += adder
                else:
                    speed = 0
                    adder = 1

                BP.set_motor_power(BP.PORT_A + BP.PORT_D, speed)
                BP.set_motor_power(BP.PORT_B, -speed)

                try:
                    print("Encoder A: %6d B: %6d D: %6d" % (BP.get_motor_encoder(BP.PORT_A), BP.get_motor_encoder(BP.PORT_B), BP.get_motor_encoder(BP.PORT_D)))
                except IOError as error:
                    print(error)

                time.sleep(0.02)
        except KeyboardInterrupt:
            x = False

except KeyboardInterrupt:
    BP.reset_all()
