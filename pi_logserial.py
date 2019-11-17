#!/usr/bin/env python3

import logging

import serial

PORT="/dev/ttyUSB0"


def main():
    conn = serial.Serial(PORT, baudrate=9600, stopbits=serial.STOPBITS_ONE)
    logging.info("Connected serial port " + repr(conn))

    while True:
        data = conn.readline()
        logging.info("Received data: " + data)
        
        with open("ivt490_raw_log.txt", "wt+") as fp:
            fp.write(data)
    
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    main()
