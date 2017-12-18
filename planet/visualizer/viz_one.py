from visualizer.base_visualizer import BaseVisualizer
import math

class Viz_One(BaseVisualizer):
    def __init__(self, lowest_key, highest_key, led_amount):
        
        BaseVisualizer.__init__(self, lowest_key, highest_key, led_amount)
        

        self.colorStrip = [[0, 0, 0]] * led_amount
        self.blurRad = 1


    def draw(self):
        print(self.colorStrip)
        return self.colorStrip


    def key_press(self, key_index, velocity):
        led_index = math.floor(self.led_amount * (key_index - self.lowest_key)/(self.highest_key - self.lowest_key)) #todo?
        self.colorStrip[led_index] = [0, 0, 1.0]

    def key_release(self, key_index):
        return

    def update(self, Δt):
        newstrip = self.colorStrip

        for index, color in enumerate(newstrip):
            #Calculate Average in radius
            color[0] = 0
            color[1] = 0
            color[2] = 0
            for r in range(max(index - self.blurRad, 0), min(index + self.blurRad + 1, len(self.colorStrip))):
                color[0] += self.colorStrip[r][0] ** 2 #R
                color[1] += self.colorStrip[r][1] ** 2 #G
                color[2] += self.colorStrip[r][2] ** 2 #B


            pixelAmount = min(index + self.blurRad + 1, len(self.colorStrip)) - max(index - self.blurRad, 0)
            color[0] = math.sqrt(color[0] / pixelAmount)
            color[1] = math.sqrt(color[1] / pixelAmount)
            color[2] = math.sqrt(color[2] / pixelAmount)

        #Write blurred version
        self.colorStrip = newstrip