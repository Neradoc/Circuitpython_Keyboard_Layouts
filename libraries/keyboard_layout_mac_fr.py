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
* Author(s): Dan Halbert, Neradoc
"""

#from .keycode import Keycode
from adafruit_hid.keycode import Keycode


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayoutMacFR:
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
    NUL = b'\x00'
    SHIFT = b'\x02'
    ALTGR = b'\x40'
    ALTSHIFT = b'\x42'
    ASCII_TO_KEYCODE = (
        NUL+b'\x00'     # NUL
        +NUL+b'\x00'    # SOH
        +NUL+b'\x00'    # STX
        +NUL+b'\x00'    # ETX
        +NUL+b'\x00'    # EOT
        +NUL+b'\x00'    # ENQ
        +NUL+b'\x00'    # ACK
        +NUL+b'\x00'    # BEL \a
        +NUL+b'\x2a'    # BS BACKSPACE \b (called DELETE in the usb.org document)
        +NUL+b'\x2b'    # TAB \t
        +NUL+b'\x28'    # LF \n (called Return or ENTER in the usb.org document)
        +NUL+b'\x00'    # VT \v
        +NUL+b'\x00'    # FF \f
        +NUL+b'\x00'    # CR \r
        +NUL+b'\x00'    # SO
        +NUL+b'\x00'    # SI
        +NUL+b'\x00'    # DLE
        +NUL+b'\x00'    # DC1
        +NUL+b'\x00'    # DC2
        +NUL+b'\x00'    # DC3
        +NUL+b'\x00'    # DC4
        +NUL+b'\x00'    # NAK
        +NUL+b'\x00'    # SYN
        +NUL+b'\x00'    # ETB
        +NUL+b'\x00'    # CAN
        +NUL+b'\x00'    # EM
        +NUL+b'\x00'    # SUB
        +NUL+b'\x29'    # ESC
        +NUL+b'\x00'    # FS
        +NUL+b'\x00'    # GS
        +NUL+b'\x00'    # RS
        +NUL+b'\x00'    # US
        
        +NUL+b'\x2c'       #  ' '
        +NUL+b'\x25'       # !
        +NUL+b'\x20'       # "
        +SHIFT+b'\x64'    # #
        +NUL+b'\x30'       # $
        +SHIFT+b'\x34'    # %
        +NUL+b'\x1E'       # &
        +NUL+b'\x21'       # '
        +NUL+b'\x22'       # (
        +NUL+b'\x2d'       # )
        +SHIFT+b'\x30'    # *
        +SHIFT+b'\x38'    # +
        +NUL+b'\x10'       # ,
        +NUL+b'\x2E'       # -
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
        +NUL+b'\x37'       # :
        +NUL+b'\x36'       # ;
        +NUL+b'\x35'       # <
        +NUL+b'\x38'       # =
        +SHIFT+b'\x35'    # >
        +SHIFT+b'\x10'    # ?
        +NUL+b'\x64'       # @
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
        +ALTSHIFT+b'\x22'    # [
        +ALTSHIFT+b'\x37'       # bslash
        +ALTSHIFT+b'\x2d'    # ]
        +NUL+b'\x2F'       # ^
        +SHIFT+b'\x2E'       # _
        +NUL+b'\x31'    # `
        +NUL+b'\x14'       # a
        +NUL+b'\x05'       # b
        +NUL+b'\x06'       # c
        +NUL+b'\x07'       # d
        +NUL+b'\x08'       # e
        +NUL+b'\x09'       # f
        +NUL+b'\x0a'       # g
        +NUL+b'\x0b'       # h
        +NUL+b'\x0c'       # i
        +NUL+b'\x0d'       # j
        +NUL+b'\x0e'       # k
        +NUL+b'\x0f'       # l
        +NUL+b'\x33'       # m
        +NUL+b'\x11'       # n
        +NUL+b'\x12'       # o
        +NUL+b'\x13'       # p
        +NUL+b'\x04'       # q
        +NUL+b'\x15'       # r
        +NUL+b'\x16'       # s
        +NUL+b'\x17'       # t
        +NUL+b'\x18'       # u
        +NUL+b'\x19'       # v
        +NUL+b'\x1d'       # w
        +NUL+b'\x1b'       # x
        +NUL+b'\x1c'       # y
        +NUL+b'\x1a'       # z
        +ALTGR+b'\x22'    # {
        +ALTSHIFT+b'\x0f'    # |
        +ALTGR+b'\x2d'    # }
        +ALTGR+b'\x11'    # ~ TODO
        +NUL+b'\x00'       # DEL
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
