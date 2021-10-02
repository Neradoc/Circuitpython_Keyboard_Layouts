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

from keyboard_layout import KeyboardLayoutBase


__version__ = "1.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayout(KeyboardLayoutBase):
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
    SHIFT_FLAG = 0x80
    
    ASCII_TO_KEYCODE = (
        b'\x00'     # NUL
        b'\x00'    # SOH
        b'\x00'    # STX
        b'\x00'    # ETX
        b'\x00'    # EOT
        b'\x00'    # ENQ
        b'\x00'    # ACK
        b'\x00'    # BEL \a
        b'\x2a'    # BS BACKSPACE \b (called DELETE in the usb.org document)
        b'\x2b'    # TAB \t
        b'\x28'    # LF \n (called Return or ENTER in the usb.org document)
        b'\x00'    # VT \v
        b'\x00'    # FF \f
        b'\x00'    # CR \r
        b'\x00'    # SO
        b'\x00'    # SI
        b'\x00'    # DLE
        b'\x00'    # DC1
        b'\x00'    # DC2
        b'\x00'    # DC3
        b'\x00'    # DC4
        b'\x00'    # NAK
        b'\x00'    # SYN
        b'\x00'    # ETB
        b'\x00'    # CAN
        b'\x00'    # EM
        b'\x00'    # SUB
        b'\x29'    # ESC
        b'\x00'    # FS
        b'\x00'    # GS
        b'\x00'    # RS
        b'\x00'    # US
        
        b'\x2c'       #  ' '
        b'\x25'       # !
        b'\x20'       # "
        b'\xe4'    # #
        b'\x30'       # $
        b'\xb4'    # %
        b'\x1E'       # &
        b'\x21'       # '
        b'\x22'       # (
        b'\x2d'       # )
        b'\xb0'    # *
        b'\xb8'    # +
        b'\x10'       # ,
        b'\x2E'       # -
        b'\xb6'    # .
        b'\xb7'    # /
        b'\xa7'    # 0
        b'\x9e'    # 1
        b'\x9f'    # 2
        b'\xa0'    # 3
        b'\xa1'    # 4
        b'\xa2'    # 5
        b'\xa3'    # 6
        b'\xa4'    # 7
        b'\xa5'    # 8
        b'\xa6'    # 9
        b'\x37'       # :
        b'\x36'       # ;
        b'\x35'       # <
        b'\x38'       # =
        b'\xb5'    # >
        b'\x90'    # ?
        b'\x64'       # @
        b'\x94'    # A
        b'\x85'    # B
        b'\x86'    # C
        b'\x87'    # D
        b'\x88'    # E
        b'\x89'    # F
        b'\x8a'    # G
        b'\x8b'    # H
        b'\x8c'    # I
        b'\x8d'    # J
        b'\x8e'    # K
        b'\x8f'    # L
        b'\xb3'    # M
        b'\x91'    # N
        b'\x92'    # O
        b'\x93'    # P
        b'\x84'    # Q
        b'\x95'    # R
        b'\x96'    # S
        b'\x97'    # T
        b'\x98'    # U
        b'\x99'    # V
        b'\x9d'    # W
        b'\x9b'    # X
        b'\x9c'    # Y
        b'\x9a'    # Z
        b'\xa2'    # [
        b'\xb7'       # bslash
        b'\xad'    # ]
        b'\x00'       # ^
        b'\xaE'       # _
        b'\x00'    # `
        b'\x14'       # a
        b'\x05'       # b
        b'\x06'       # c
        b'\x07'       # d
        b'\x08'       # e
        b'\x09'       # f
        b'\x0a'       # g
        b'\x0b'       # h
        b'\x0c'       # i
        b'\x0d'       # j
        b'\x0e'       # k
        b'\x0f'       # l
        b'\x33'       # m
        b'\x11'       # n
        b'\x12'       # o
        b'\x13'       # p
        b'\x04'       # q
        b'\x15'       # r
        b'\x16'       # s
        b'\x17'       # t
        b'\x18'       # u
        b'\x19'       # v
        b'\x1d'       # w
        b'\x1b'       # x
        b'\x1c'       # y
        b'\x1a'       # z
        b'\x22'    # {
        b'\x8f'    # |
        b'\x2d'    # }
        b'\x00'    # ~
        b'\x00'       # DEL
    )

    NEED_ALTGR = "[]\\{}|~€"
    HIGHER_ASCII = {
        "à": 0x27,  # à
        "ç": 0x26,  # ç
        "è": 0x24,  # è
        "é": 0x1F,  # é
        "ù": 0x34,  # ù
        "€": 0x30,  # € - altgr will be added thanks to NEED_ALTGR
        "°": 0xAD,  # °
        "§": 0x23,  # §
        "£": 0xB1,  # £
    }
    COMBINED_KEYS = {
        'ã': 0x11e1,
        'Ã': 0x11c1,
        'ñ': 0x11ee,
        'Ñ': 0x11ce,
        'õ': 0x11ef,
        'Õ': 0x11cf,
        '~': 0x11a0,
        'Ù': 0x3155,
        '`': 0x3120,
        'ì': 0x3169,
        'Ì': 0x3149,
        'ò': 0x316f,
        'Ò': 0x314f,
        'À': 0x3141,
        'È': 0x3145,
        'â': 0x2f61,
        'ê': 0x2f65,
        'î': 0x2f69,
        'ô': 0x2f6f,
        'û': 0x2f75,
        'Â': 0x2f41,
        'Ê': 0x2f45,
        'Î': 0x2f49,
        'Ô': 0x2f4f,
        'Û': 0x2f55,
        '^': 0x2f20,
        'ä': 0xaf61,
        'ë': 0xaf65,
        'ï': 0xaf69,
        'ö': 0xaf6f,
        'ü': 0xaf75,
        'ÿ': 0xaf79,
        'Ä': 0xaf41,
        'Ë': 0xaf45,
        'Ï': 0xaf49,
        'Ö': 0xaf4f,
        'Ü': 0xaf55,
        '¨': 0xaf20,
    }

