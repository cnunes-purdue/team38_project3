# Project 3 Final Demonstration: MACRO Stop Test.
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
#           This program instructs the MACRO to move forward and stop when encountering an obstacle.
# ---------------------------------------------------
#  Imports
# ---------------------------------------------------
import brickpi3
import grovepi
import time

# ---------------------------------------------------
#  Define Variables
# ---------------------------------------------------
BP = brickpi3.BrickPi3()
LEFTMOTOR_PORT = BP.PORT_A
RIGHTMOTOR_PORT = BP.PORT_D
SONIC_PORT = 3

# ---------------------------------------------------
#  Initialize Sensors
# ---------------------------------------------------
grovepi.pinMode(SONIC_PORT, "INPUT")


# ---------------------------------------------------
#  Define Functions
# ---------------------------------------------------
def setpower(port, power):
    BP.set_motor_power(port, -power)


# ---------------------------------------------------
#  Main Logic
# ---------------------------------------------------
try:
    while True:
        try:
            # Gather values from ultrasonic sensor
            sonicvalue = grovepi.digitalRead(SONIC_PORT)
            time.sleep(0.01)
        except IOError:
            print("Error")
        try:
            if sonicvalue > 25:  # Standard cruising distance
                setpower(LEFTMOTOR_PORT, 30)
                setpower(LEFTMOTOR_PORT, 30)
            elif 10 <= sonicvalue <= 25:  # Caution distance
                setpower(LEFTMOTOR_PORT, 15)
                setpower(LEFTMOTOR_PORT, 15)
            elif sonicvalue <= 15:  # Collision avoidance distance
                setpower(LEFTMOTOR_PORT, 0)  # Stops robot
                setpower(RIGHTMOTOR_PORT, 0)
        except NameError:
            pass

# ---------------------------------------------------
#  Exception
# ---------------------------------------------------
except KeyboardInterrupt:  # Ctrl-c ends program
    setpower(LEFTMOTOR_PORT, 0)
    setpower(RIGHTMOTOR_PORT, 0)
    BP.reset_all()


