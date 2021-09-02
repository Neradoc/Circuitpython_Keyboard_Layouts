import usb_hid
from adafruit_hid.keyboard import Keyboard

# import the classes for the international layout
from keyboard_layout_win_fr import KeyboardLayout
from keycode_win_fr import Keycode

keyboard = Keyboard(usb_hid.devices)

# type with a layout
layout = KeyboardLayout(keyboard)
layout.write("Bonjour le monde")

# shortcuts with keycodes
keyboard.send(Keycode.ALT, Keycode.TAB)
