from configparser import ConfigParser
from pixel_pusher import PixelPusher

if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.conf')

    print('Welcome to k!')

    pushy = PixelPusher(config=config)

    pushy.set_all((1.0, 0.0, 1.0))
    pushy.show()

    input("bla")
