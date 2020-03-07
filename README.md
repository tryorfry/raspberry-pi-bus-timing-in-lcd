# Raspberry PI Singapore Bus Schedule Display in 16x2 LCD
Displays Bus Schedule for a bus stop in 16x2 LCD using [Raspberry PI](https://www.raspberrypi.org/).
This program uses [Land Transport Singapore](https://www.mytransport.sg/content/mytransport/home/dataMall.html) API
to display the bus services available and next 3 bus arrival timings for a given bus stop in 16x2 LCD

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- [Raspberry Pi](https://www.raspberrypi.org/) - I used Raspberry Pi 4 - but any pi should work fine
- 16x2 LCD

### Installing
![Wire Raspberry Pi and 16x2 LCD - in 4 bit mode](https://www.circuitbasics.com/wp-content/uploads/2015/04/Raspberry-Pi-LCD-4-bit-mode.png)

- Wire Raspberry Pi and 16x2 LCD - in 4 bit mode as shown above
```
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)    
```
- Clone this repo
- Install the depended python3 modules in ```requirements.py``` file
- Sign in [Singapore LTA](https://www.mytransport.sg/content/mytransport/home/dataMall.html) API to get the API token token
- Set the token as the environment variable
```
export DATAMALL_API_KEY='<YOUR_API_KEY>'
```
- Run the program:
```
python3 main.py 28091
```
### Demo Image:
![Showing Bus Timing](https://i.stack.imgur.com/o4KCI.jpg)



#### Built With
* [Raspberry Pi](https://www.raspberrypi.org/)
* [RPLCD](https://github.com/dbrgn/RPLCD) - The python Raspberry PI character LCD library
* [Singapore LTA](https://github.com/dbrgn/RPLCD) - Datamall API for bus services in Singapore

## Authors
* **Sachin Dangol**
