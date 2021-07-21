# The MIT License (MIT)
#
# Copyright (c) 2017 Dan Halbert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
`adafruit_hid.keyboard_layout_fr.KeyboardLayoutFR`
=======================================================

* Author(s): Dan Halbert
"""

#from .keycode import Keycode
from adafruit_hid.keycode import Keycode


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayoutFR:
    """Map ASCII characters to appropriate keypresses on a FR Mac keyboard.

    Non-ASCII characters and most control characters will raise an exception.
    """

    # The ASCII_TO_KEYCODE bytes object is used as a table to maps ASCII 0-127
    # to the corresponding # keycode on a US 104-key keyboard.
    # The user should not normally need to use this table,
    # but it is not marked as private.
    #
    # Because the table only goes to 127, we use the top bit of each byte (ox80) to indicate
    # that the shift key should be pressed. So any values 0x{8,9,a,b}* are shifted characters.
    #
    # The Python compiler will concatenate all these bytes literals into a single bytes object.
    # Micropython/CircuitPython will store the resulting bytes constant in flash memory
    # if it's in a .mpy file, so it doesn't use up valuable RAM.
    #
    # \x00 entries have no keyboard key and so won't be sent.
    SHIFT = b'\x02'
    ALTGR = b'\x40'
    ASCII_TO_KEYCODE = (
        b'\x00\x00'    # NUL
        b'\x00\x00'    # SOH
        b'\x00\x00'    # STX
        b'\x00\x00'    # ETX
        b'\x00\x00'    # EOT
        b'\x00\x00'    # ENQ
        b'\x00\x00'    # ACK
        b'\x00\x00'    # BEL \a
        b'\x00\x2a'    # BS BACKSPACE \b (called DELETE in the usb.org document)
        b'\x00\x2b'    # TAB \t
        b'\x00\x28'    # LF \n (called Return or ENTER in the usb.org document)
        b'\x00\x00'    # VT \v
        b'\x00\x00'    # FF \f
        b'\x00\x00'    # CR \r
        b'\x00\x00'    # SO
        b'\x00\x00'    # SI
        b'\x00\x00'    # DLE
        b'\x00\x00'    # DC1
        b'\x00\x00'    # DC2
        b'\x00\x00'    # DC3
        b'\x00\x00'    # DC4
        b'\x00\x00'    # NAK
        b'\x00\x00'    # SYN
        b'\x00\x00'    # ETB
        b'\x00\x00'    # CAN
        b'\x00\x00'    # EM
        b'\x00\x00'    # SUB
        b'\x00\x29'    # ESC
        b'\x00\x00'    # FS
        b'\x00\x00'    # GS
        b'\x00\x00'    # RS
        b'\x00\x00'    # US
        
        b'\x00\x2c'       #  ' '
        b'\x00\x38'       # !
        b'\x00\x20'       # "
        +SHIFT+b'\x20'    # #
        b'\x00\x30'       # $
        +SHIFT+b'\x34'    # %
        b'\x00\x1E'       # &
        b'\x00\x21'       # '
        b'\x00\x22'       # (
        b'\x00\x2d'       # )
        b'\x00\x31'       # *
        +SHIFT+b'\x2e'    # +
        b'\x00\x10'       # ,
        b'\x00\x23'       # -
        +SHIFT+b'\x36'    # .
        +SHIFT+b'\x37'    # /
        +SHIFT+b'\x27'    # 0
        +SHIFT+b'\x1e'    # 1
        +SHIFT+b'\x1f'    # 2
        +SHIFT+b'\x20'    # 3
        +SHIFT+b'\x21'    # 4
        +SHIFT+b'\x22'    # 5
        +SHIFT+b'\x23'    # 6
        +SHIFT+b'\x24'    # 7
        +SHIFT+b'\x25'    # 8
        +SHIFT+b'\x26'    # 9
        b'\x00\x37'       # :
        b'\x00\x36'       # ;
        b'\x00\x64'       # <
        b'\x00\x2e'       # =
        +SHIFT+b'\x64'    # >
        +SHIFT+b'\x10'    # ?
        +ALTGR+b'\x27'    # @
        +SHIFT+b'\x14'    # A
        +SHIFT+b'\x05'    # B
        +SHIFT+b'\x06'    # C
        +SHIFT+b'\x07'    # D
        +SHIFT+b'\x08'    # E
        +SHIFT+b'\x09'    # F
        +SHIFT+b'\x0a'    # G
        +SHIFT+b'\x0b'    # H
        +SHIFT+b'\x0c'    # I
        +SHIFT+b'\x0d'    # J
        +SHIFT+b'\x0e'    # K
        +SHIFT+b'\x0f'    # L
        +SHIFT+b'\x33'    # M
        +SHIFT+b'\x11'    # N
        +SHIFT+b'\x12'    # O
        +SHIFT+b'\x13'    # P
        +SHIFT+b'\x04'    # Q
        +SHIFT+b'\x15'    # R
        +SHIFT+b'\x16'    # S
        +SHIFT+b'\x17'    # T
        +SHIFT+b'\x18'    # U
        +SHIFT+b'\x19'    # V
        +SHIFT+b'\x1d'    # W
        +SHIFT+b'\x1b'    # X
        +SHIFT+b'\x1c'    # Y
        +SHIFT+b'\x1a'    # Z
        +ALTGR+b'\x22'    # [
        b'\x00\x31'       # bslash
        +ALTGR+b'\x2d'    # ]
        b'\x00\x2F'       # ^
        b'\x00\x25'       # _
        +ALTGR+b'\x24'    # `
        b'\x00\x14'       # a
        b'\x00\x05'       # b
        b'\x00\x06'       # c
        b'\x00\x07'       # d
        b'\x00\x08'       # e
        b'\x00\x09'       # f
        b'\x00\x0a'       # g
        b'\x00\x0b'       # h
        b'\x00\x0c'       # i
        b'\x00\x0d'       # j
        b'\x00\x0e'       # k
        b'\x00\x0f'       # l
        b'\x00\x33'       # m
        b'\x00\x11'       # n
        b'\x00\x12'       # o
        b'\x00\x13'       # p
        b'\x00\x04'       # q
        b'\x00\x15'       # r
        b'\x00\x16'       # s
        b'\x00\x17'       # t
        b'\x00\x18'       # u
        b'\x00\x19'       # v
        b'\x00\x1d'       # w
        b'\x00\x1b'       # x
        b'\x00\x1c'       # y
        b'\x00\x1a'       # z
        +ALTGR+b'\x21'    # {
        +ALTGR+b'\x23'    # |
        +ALTGR+b'\x2e'    # }
        +ALTGR+b'\x19'    # ~ TODO
        b'\x00\x00'       # DEL
    )

    def __init__(self, keyboard):
        """Specify the layout for the given keyboard.

        :param keyboard: a Keyboard object. Write characters to this keyboard when requested.

        Example::

            kbd = Keyboard()
            layout = KeyboardLayoutFR(kbd)
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
            (modifier,keycode) = self._char_to_keycode(char)
            # If this is a shifted char, clear the SHIFT flag and press the SHIFT key.
            if modifier & self.SHIFT[0]:
                self.keyboard.press(Keycode.SHIFT)
            if modifier & self.ALTGR[0]:
                self.keyboard.press(Keycode.GUI)
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
            keycode('a')
            # Returns (Keycode.SHIFT, Keycode.A)
            keycode('A')
            # Raises ValueError because it's a accented e and is not ASCII
            keycode('é')
        """
        out = []
        (modifier,keycode) = self._char_to_keycode(char)
        if modifier & self.SHIFT:
            out += [Keycode.SHIFT]
        if modifier & self.ALTGR:
            out += [Keycode.GUI]
        out += [keycode]
        return out

    def _char_to_keycode(self, char):
        """Return the HID keycode for the given ASCII character, with the SHIFT_FLAG possibly set.

        If the character requires pressing the Shift key, the SHIFT_FLAG bit is set.
        You must clear this bit before passing the keycode in a USB report.
        """
        char_val = ord(char)*2
        if char_val+1 >= len(self.ASCII_TO_KEYCODE):
            raise ValueError("Unknown character.")
        modifier = self.ASCII_TO_KEYCODE[char_val]
        keycode = self.ASCII_TO_KEYCODE[char_val+1]
        if keycode == 0:
            raise ValueError("No keycode available for character.")
        return (modifier,keycode)
