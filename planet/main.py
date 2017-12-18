from configparser import ConfigParser
from pixel_pusher import PixelPusher
from serial import Serial

if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.conf')

    print('Welcome to k!')

    pushy = PixelPusher(config=config)

    input("bla")
