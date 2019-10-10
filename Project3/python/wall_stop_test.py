import time
import brickpi3
import grovepi

BP = brickpi3.BrickPi3()


ultrasonic_sensor_port = 7

try:
    print("before while")
    while grovepi.ultrasonicRead(ultrasonic_sensor_port) > 15:
        print("after while")
        print("Sensor: %6d Motor A: %6d  B: %6d  D: %6d" \
			% (grovepi.ultrasonicRead(ultrasonic_sensor_port), \
				BP.get_motor_encoder(BP.PORT_A), \
				BP.get_motor_encoder(BP.PORT_B), \
				BP.get_motor_encoder(BP.PORT_D)))
        BP.set_motor_power(BP.PORT_A + BP.PORT_D, 30)
        BP.set_motor_power(BP.PORT_B, -30)


except IOError as error:
	print(error)
except TypeError as error:
	print(error)
except KeyboardInterrupt:
	print("You pressed ctrl+C...")


BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_D, 0)

BP.reset_all()

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
