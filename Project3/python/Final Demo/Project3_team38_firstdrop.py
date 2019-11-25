# Project 3 Final Demonstration: First Cargo Drop.
# File: Project3_team38_firstdrop.py
# Date: 25 November 2019
# By: Cohen Nunes
# cnunes
# Kyra Kennan
# Login ID
# Gabby Nyce
# Login ID
# Lee Ault
# Login ID
# Section: 3
# Team: 38
#
# ELECTRONIC SIGNATURE
# Cohen Thomas Vestal Nunes
# Full Name team member 2
# Full Name team member 3
# Full Name team member 4
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES
#           This program instructs the MACRO to follow a line through the course and drop off cargo at point 'A'.
# ---------------------------------------------------
#  Imports
# ---------------------------------------------------
import time
import brickpi3
import grovepi

# ---------------------------------------------------
#  Define Variables
# ---------------------------------------------------
BP = brickpi3.BrickPi3()
RIGHTMOTOR_PORT = BP.PORT_A
LEFTMOTOR_PORT = BP.PORT_D
CONVEYOR_PORT = BP.PORT_B
HALL_PORT = BP.PORT_1
SONIC_PORT = 2
RIGHTLINE_PORT = 3
LEFTLINE_PORT = 4
powerMotor = 50
powerConveyor = 80
x = 0  # Trigger for determining if cargo has been dropped

# ---------------------------------------------------
#  Initialize Sensors
# ---------------------------------------------------
grovepi.pinMode(RIGHTLINE_PORT, "INPUT")
grovepi.pinMode(LEFTLINE_PORT, "INPUT")
BP.set_sensor_type(HALL_PORT, BP.SENSOR_TYPE.CUSTOM, [BP.SENSOR_CUSTOM.PIN1_ADC])


# ---------------------------------------------------
#  Define Functions
# ---------------------------------------------------

def setpower(port, power):
    BP.set_motor_power(port, -power)


# ---------------------------------------------------
#  Warm-Up
# ---------------------------------------------------
time.sleep(5)
print("Starting")

# ---------------------------------------------------
#  Main Logic
# ---------------------------------------------------
try:
    while x != 3:
        try:
            sonicvalue = grovepi.ultrasonicRead(SONIC_PORT)
        except IOError:
            print("Error")
        try:
            if sonicvalue >= 25:
                if x != 2:
                    try:
                        # Read and store line finder values
                        leftvalue = grovepi.digitalRead(LEFTLINE_PORT)
                        rightvalue = grovepi.digitalRead(RIGHTLINE_PORT)
                    except IOError:
                        print("Error")

                    # ---------------------------------------------------
                    #  Beacon Locating
                    # ---------------------------------------------------
                    if x == 0:  # Check hall sensor when the first beacon has not been passed.
                        try:
                            # Read and store hall sensor value
                            value = BP.get_sensor(HALL_PORT)[0]
                            if value >= 2100:
                                setpower(LEFTMOTOR_PORT, 15)
                                setpower(RIGHTMOTOR_PORT, 60)
                                time.sleep(1.5)
                                x = x + 1
                        except brickpi3.SensorError as error:
                            print(error)

                    if x == 1:  # Check hall sensor when cargo has not been dropped off, after the first beacon.
                        try:
                            # Read and store hall sensor value
                            value = BP.get_sensor(HALL_PORT)[0]
                            if value >= 2100:
                                setpower(RIGHTMOTOR_PORT, powerMotor)
                                setpower(LEFTMOTOR_PORT, powerMotor)
                                time.sleep(0.75)
                                setpower(CONVEYOR_PORT, powerConveyor)
                                time.sleep(1.5)
                                x = x + 1
                        except brickpi3.SensorError as error:
                            print(error)

                    # ---------------------------------------------------
                    #  Line Following
                    # ---------------------------------------------------
                    try:
                        if leftvalue == 1 and rightvalue == 1:
                            setpower(RIGHTMOTOR_PORT, 30)
                            setpower(LEFTMOTOR_PORT, 30)
                            time.sleep(0.01)
                        if rightvalue == 0 and leftvalue == 1:
                            setpower(RIGHTMOTOR_PORT, -30)
                            setpower(LEFTMOTOR_PORT, 30)
                            time.sleep(0.1)
                        if leftvalue == 0 and rightvalue == 1:
                            setpower(RIGHTMOTOR_PORT, 30)
                            setpower(LEFTMOTOR_PORT, -30)
                            time.sleep(0.1)
                        if leftvalue == 0 and rightvalue == 0:
                            setpower(RIGHTMOTOR_PORT, -30)
                            setpower(LEFTMOTOR_PORT, 30)
                            time.sleep(0.01)
                    except NameError:
                        pass

                # ---------------------------------------------------
                #  Stopping at final beacon
                # ---------------------------------------------------
                elif x == 2:  # Check hall sensor when the final beacon has not been passed, after the cargo has been
                    # dropped off.
                    try:
                        # Read and store hall sensor value
                        value = BP.get_sensor(HALL_PORT)[0]
                        if value >= 2100:
                            setpower(RIGHTMOTOR_PORT, 0)
                            setpower(LEFTMOTOR_PORT, 0)
                        x = x + 1
                    except brickpi3.SensorError as error:
                        print(error)
                else:
                    pass
            else:
                setpower(RIGHTMOTOR_PORT, 0)
                setpower(LEFTMOTOR_PORT, 0)
        except NameError:
            pass

# ---------------------------------------------------
#  Exception
# ---------------------------------------------------
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    BP.reset_all()
