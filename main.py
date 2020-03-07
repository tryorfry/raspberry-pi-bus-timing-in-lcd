"""
Bus Arrival timings display in 16x2 LCD:

This program uses Land Transport Singapore(https://www.mytransport.sg/content/mytransport/home/dataMall.html) API
to display the bus services available and next 3 bus arrival timings for a given bus stop in 16x2 LCD
"""

import sys
import time
import RPi.GPIO as GPIO
from RPLCD import CharLCD

from sg_bus_api import DatamallApiClient

def main(BUS_STOP_CODE):
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

    bus_api = DatamallApiClient()

    while True:
        buses = bus_api.bus_at_busstop_code(BUS_STOP_CODE)
        for bus_num, bus_timings in buses.items():
            display_string = ''
            if len(bus_timings) == 0:
                display_string = f"Bus {bus_num}: NOT\r\nAVAILABLE"
            if len(bus_timings) == 1:
                display_string = f"Bus {bus_num}: {bus_timings[0]}\r\nLAST BUS"
            if len(bus_timings) == 2:
                display_string = f"Bus {bus_num}: {bus_timings[0]}\r\n{bus_timings[1]}"
            if len(bus_timings) == 3:            
                display_string = f"Bus {bus_num}: {bus_timings[0]}\r\n{bus_timings[1]}, {bus_timings[1]}"
            
            #print(display_string)
            lcd.clear()
            time.sleep(1) # to make change in info visible in screen 
            lcd.write_string(display_string)
            time.sleep(5)

        time.sleep(5) # in case of no items, do not send request in loop so fast to DatamallApi.

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError as error:
        print(f"ERROR:\n\tbus stop code not provided in command line argument.\nUSAGE:\n\tpython3 {sys.argv[0]} <6 digit bus stop code>")
        sys.exit()
        