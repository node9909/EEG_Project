from pynput.keyboard import Key, Listener
import numpy as np

log = []


def on_press(key):
    if key == Key.ctrl_l:
        print('True')
        log.append(1)
    if key == Key.ctrl_r:
        print('False')
        log.append(0)
    if key == Key.backspace:
        return False


with Listener(on_press=on_press) as listener:
    listener.join()

np.save('./answers', log)
