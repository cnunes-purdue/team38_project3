import time
import brickpi3

BP = brickpi3.BrickPi3()
LEFT = BP.PORT_A
RIGHT = BP.PORT_D
COLOR_PORT = BP.PORT_1

BP.set_sensor_type(COLOR_PORT, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

time.sleep(5)

def power(port, power):
    BP.set_motor_power(port, power)

x = "R"
y = 0

try:
    while True:
        print("Start")
        try:
            power(LEFT, -30)
            power(RIGHT, -28)
        except IOError:
            pass

        try:
            value = BP.get_sensor(COLOR_PORT)
        except brickpi3.SensorError as error:
            print(error)

        print("value =",value)
        i = 0
        while value == 6:
            print("before: x =",x)
            if x == "R":
                if i < 14:
                    print(value)
                    print(i)
                    time.sleep(0.01)
                    power(LEFT, -45)
                    power(RIGHT, 30)
                    time.sleep(0.05)
                    i = i+1
                    x = "R"
                    print("after1: x =",x)
                    try:
                        value = BP.get_sensor(COLOR_PORT)
                    except brickpi3.SensorError as error:
                        print(error)
                elif i == 14:
                    print(value)
                    print(i)
                    time.sleep(0.01)
                    power(LEFT, 30)
                    power(RIGHT, -45)
                    time.sleep(0.05)
                    print("after2: x =",x)
                    try:
                        value = BP.get_sensor(COLOR_PORT)
                    except brickpi3.SensorError as error:
                        print(error)
                    if value != 6:
                        x = "L"
            elif x == "L":
                if i < 14:
                    print(value)
                    print(i)
                    time.sleep(0.01)
                    power(LEFT, 30)
                    power(RIGHT, -45)
                    time.sleep(0.05)
                    i = i + 1
                    x = "L"
                    print("after3: x =",x)
                    try:
                        value = BP.get_sensor(COLOR_PORT)
                    except brickpi3.SensorError as error:
                        print(error)
                elif i == 14:
                    print(value)
                    print(i)
                    time.sleep(0.01)
                    power(LEFT, -45)
                    power(RIGHT, 30)
                    time.sleep(0.05)
                    print("after4: x =",x)
                    try:
                        value = BP.get_sensor(COLOR_PORT)
                    except brickpi3.SensorError as error:
                        print(error)
                    if value != 6:
                        x = "R"




        time.sleep(0.02)

except KeyboardInterrupt:
    BP.reset_all()

