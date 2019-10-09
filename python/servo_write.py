#!/usr/bin/python3

import time                 # import time for sleep()
import L1_servo as servo    # import L1_servo as servo for servo control

filename = "/tmp/servo_pos.txt"   # File path we will send our battery voltage data to.

while 1:    # Infinite loop.

    file = open(filename,"r")          # Open file.
    servo_pos = file.read()             # Read data in file and store in servo_pos

    print(servo_pos)

    if len(servo_pos) > 0:              # Makes sure servo_pos holds value.
        servo.move1(float(servo_pos))	# Set servo duty
    else:                               # If file is empty move on.
        pass

    time.sleep(0.1)
