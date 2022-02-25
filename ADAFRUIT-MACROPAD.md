# Adafruit Macropad - Installing and using other keyboard layouts

<br/>

The following is a guide on how to install and use other keyboard layouts from https://github.com/Neradoc/Circuitpython_Keyboard_Layouts on the *Adafruit Macropad*.

<br/>

## 1 - Getting the right keyboard layout files on the Adafruit Macropad

1) Go to https://kbdlayout.info and find the correct layout you need. In the case of the *Belgian French (Period)* layout the link is https://kbdlayout.info/kbdbe.
2) Paste this link in the *Url* box over at https://www.neradoc.me/layouts/ and press the *Make Zip Bundle Links* button.
3) Click the purple *CP7* (CircuitPython 7) button to download the smaller `.mpy` (binary) files instead of the `.py` files (you get these by pressing the purple *Download the zip file (.py)* button) and use those to save memory. If you want to slightly change the keyboard layout yourself then download the `.py` files.
4) Open the downloaded `.zip` folder and copy the files `keyboard_layout.mpy`, `keyboard_layout_win_XX.mpy` and `keycode_win_XX.mpy` to the `lib` folder on the *Adafruit Macropad*.

<br/>

## 2 - Making sure the macropad-code uses these new keyboard layout files

1) Replace the `adafruit_macropad.mpy` file in the `lib` folder on the *Adafruit Macropad* with the `adafruit_macropad.py` file so we can edit the contents of this library file and change which keyboard layout is used. Delete the `adafruit_macropad.mpy` file and replace it with the `adafruit_macropad.py` file downloaded from https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_MacroPad/main/adafruit_macropad.py (*right click* > *save as...*).
2) Edit the `adafruit_macropad.py` file so the code uses the correct keyboard layout files.
   1) Replace the line `from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS` with `from keyboard_layout_win_XX import KeyboardLayout`. This makes sure the code imports the keyboard layout we just copied to the `.lib` folder.
   3) Replace the line `self._keyboard_layout = KeyboardLayoutUS(self.keyboard)` with `self._keyboard_layout = KeyboardLayout(self.keyboard)`. This makes sure the code uses this newly imported keyboard layout.
3) Edit the files in the `macros` folder to use the new `Keycode` file.
   1) Replace the line `from adafruit_hid.keycode import Keycode` with `from keycode_win_XX import Keycode`. This makes sure the correct key-sequences are called when using the `Keycode.XXXXXX` functionality to create macros.

<br/>

## 3 - All done!

That should be everything, happy macro-padding!
