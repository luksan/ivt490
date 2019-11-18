#!/usr/bin/env python3

import logging
from datetime import datetime

import serial

PORT="/dev/ttyUSB0"


def main():
    conn = serial.Serial(PORT, baudrate=9600, stopbits=serial.STOPBITS_ONE)
    logging.info("Connected serial port " + repr(conn))

    while True:
        data = conn.readline().decode('ascii')
        now = datetime.now().isoformat()
        logging.info(now + " Received data: " + data)
        
        with open("ivt490_raw_log.txt", "wt+") as fp:
            fp.write(now)
            fp.write(",")
            fp.write(data)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    main()
