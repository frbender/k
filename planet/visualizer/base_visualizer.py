from abc import ABCMeta, abstractmethod


class BaseVisualizer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, lowest_key, highest_key, led_amount):
        self.lowest_key = lowest_key
        self.highest_key = highest_key
        self.led_amount = led_amount
        print("[vis] initialized visualizer")

    def key_press(self, key_index, velocity):
        print("[vis] key press (key: {}, velocity: {})".format(key_index, velocity))

    def key_release(self, key_index):
        print("[vis] key release (key: {})")

    def get_lowest_key(self):
        return self.lowest_key

    def get_highest_key(self):
        return self.highest_key

    def get_led_amount(self):
        return self.led_amount

    def update(self, Δt = 1):
        return

    def draw(self):
        return