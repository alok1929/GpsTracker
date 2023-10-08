from flask import Flask, jsonify
import serial
import pynmea2
import time

app = Flask(__name__)

def get_gps_data():
     while True:
        try:
            port = "/dev/ttyAMA0"
            ser = serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout = pynmea2.NMEAStreamReader()
            newdata = ser.readline()

            if newdata[0:6] == "$GPRMC":
                newmsg = pynmea2.parse(newdata)
                lat = newmsg.latitude
                lng = newmsg.longitude
                return {'latitude': lat, 'longitude': lng}

            time.sleep(5)  # Wait for 5 seconds before reading again
        except Exception as e:
            print("Error:", str(e))
            time.sleep(5)  # Wait for 5 seconds before retrying

@app.route('/api/get_gps_data', methods=['GET'])
def serve_gps_data():
    gps_data = get_gps_data()
    return jsonify(gps_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
