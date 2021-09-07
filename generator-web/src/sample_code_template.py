import usb_hid
from adafruit_hid.keyboard import Keyboard
import keyboard_layout_<platform>_<lang>
from keycode_<platform>_<lang> import Keycode

keyboard = Keyboard(usb_hid.devices)
# type with a layout
layout = keyboard_layout_<platform>_<lang>.KeyboardLayout(keyboard)
layout.write("Bonjour le monde")
# shortcuts with keycodes
keyboard.send(Keycode.LEFT_CONTROL, Keycode.A)
keyboard.send(Keycode.DELETE)
