from visualizer.base_visualizer import BaseVisualizer

class DebugViz(BaseVisualizer):
    def __init__(self, lowest_key, highest_key, led_amount):
        BaseVisualizer.__init__(self, lowest_key, highest_key, led_amount)
        self.i = 0

    def draw(self):
        return [(1.0,0.0,1.0)] * BaseVisualizer.get_led_amount()
