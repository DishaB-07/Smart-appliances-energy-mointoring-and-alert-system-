from flask import Flask, jsonify
import serial
import threading

app = Flask(__name__)

# change COM port
arduino = serial.Serial('COM3', 9600)

latest_data = {"current": 0}

def read_serial():
    global latest_data
    while True:
        if arduino.in_waiting:
            line = arduino.readline().decode().strip()
            try:
                latest_data["current"] = float(line)
            except:
                pass

threading.Thread(target=read_serial, daemon=True).start()

@app.route('/api/data')
def get_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)