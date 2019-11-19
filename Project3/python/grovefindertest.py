import grovepi
import time

rightfinder = 5
leftfinder = 6

grovepi.pinMode(rightfinder, "INPUT")
grovepi.pinMode(leftfinder, "INPUT")

time.sleep(1)
print("starting")
try:
    while True:
        try:
            leftvalue = grovepi.digitalRead(leftfinder)
            print(leftvalue)
            time.sleep(.25)
            rightvalue = grovepi.digitalRead(rightfinder)
            print(rightvalue)
            time.sleep(.25)
        except IOError:
            print("Error")
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
