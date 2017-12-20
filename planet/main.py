from configparser import ConfigParser
from pixel_pusher import PixelPusher
from blast_piano_processor import BlastPianoProcessor
from visualizer.viz_one import Viz_One
import time
import threading

if __name__ == '__main__':
    print('Welcome to k!')

    # Setup config
    config = ConfigParser()
    config.read('config.conf')

    lowest_key = int(config["midi"]["lowest_key"])
    highest_key = int(config["midi"]["highest_key"])
    led_amount = int(config["visualizer"]["led_amount"])

    # pushes colors to leds
    pushy = PixelPusher(config=config)

    # visualization
    # todo: add config to vis
    vizzy = Viz_One(config,
                    lowest_key,
                    highest_key,
                    led_amount)


    def key_press(key, vel):
        vizzy.key_press(key - lowest_key, float(vel) / 127.0)


    def key_release(key):
        vizzy.key_release(key - lowest_key)


    blaster = BlastPianoProcessor(config=config, key_press_callback=key_press, key_release_callback=key_release)

    old_time = time.time()

    vizzy.key_press(10, 1)


    def tick(old_time):
        new_time = time.time()

        vizzy.update(new_time - old_time)
        newColors = vizzy.draw()
        pushy.set_multiple(newColors)
        pushy.show()

        old_time = new_time
        threading.Timer(0.0, tick, [old_time]).start()


    threading.Timer(0.03, tick, [1]).start()

    input("bla")
