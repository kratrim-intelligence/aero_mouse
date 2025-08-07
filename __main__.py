import serial
from pynput.mouse import Controller, Button
import re

port = serial.Serial('COM7', baudrate=9600)
mouse = Controller()
mouse.move(0, 0)

while True:
    try:
        data = port.readline()
        data = data.decode("ascii").strip()
        data = re.split(r' ', data)
        s = data[0]
        x = int(float(data[1]))
        y = int(float(data[2]))

        print(s, ' ', x, ' ', y)
        mouse.move((-1) * y, x)

        if s == 'H':
            mouse.press(Button.left)
            # mouse.release(Button.left)
        else:
            mouse.release(Button.left)
    except:
        port.close()
