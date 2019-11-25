import grovepi
import time

HALL_PORT = 7


grovepi.pinMode(HALL_PORT, "INPUT")


try:
    while True:
        try:
            hallvalue = grovepi.digitalRead(HALL_PORT)
            print(hallvalue)
            time.sleep(.25)
        except IOError:
            print("Error")
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
