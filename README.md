## Keyboard Layouts For Circuitpython

The goal of this repository is to contain a list of keyboard layouts for use with the adafruit_hid library, that can be used as a reference for international keyboards and can be distributed as a "bundle" in the style of the Adafruit bundle.

It is intended to be compatible with circup for easy installation with a command like this, once circup supports third-party bundles.

```
circup install keyboard_layout_win_fr
```

`keyboard_layout_<platform>_<lang>` modules will contain the layout information for use with the `Keyboard` to type text.

```py
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_fr import KeyboardLayoutFR
keyboard = Keyboard(usb_hid.devices)
keyboard_fr = KeyboardLayoutFR(keyboard)
keyboard_fr.write("Bonjour le monde")
```

`keycode_<platform>_<lang>` modules are an attempt to make it easier to swap layouts. HID Keycodes normally reference the US keyboard. These these localized keycodes offer a level of conversion allowing to use `Keycode.A` across azerty and qwerty keyboards for example. It won't swap `control` and `command` to match the platform however. (yet ?)

```py
if IS_AZERTY:
	from keycode_mac_fr import Keycode
else:
	from adafruit_hid.keycode import Keycode

kbd.send(Keycode.COMMAND, Keycode.A)
```

NOTE: this is pretty much experimental for now, these layouts are not for use.