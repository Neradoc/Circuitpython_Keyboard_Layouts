import usb_hid
from adafruit_hid.keyboard import Keyboard

# import the classes for the international layout
from keyboard_layout_win_fr import KeyboardLayout as KeyboardLayoutFR
from keyboard_layout_win_us import KeyboardLayout as KeyboardLayoutUS
from keycode_win_fr import Keycode as KeycodeFR
from keycode_win_us import Keycode as KeycodeUS

keyboard = Keyboard(usb_hid.devices)

# type in french
layout = KeyboardLayoutFR(keyboard)
layout.write("Vive l'été à la forêt")

# switch layout
# needs to have the layouts configured and the shortcut too
# NOTE: alt and shift don't need a special layout
keyboard.send(KeycodeFR.SHIFT, KeycodeFR.ALT)

# type in english
layout = KeyboardLayoutFR(keyboard)
layout.write("This was QWERTY")
