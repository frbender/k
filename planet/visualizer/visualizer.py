from abc import ABCMeta, abstractmethod

class Visualizer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, lowest_key, highest_key, led_amount):
        print("[vis] initialized visualizer")

    def key_press(self, key_index, velocity):
        print("[vis] key press (key: {}, velocity: {})".format(key_index, velocity))

    def key_release(self, key_index):
        print("[vis] key release (key: {})")

    def update(self):
        print("[vis] update")

    def draw(self):
        print("[vis] draw")
