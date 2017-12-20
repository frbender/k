from visualizer.base_visualizer import BaseVisualizer
import colorsys
import math


class Particles(BaseVisualizer):
    def __init__(self, config, lowest_key, highest_key, led_amount):
        BaseVisualizer.__init__(self, config, lowest_key, highest_key, led_amount)
        self.particles = []
        self.friction = float(config["particles"]["friction"])
        self.speed = float(config["particles"]["speed"])
        self.decay = float(config["particles"]["decay"])

    def spawn_particles(self, pos, direction, force):
        directed_force = 0.0
        if direction == "left":
            directed_force = -1.0
        elif direction == "right":
            directed_force = 1.0
        else:
            print("direction has to be 'left' or 'right'")
            return

        color = colorsys.hsv_to_rgb(pos, 1.0, 1.0)

        new_particle = {
            "pos": pos,
            "dir": directed_force,
            "vel": force,
            "opacity": force,
            "color": color}

        self.particles.append(new_particle)

    def update(self, Δt=1):
        removed_particles = []
        for particle in self.particles:
            particle['pos'] += particle['vel'] * particle['dir'] * Δt * self.speed
            particle['vel'] = max(particle['vel'] - self.friction, 0.0)
            particle['opacity'] -= self.decay
            if 0 > particle['pos'] or 1 < particle['pos'] or particle['opacity'] <= 0:
                removed_particles.append(particle)

        for particle in removed_particles:
            self.particles.remove(particle)

    def draw(self):
        leds = [[0.0, 0.0, 0.0] for x in range(self.led_amount)]
        for x in range(self.led_amount):
            for p in self.particles:
                if int(math.floor(p['pos']*self.led_amount)) == x:
                    col = p['color']
                    leds[x][0] += col[0] * p['opacity']
                    leds[x][1] += col[1] * p['opacity']
                    leds[x][2] += col[2] * p['opacity']
        return [(min(c[0], 1.0), min(c[1], 1.0), min(c[2], 1.0)) for c in leds]

    def key_press(self, key_index, velocity):
        pos = float(key_index) / float(self.key_amount-1)
        self.spawn_particles(pos, 'left', velocity)
        self.spawn_particles(pos, 'right', velocity)

    def key_release(self, key_index):
        return
