How to use a layout this with the pico-ducky repository.

#### Go to the [latest release page](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/releases/latest), look if your language is in the list.

## If your language/layout is in the bundle

Download the `py` zip, named `circuitpython-keyboard-layouts-py-XXXXXXXX.zip`

*You can use the mpy version targetting the version of Circuitpython that is on the device, but on Raspberry Pi Pico you don't need it - they only reduce file size and memory use on load, which the pico has plenty of.*

## If your language/layout is not in the bundle

Try the online generator, it should get you a zip file with the bundles for yout language

https://www.neradoc.me/layouts/

## Now you have a zip file

#### Find your language/layout in the lib directory 

For a language `LANG`, copy the following files from the zip's `lib` folder to the `lib` folder of the board.  
*DO NOT* change the names or extensions of the files. Just pick the right ones.  
Replace LANG with the letters for your language of choice.

- `keyboard_layout.py`
- `keyboard_layout_win_LANG.py`
- `keycode_win_LANG.py`

#### Modify the pico-ducky code to use your language file:

At the start of the file replace:

```py
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
```

With this. Change `LANG` for you language, so the module names match the files without the extension.
```py
from keyboard_layout_win_LANG import KeyboardLayout
from keycode_win_LANG import Keycode
```

And also replace:
```py
layout = KeyboardLayoutUS(kbd)
```
With:
```py
layout = KeyboardLayout(kbd)
```
