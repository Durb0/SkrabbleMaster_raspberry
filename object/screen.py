import serial
from typing import List
import time
import os
import serial.tools.list_ports

class Screen:
    def __init__(self, width, height):
        port = self.find_arduino_port()
        self.activate_port_permission(port)
        self.ser = serial.Serial(port, 9600)
        time.sleep(3)
        self._width = width
        self._height = height

    def find_arduino_port(self):
        arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Arduino' in p.description
        ]
        if not arduino_ports:
            raise IOError("No Arduino found")
        return arduino_ports[0]

    def activate_port_permission(self, port):
        os.system(f'sudo chmod a+rw {port}')

    def show_on_arduino(self, commands: List[str]):
        #join all commands with a | separator
        message = '|'.join(commands)
        print(bytes(message, "utf-8"))
        self.ser.write(bytes(message, "utf-8"))


if __name__ == '__main__':
    screen = Screen(240, 320)
    while True:
        try:
            screen.show_on_arduino([
                "text?value=Hello;color=0xFFFF;x_start=0;y_start=0;size=2;",
                "text?value=World;color=0xFFFF;x_start=0;y_start=30;size=2;"
            ])
            input('Press enter to retry')
        except serial.serialutil.SerialException:
            print('No serial connection')
            input('Press enter to try again')
