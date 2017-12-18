import mido

def noop ():
    return

class BlastPianoProcessor():
    def __init__(self, config, key_press_callback = noop, key_release_callback = noop):
        if config["midi"]["input"] == "default":
            if len(mido.get_input_names()) == 0:
                print("No Midi Inputs detected!")
                exit(0)
            else:
                self.input_name = mido.get_input_names()[0]
        else:
            self.input_name = config["midi"]["input"]

        self.input = mido.open_input(self.input_name)

        self.input.callback = self.handle_event
        self.key_press_callback = key_press_callback
        self.key_release_callback = key_release_callback

    def handle_event(self, event):
        if event.type == 'note_on':
            if event.velocity > 0:
                self.key_press_callback(event.note, event.velocity)
            if event.velocity == 0:
                self.key_release_callback(event.note)
        if event.type == 'note_off':
                self.key_release_callback(event.note)

if __name__ == "__main__":
    from configparser import ConfigParser
    config = ConfigParser()
    config.read('config.conf')
    x = BlastPianoProcessor(config)

    input("exit?")