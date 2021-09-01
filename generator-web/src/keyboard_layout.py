# SPDX-FileCopyrightText: 2017 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
* Author(s): Dan Halbert, AngainorDev, Neradoc
"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayoutBase:
    """Map ASCII characters to appropriate keypresses on a standard US PC keyboard.

    Non-ASCII characters and most control characters will raise an exception.
    """

    # We use the top bit of each byte (0x80) to indicate
    # that the shift key should be pressed, and an extra 9th bit 0x100 for AltGr
    SHIFT_FLAG = 0x80
    ALTGR_FLAG = 0x100
    ASCII_TO_KEYCODE = ()
    NEED_ALTGR = ""
    HIGHER_ASCII = {}
    RIGHT_ALT_CODE = 0xE6
    SHIFT_CODE = 0xE1

    def __init__(self, keyboard):
        """Specify the layout for the given keyboard.

        :param keyboard: a Keyboard object. Write characters to this keyboard when requested.

        Example::

            kbd = Keyboard(usb_hid.devices)
            layout = KeyboardLayoutUS(kbd)
        """
        self.keyboard = keyboard

    def write(self, string):
        """Type the string by pressing and releasing keys on my keyboard.

        :param string: A string of ASCII characters.
        :raises ValueError: if any of the characters are not ASCII or have no keycode
            (such as some control characters).

        Example::

            # Write abc followed by Enter to the keyboard
            layout.write('abc\\n')
        """
        for char in string:
            keycode = self._char_to_keycode(char)
            if char in self.NEED_ALTGR:
                # Add altgr modifier
                self.keyboard.press(self.RIGHT_ALT_CODE)
            # If this is a shifted char, clear the SHIFT flag and press the SHIFT key.
            if keycode & self.SHIFT_FLAG:
                keycode &= ~self.SHIFT_FLAG
                self.keyboard.press(self.SHIFT_CODE)
            self.keyboard.press(keycode)
            self.keyboard.release_all()

    def keycodes(self, char):
        """Return a tuple of keycodes needed to type the given character.

        :param char: A single ASCII character in a string.
        :type char: str of length one.
        :returns: tuple of Keycode keycodes.
        :raises ValueError: if ``char`` is not ASCII or there is no keycode for it.

        Examples::

            # Returns (Keycode.TAB,)
            keycodes('\t')
            # Returns (Keycode.A,)
            keycodes('a')
            # Returns (Keycode.SHIFT, Keycode.A)
            keycodes('A')
            # Raises ValueError because it's a accented e and is not ASCII
            keycodes('é')
        """
        keycode = self._char_to_keycode(char)
        codes = []
        if char in self.NEED_ALTGR:
            codes.append(self.RIGHT_ALT_CODE)
        if keycode & self.SHIFT_FLAG:
            codes.extend((self.SHIFT_CODE, keycode & ~self.SHIFT_FLAG))
        else:
            codes.append(keycode)

        return codes

    def _above128char_to_keycode(self, char):
        """Return keycode for above 128 ascii codes.

        Since the values are sparse, this may be more space efficient than bloating the table above
        or adding a dict.

        :param char_val: ascii char value
        :return: keycode, with modifiers if needed
        """
        if char in self.HIGHER_ASCII:
            return self.HIGHER_ASCII[char]
        if ord(char) in self.HIGHER_ASCII:
            return self.HIGHER_ASCII[ord(char)]

        raise ValueError(
            "Unsupported non-ASCII character {letter} ({num}/0x{num:02x}).".format(
                letter=str(char), num=ord(char)
            )
        )

    def _char_to_keycode(self, char):
        """Return the HID keycode for the given ASCII character, with the SHIFT_FLAG possibly set.

        If the character requires pressing the Shift key, the SHIFT_FLAG bit is set.
        You must clear this bit before passing the keycode in a USB report.
        """
        char_val = ord(char)
        if char_val > len(self.ASCII_TO_KEYCODE):
            return self._above128char_to_keycode(char)
        keycode = self.ASCII_TO_KEYCODE[char_val]
        if keycode == 0:
            raise ValueError(
                "No keycode available for character {letter} ({num}/0x{num:02x}).".format(
                    letter=str(char), num=char_val
                )
            )
        return keycode
