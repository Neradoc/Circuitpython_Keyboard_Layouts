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
        b'\x9e'  # '!'
        b'\x35'  # '"'
        b'\x20'  # '#'
        b'\x21'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x9f'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\x2d'  # '*'
        b'\xa1'  # '+'
        b'\x31'  # ','
        b'\x2e'  # '-'
        b'\x38'  # '.'
        b'\xa4'  # '/'
        b'\x27'  # '0'
        b'\x1e'  # '1'
        b'\x1f'  # '2'
        b'\x20'  # '3'
        b'\x21'  # '4'
        b'\x22'  # '5'
        b'\x23'  # '6'
        b'\x24'  # '7'
        b'\x25'  # '8'
        b'\x26'  # '9'
        b'\xb8'  # ':'
        b'\xb1'  # ';'
        b'\x35'  # '<'
        b'\xa7'  # '='
        b'\x1e'  # '>'
        b'\xad'  # '?'
        b'\x14'  # '@'
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
        b'\x25'  # '['
        b'\x2d'  # '\\'
        b'\x26'  # ']'
        b'\x00'
        b'\xae'  # '_'
        b'\x00'  # '`' (Dead key)
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
        b'\x24'  # '{'
        b'\x2e'  # '|'
        b'\x27'  # '}'
        b'\x00'  # '~' (Dead key)
        b'\x00'
    )
    NEED_ALTGR = '#$<>@[\\]i{|}£½ßæ€₺'
    HIGHER_ASCII = {
        '£': 0x1f,
        '½': 0x22,
        '€': 0x08,
        '₺': 0x17,
        'ı': 0x0c,
        'ğ': 0x2f,
        'Ğ': 0xaf,
        'ü': 0x30,
        'Ü': 0xb0,
        'æ': 0x04,
        'ß': 0x16,
        'ş': 0x33,
        'Ş': 0xb3,
        'İ': 0xb4,
        'é': 0xb5,
        'ö': 0x36,
        'Ö': 0xb6,
        'ç': 0x37,
        'Ç': 0xb7,
    }
    COMBINED_KEYS = {
        'â': b"\xa0\x61",
        'ê': b"\xa0\x65",
        'î': b"\xa0\x131",
        'ô': b"\xa0\x6f",
        'û': b"\xa0\x75",
        'Â': b"\xa0\x41",
        'Ê': b"\xa0\x45",
        'Î': b"\xa0\x130",
        'Ô': b"\xa0\x4f",
        'Û': b"\xa0\x55",
        '^': b"\xa0\x20",
        'ä': b"\x2f\xe1",
        'ë': b"\x2f\xe5",
        'ï': b"\x2f\x1b1",
        'ö': b"\x2f\xef",
        'ü': b"\x2f\xf5",
        'Ä': b"\x2f\xc1",
        'Ë': b"\x2f\xc5",
        'Ï': b"\x2f\x1b0",
        'Ö': b"\x2f\xcf",
        'Ü': b"\x2f\xd5",
        '¨': b"\x2f\xa0",
        'ã': b"\x30\xe1",
        'õ': b"\x30\xef",
        'ñ': b"\x30\xee",
        'Ã': b"\x30\xc1",
        'Õ': b"\x30\xcf",
        'Ñ': b"\x30\xce",
        '~': b"\x30\xa0",
        'á': b"\x33\xe1",
        'é': b"\x33\xe5",
        'í': b"\x33\x1b1",
        'ó': b"\x33\xef",
        'ú': b"\x33\xf5",
        'Á': b"\x33\xc1",
        'É': b"\x33\xc5",
        'Í': b"\x33\x1b0",
        'Ó': b"\x33\xcf",
        'Ú': b"\x33\xd5",
        '´': b"\x33\xa0",
        'à': b"\x31\xe1",
        'è': b"\x31\xe5",
        'ì': b"\x31\x1b1",
        'ò': b"\x31\xef",
        'ù': b"\x31\xf5",
        'À': b"\x31\xc1",
        'È': b"\x31\xc5",
        'Ì': b"\x31\x1b0",
        'Ò': b"\x31\xcf",
        'Ù': b"\x31\xd5",
        '`': b"\x31\xa0",
    }
