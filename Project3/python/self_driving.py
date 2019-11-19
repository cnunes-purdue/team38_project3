import time
import brickpi3
import grovepi

BP = brickpi3.BrickPi3()

ULTRA = 4 # assign ultrasonic sensor port to D4
TOUCH = BP.PORT_1

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)  # Configure port 1 sensor type

# Before touch sensor is pressed, your program will be stuck in this loop
print("Press touch sensor on port 1 to run motors")
value = 0
while not value:
    try:
        value = BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        value = 0
print("Starting...")

# Main logic
d = grovepi.ultrasonicRead(ULTRA)
if d > 30:
    try:
        while d > 30:
            BP.set_motor_power(BP.PORT_A, 20)
            BP.set_motor_power(BP.PORT_D, 20)
        while d < 30 and d > 15:
            BP.set_motor_power(BP.PORT_A, 10)
            BP.set_motor_power(BP.PORT_D, 10)

        time.sleep(.2)  # hold each loop/iteration for .2 seconds
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")

elif d < 15:
    BP.set_motor_power(BP.PORT_A, 20)
    BP.set_motor_power(BP.PORT_D, 5)
    time.sleep(1)
    BP.set_motor_power(BP.PORT_A, 20)
    BP.set_motor_power(BP.PORT_D, 20)
    time.sleep(3)
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)
    print("Avoided obstacle")


# use reset_all() to return all motors and sensors to resting states
BP.reset_all()
