#!/usr/bin/python3

import time             # import time for sleep()
import L1_adc as adc    # import L1_adc as adc for getDcJack()

filename = "/tmp/battery_v.txt"   # File path we will send our battery voltage data to.

while 1:    # Infinite loop.

    dcJack = adc.getDcJack()    # Read Battery Voltage.

    with open(filename, 'w+') as out:   # Open file (creates file if it does not already exist.) to write data to.
        out.write(str(dcJack)+"\n")     # Write dcJack variable to file.

    # print(dcJack)   # Print voltage.
    time.sleep(10) # Sleep 500 ms. 2Hz Sample rate.
