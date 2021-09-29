# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


from keyboard_layout import KeyboardLayoutBase
class KeyboardLayout(KeyboardLayoutBase):
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\x1e'  # '!'
        b'\xb3'  # '"'
        b'\x20'  # '#'
        b'\x21'  # '$'
        b'\x22'  # '%'
        b'\x24'  # '&'
        b'\xb1'  # "'"
        b'\x26'  # '('
        b'\x27'  # ')'
        b'\x25'  # '*'
        b'\x1e'  # '+'
        b'\x36'  # ','
        b'\x2d'  # '-'
        b'\x37'  # '.'
        b'\xaf'  # '/'
        b'\xa7'  # '0'
        b'\x9e'  # '1'
        b'\x9f'  # '2'
        b'\xa0'  # '3'
        b'\xa1'  # '4'
        b'\xa2'  # '5'
        b'\xa3'  # '6'
        b'\xa4'  # '7'
        b'\xa5'  # '8'
        b'\xa6'  # '9'
        b'\xb7'  # ':'
        b'\x33'  # ';'
        b'\x36'  # '<'
        b'\x2d'  # '='
        b'\x37'  # '>'
        b'\xb6'  # '?'
        b'\x1f'  # '@'
        b'\x84'  # 'A'
        b'\x85'  # 'B'
        b'\x86'  # 'C'
        b'\x87'  # 'D'
        b'\x88'  # 'E'
        b'\x89'  # 'F'
        b'\x8a'  # 'G'
        b'\x8b'  # 'H'
        b'\x8c'  # 'I'
        b'\x8d'  # 'J'
        b'\x8e'  # 'K'
        b'\x8f'  # 'L'
        b'\x90'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x94'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9a'  # 'W'
        b'\x9b'  # 'X'
        b'\x9c'  # 'Y'
        b'\x9d'  # 'Z'
        b'\x2f'  # '['
        b'\x31'  # '\\'
        b'\x30'  # ']'
        b'\x23'  # '^'
        b'\xb8'  # '_'
        b'\x35'  # '`'
        b'\x04'  # 'a'
        b'\x05'  # 'b'
        b'\x06'  # 'c'
        b'\x07'  # 'd'
        b'\x08'  # 'e'
        b'\x09'  # 'f'
        b'\x0a'  # 'g'
        b'\x0b'  # 'h'
        b'\x0c'  # 'i'
        b'\x0d'  # 'j'
        b'\x0e'  # 'k'
        b'\x0f'  # 'l'
        b'\x10'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x14'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1a'  # 'w'
        b'\x1b'  # 'x'
        b'\x1c'  # 'y'
        b'\x1d'  # 'z'
        b'\x00'
        b'\xe4'  # '|'
        b'\x00'
        b'\x00'
        b'\x00'
    )
    NEED_ALTGR = '!#$%&()*-;<>@[\\]^`¤ß€'
    HIGHER_ASCII = {
        'ě': 0x1f,
        'š': 0x20,
        'č': 0x21,
        'ř': 0x22,
        'ž': 0x23,
        'ý': 0x24,
        'á': 0x25,
        'í': 0x26,
        'é': 0x27,
        '€': 0x08,
        'ú': 0x2f,
        'ů': 0x33,
        '§': 0x34,
        '¤': 0x34,
        'ß': 0x64,
    }
    COMBINED_KEYS = {
        'á': 0x2e61,
        'Á': 0x2e41,
        'ś': 0x2e73,
        'Ś': 0x2e53,
        'ć': 0x2e63,
        'Ć': 0x2e43,
        'é': 0x2e65,
        'É': 0x2e45,
        'ŕ': 0x2e72,
        'Ŕ': 0x2e52,
        'í': 0x2e69,
        'Í': 0x2e49,
        'ó': 0x2e6f,
        'Ó': 0x2e4f,
        'ú': 0x2e75,
        'Ú': 0x2e55,
        'ý': 0x2e79,
        'Ý': 0x2e59,
        'ĺ': 0x2e6c,
        'Ĺ': 0x2e4c,
        'ń': 0x2e6e,
        'Ń': 0x2e4e,
        'ź': 0x2e7a,
        'Ź': 0x2e5a,
        '´': 0x2e20,
        'č': 0xae63,
        'Č': 0xae43,
        'ď': 0xae64,
        'Ď': 0xae44,
        'ě': 0xae65,
        'Ě': 0xae45,
        'ř': 0xae72,
        'Ř': 0xae52,
        'ľ': 0xae6c,
        'Ľ': 0xae4c,
        'ň': 0xae6e,
        'Ň': 0xae4e,
        'š': 0xae73,
        'Š': 0xae53,
        'ť': 0xae74,
        'Ť': 0xae54,
        'ž': 0xae7a,
        'Ž': 0xae5a,
        'ˇ': 0xae20,
        'å': 0xb561,
        'Å': 0xb541,
        'ů': 0xb575,
        'Ů': 0xb555,
        '°': 0xb520,
        'ä': 0x3161,
        'Ä': 0x3141,
        'ë': 0x3165,
        'Ë': 0x3145,
        'ï': 0x3169,
        'Ï': 0x3149,
        'ö': 0x316f,
        'Ö': 0x314f,
        'ü': 0x3175,
        'Ü': 0x3155,
        'ÿ': 0x3179,
        'Ÿ': 0x3159,
        '¨': 0x3120,
    }
