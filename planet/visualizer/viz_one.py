from visualizer.base_visualizer import BaseVisualizer
import math


class Viz_One(BaseVisualizer):
    def __init__(self, config, lowest_key, highest_key, led_amount):

        BaseVisualizer.__init__(self, config, lowest_key, highest_key, led_amount)

        self.colorStrip = [[0, 0, 0]] * led_amount
        self.blurRad = int(BaseVisualizer.config["viz_one"]["blur_radius"])
        self.alpha = int(BaseVisualizer.config["viz_one"]["alpha"])

    def draw(self):
        return self.colorStrip

    def key_press(self, key_index, velocity):
        led_index = math.floor(
            self.led_amount * (key_index - self.lowest_key) / (self.highest_key - self.lowest_key))  # todo?
        self.colorStrip[led_index] = [0, 0, 1.0]

    def key_release(self, key_index):
        return

    def update(self, Δt):
        new_strip = list(self.colorStrip)

        for index, color in enumerate(new_strip):
            # Calculate Average in radius
            sum_r, sum_g, sum_b = 0, 0, 0
            for r in range(max(index - self.blurRad, 0), min(index + self.blurRad + 1, len(self.colorStrip))):
                old_r, old_g, old_b = self.colorStrip[r]
                sum_r += old_r ** 2.  # R
                sum_g += old_g ** 2.  # G
                sum_b += old_b ** 2.  # B

            pixelAmount = float(min(index + self.blurRad + 1, len(self.colorStrip)) - max(index - self.blurRad, 0))
            new_r = math.sqrt(sum_r / pixelAmount) * self.alpha
            new_g = math.sqrt(sum_g / pixelAmount) * self.alpha
            new_b = math.sqrt(sum_b / pixelAmount) * self.alpha

            new_strip[index] = new_r, new_g, new_b

        # Write blurred version
        self.colorStrip = new_strip
