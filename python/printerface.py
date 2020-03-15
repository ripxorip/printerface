import serial
import sys
import json

from flask import Flask
from flask_restful import Resource, Api

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
            print(inp)
            try:
                data = json.loads(inp)
                state = data
            except json.JSONDecodeError:
                pass


printerface = PrinterFace(sys.argv[1])
t = threading.Thread(target=printerface.run)

print("Starting thread...")
t.start()

app = Flask(__name__)
api = Api(app)


class GetGas(Resource):
    def get(self):
        global state
        return state['gas']


class GetTemperature(Resource):
    def get(self):
        global state
        return state['temp']


api.add_resource(GetGas, '/gas')
api.add_resource(GetTemperature, '/temp')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
