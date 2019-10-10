#!/usr/bin/python3
import sys
from mfrc522 import SimpleMFRC522

# Create a dictionary containing the last 4 digits of the RFID's serial numbers
# as the key and store the corresponding rooms as values to the keys.
rooms = {
  "3972": "Kitchen",
  "3453": "Living Room"
}

reader = SimpleMFRC522()
location_filename = "/tmp/location.txt"   # File path we will send our location data to.
sn_filename = "/tmp/rfid_sn.txt"   # File path we will send our RFID serial number data to.

# If this key doesnt work for you, try running find_key.py to find the key for your RFID
SimpleMFRC522.KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

try:
    while 1:    # Infinite loop.
        id, text = reader.read()   # Read RFID tag serial number and data
        sn = str(id)[-4:]
        with open(sn_filename, 'w+') as out:   # Open file (creates file if it does not already exist.) to write data to.
            out.write(sn+"\n")  # Write last 4 digits of S/N variable to file.
        with open(location_filename, 'w+') as out:   # Open file (creates file if it does not already exist.) to write data to.
            out.write(rooms[str(sn)]+"\n")  # Write last 4 digits of S/N variable to file.

except KeyboardInterrupt:
    raise
