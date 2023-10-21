# GpsTracker using Raspberry Pi, Python and HTML

Gives your longitude and latitude location using a gps module and sends it a html page using flask

## Hardware Requirements:
- A raspberry pi
- female to male connectors
- Neo6m GPS tracker
- Header pins for the tracker

## Software Requirements:    
### Frontend: 
Packages used:
- Leaflet node module.

### Backend: 
Python: 
- Flask to get and push data to the front end.

   ``` pip3 install flask ```
- Serial to read data from the GPIO Ports of the Raspberry Pi.

  ```pip3 install pyserial```
- pynmea2 to read data from the neo6m GPS Tracker module.

  ```pip3 install pynmea2```
- Time to get time

  
