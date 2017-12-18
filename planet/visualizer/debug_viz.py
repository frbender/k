import visualizer

class DebugViz(visualizer):
    def __init__(self, lowest_key, highest_key, led_amount):
        visualizer.__init__(self, lowest_key, highest_key, led_amount)
        self.i = 0

    def draw(self):
        return [(1.0,0.0,1.0)] * visualizer.get_led_amount()
