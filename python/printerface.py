import serial
import sys
import json

from flask import Flask
from flask_restful import reqparse, Resource, Api

import threading

state = {}


class PrinterFace():
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, 9600, timeout=5)

    # Thread function
    def run(self):
        global state
        while True:
            inp = self.ser.readline().decode().replace('\n', '')
            try:
                data = json.loads(inp)
                state = data
            except json.JSONDecodeError:
                pass


printerface = PrinterFace(sys.argv[1])
t = threading.Thread(target=printerface.run)

print("Starting thread...")
t.start()

parser = reqparse.RequestParser()
parser.add_argument('sensor')

app = Flask(__name__)
api = Api(app)


class Get(Resource):
    def get(self, sensor):
        if sensor in state:
            return state[sensor]
        else:
            return 0


api.add_resource(Get, '/get/<sensor>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
