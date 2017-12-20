import serial
import time

class PixelPusher():
    def __init__(self, config):
        self.port = config["serial"]["port"]
        self.baud = int(config["serial"]["baud"])
        self.serial = serial.Serial(port=self.port, baudrate=self.baud)
        time.sleep(3)

    def send_preamble(self):
        self.serial.write([0xFF,0xFF,0xFF,0xFF])

    def set_multiple(self, colors):
        for index, color in enumerate(colors):
            self.set_led(index, color)


    def set_led(self, led, color):
        if led > 199:
            print("Cant set LED with index > 199!")
            return
        r, g, b = color
        led = int(led)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        self.send_preamble()
        self.send([led,r,g,b])

    def blackout(self):
        self.send_preamble()
        self.send([201, 0x00, 0x00, 0x00])
        self.flush()

    def set_all(self, color):
        r, g, b = color
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        self.send_preamble()
        self.send([200,r,g,b])
        self.flush()

    def show(self):
        self.send_preamble()
        self.send([0xFE, 0x00, 0x00, 0x00])
        self.flush()

    def send(self, data):
        if not self.serial.is_open:
            return
        self.serial.write(bytearray(data))

    def flush(self):
        self.serial.flush()

    def close(self):
        self.serial.close()

