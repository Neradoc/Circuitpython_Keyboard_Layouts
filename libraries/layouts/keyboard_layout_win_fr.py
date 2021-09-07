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
        b'\x38'  # '!'
        b'\x20'  # '"'
        b'\x20'  # '#'
        b'\x30'  # '$'
        b'\xb4'  # '%'
        b'\x1e'  # '&'
        b'\x21'  # "'"
        b'\x22'  # '('
        b'\x2d'  # ')'
        b'\x31'  # '*'
        b'\xae'  # '+'
        b'\x10'  # ','
        b'\x23'  # '-'
        b'\xb6'  # '.'
        b'\xb7'  # '/'
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
        b'\x37'  # ':'
        b'\x36'  # ';'
        b'\x64'  # '<'
        b'\x2e'  # '='
        b'\xe4'  # '>'
        b'\x90'  # '?'
        b'\x27'  # '@'
        b'\x94'  # 'A'
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
        b'\xb3'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x84'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9d'  # 'W'
        b'\x9b'  # 'X'
        b'\x9c'  # 'Y'
        b'\x9a'  # 'Z'
        b'\x22'  # '['
        b'\x25'  # '\\'
        b'\x2d'  # ']'
        b'\x26'  # '^'
        b'\x25'  # '_'
        b'\x00'  # '`' (Dead key)
        b'\x14'  # 'a'
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
        b'\x33'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x04'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1d'  # 'w'
        b'\x1b'  # 'x'
        b'\x1c'  # 'y'
        b'\x1a'  # 'z'
        b'\x21'  # '{'
        b'\x23'  # '|'
        b'\x2e'  # '}'
        b'\x00'  # '~' (Dead key)
        b'\x00'
    )
    NEED_ALTGR = '#@[\\]^{|}¤€'
    HIGHER_ASCII = {
        'é': 0x1f,
        'è': 0x24,
        'ç': 0x26,
        'à': 0x27,
        '°': 0xad,
        '€': 0x08,
        '£': 0xb0,
        '¤': 0x30,
        'ù': 0x34,
        '²': 0x35,
        'µ': 0xb1,
        '§': 0xb8,
    }
    COMBINED_KEYS = {
        'ã': b"\x1f\xe1",
        'Ã': b"\x1f\xc1",
        'ñ': b"\x1f\xee",
        'Ñ': b"\x1f\xce",
        'õ': b"\x1f\xef",
        'Õ': b"\x1f\xcf",
        '~': b"\x1f\xa0",
        'à': b"\x24\xe1",
        'è': b"\x24\xe5",
        'ì': b"\x24\xe9",
        'ò': b"\x24\xef",
        'ù': b"\x24\xf5",
        'À': b"\x24\xc1",
        'È': b"\x24\xc5",
        'Ì': b"\x24\xc9",
        'Ò': b"\x24\xcf",
        'Ù': b"\x24\xd5",
        '`': b"\x24\xa0",
        'â': b"\x2f\x61",
        'ê': b"\x2f\x65",
        'î': b"\x2f\x69",
        'ô': b"\x2f\x6f",
        'û': b"\x2f\x75",
        'Â': b"\x2f\x41",
        'Ê': b"\x2f\x45",
        'Î': b"\x2f\x49",
        'Ô': b"\x2f\x4f",
        'Û': b"\x2f\x55",
        '^': b"\x2f\x20",
        'ä': b"\xaf\x61",
        'ë': b"\xaf\x65",
        'ï': b"\xaf\x69",
        'ö': b"\xaf\x6f",
        'ü': b"\xaf\x75",
        'ÿ': b"\xaf\x79",
        'Ä': b"\xaf\x41",
        'Ë': b"\xaf\x45",
        'Ï': b"\xaf\x49",
        'Ö': b"\xaf\x4f",
        'Ü': b"\xaf\x55",
        '¨': b"\xaf\x20",
    }
