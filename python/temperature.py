# Please install the BMP28P library first using:
# sudo pip3 install bmp280

#!/usr/bin/python3

import time             # import time for sleep()
import L1_bmp as bmp # import L1_bmp as bmp for temp()

filename = "/tmp/bmp_temp.txt"   # File path we will send our temperature data to.

while 1:    # Infinite loop.

    temp = bmp.temp()           # Read BMP temperature.

    with open(filename, 'w+') as out:   # Open file (creates file if it does not already exist.) to write data to.
        out.write(str(temp)+"\n")     # Write temp variable to file.

    time.sleep(1) # Sleep 500 ms. 2Hz Sample rate.
