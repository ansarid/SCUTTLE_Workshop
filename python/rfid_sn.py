#!/usr/bin/python3
import sys
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
filename = "/tmp/rfid_sn.txt"   # File path we will send our RFID serial number data to.

# If this key doesnt work for you, try running find_key.py to find the key for your RFID
SimpleMFRC522.KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

try:
    while 1:    # Infinite loop.
        id, text = reader.read()   # Read RFID tag serial number and data
        with open(filename, 'w+') as out:   # Open file (creates file if it does not already exist.) to write data to.
            out.write(str(id)[-4:]+"\n")     # Write last 4 digits of S/N variable to file.

except KeyboardInterrupt:
    raise
