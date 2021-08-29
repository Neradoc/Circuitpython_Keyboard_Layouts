import usb_hid
from adafruit_hid.keyboard import Keyboard
import keyboard_layout_win_fr
from keycode_win_fr import Keycode

keyboard = Keyboard(usb_hid.devices)
# type with a layout
layout = keyboard_layout_win_fr.KeyboardLayout(keyboard)
layout.write("Bonjour le monde")
# shortcuts with keycodes
keyboard.send(Keycode.LEFT_CONTROL, Keycode.A)
keyboard.send(Keycode.DELETE)
