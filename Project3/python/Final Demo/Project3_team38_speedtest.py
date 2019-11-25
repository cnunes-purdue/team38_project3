# Project 3 Final Demonstration: Third Cargo Drop.
# File: Project3_team38_thirddrop.py
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
#           This program instructs the MACRO to move forward at a given motor power for a given amount of time.
# ---------------------------------------------------
#  Imports
# ---------------------------------------------------
import brickpi3
import time

# ---------------------------------------------------
#  Define Variables
# ---------------------------------------------------
BP = brickpi3.BrickPi3()

LEFT_PORT = BP.PORT_A
RIGHT_PORT = BP.PORT_D

# ---------------------------------------------------
#  Inputs
# ---------------------------------------------------
power = int(input("Enter Motor Power"))
t = float(input("Enter Time to run:"))

# ---------------------------------------------------
#  Main Logic
# ---------------------------------------------------
try:
    BP.set_motor_power(LEFT_PORT, power)
    BP.set_motor_power(RIGHT_PORT, power)
    time.sleep(t)
    BP.set_motor_power(LEFT_PORT, 0)
    BP.set_motor_power(RIGHT_PORT, 0)

# ---------------------------------------------------
#  Exception
# ---------------------------------------------------
except KeyboardInterrupt:
    BP.reset_all()