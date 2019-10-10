import time
import brickpi3

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH)

x = True

try:
    while x:
        try:
            print("Press touch sensor on port 1 to run drive-train motors")
            print("or press touch sensor on port 2 to run forklift motor")
            value = 0
            value1 = 0
            while not value:
                try:
                    value = BP.get_sensor(BP.PORT_1)
                except brickpi3.SensorError:
                    pass
            while not value1:
                try:
                    value = BP.get_sensor(BP.PORT_2)
                except brickpi3.SensorError:
                    pass
            while value:
                speed = 0
                adder = 1
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
                BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, speed)

                try:
                    print("Encoder A: %6d Encoder B: %6d Encoder D: %6d" % (BP.get_motor_encoder(BP.PORT_A), BP.get_motor_encoder(BP.PORT_B), BP.get_motor_encoder(BP.PORT_D)))
                except IOError as error:
                    print(error)

                time.sleep(0.02)

            while value1:
                speed = 0
                adder = 1
                try:
                    value = BP.get_sensor(BP.PORT_2)
                except brickpi3.SensorError as error:
                    print(error)
                    value = 00

                if value1:
                    if speed <= -15 or speed >=15:
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
            x= False
except KeyboardInterrupt:
    BP.reset_all()
