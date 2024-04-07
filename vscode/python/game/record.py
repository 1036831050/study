import pyautogui
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
import threading

class Recorder:
    def __init__(self):
        self.recording = False
        self.actions = []

    def start(self):
        self.recording = True
        with MouseListener(on_click=self.on_click) as mouse_listener:
            with keyboard.Listener(on_press=self.on_press) as keyboard_listener:
                keyboard_listener.join()
                mouse_listener.join()

    def on_click(self, x, y, button, pressed):
        if self.recording:
            action = {'type': 'click', 'x': x, 'y': y, 'button': button, 'pressed': pressed}
            self.actions.append(action)

    def on_press(self, key):
        if self.recording:
            try:
                action = {'type': 'keypress', 'key': key.char}
            except AttributeError:
                action = {'type': 'keypress', 'key': key}
            self.actions.append(action)
            if key == keyboard.Key.ctrl_l and self.actions[-1]['key'] == 'q':
                self.stop()

    def stop(self):
        self.recording = False

    def save_actions(self, filename):
        with open(filename, 'w') as f:
            for action in self.actions:
                f.write(str(action) + '\n')

if __name__ == "__main__":
    recorder = Recorder()
    threading.Thread(target=recorder.start).start()
