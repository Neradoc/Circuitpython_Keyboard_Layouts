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
        b'\x9f'  # '"'
        b'\x31'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\xb1'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xb0'  # '*'
        b'\x30'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
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
        b'\xb7'  # ':'
        b'\xb6'  # ';'
        b'\x64'  # '<'
        b'\xa7'  # '='
        b'\xe4'  # '>'
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
        b'\x9d'  # 'Y'
        b'\x9c'  # 'Z'
        b'\x25'  # '['
        b'\x2d'  # '\\'
        b'\x26'  # ']'
        b'\x00'
        b'\xb8'  # '_'
        b'\x00'
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
        b'\x1d'  # 'y'
        b'\x1c'  # 'z'
        b'\x24'  # '{'
        b'\x64'  # '|'
        b'\x27'  # '}'
        b'\x30'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '@[\\]{|}~²³µ€'
    HIGHER_ASCII = {
        '²': 0x1f,
        '§': 0xa0,
        '³': 0x20,
        'ß': 0x2d,
        '€': 0x08,
        'ü': 0x2f,
        'Ü': 0xaf,
        'ö': 0x33,
        'Ö': 0xb3,
        'ä': 0x34,
        'Ä': 0xb4,
        '°': 0xb5,
        'µ': 0x10,
    }
    COMBINED_KEYS = {
        'á': b"\x2e\x61",
        'é': b"\x2e\x65",
        'í': b"\x2e\x69",
        'ó': b"\x2e\x6f",
        'ú': b"\x2e\x75",
        'ý': b"\x2e\x79",
        'Á': b"\x2e\x41",
        'É': b"\x2e\x45",
        'Í': b"\x2e\x49",
        'Ó': b"\x2e\x4f",
        'Ú': b"\x2e\x55",
        'Ý': b"\x2e\x59",
        '´': b"\x2e\x20",
        'à': b"\xae\x61",
        'è': b"\xae\x65",
        'ì': b"\xae\x69",
        'ò': b"\xae\x6f",
        'ù': b"\xae\x75",
        'À': b"\xae\x41",
        'È': b"\xae\x45",
        'Ì': b"\xae\x49",
        'Ò': b"\xae\x4f",
        'Ù': b"\xae\x55",
        '`': b"\xae\x20",
        'â': b"\x35\x61",
        'ê': b"\x35\x65",
        'î': b"\x35\x69",
        'ô': b"\x35\x6f",
        'û': b"\x35\x75",
        'Â': b"\x35\x41",
        'Ê': b"\x35\x45",
        'Î': b"\x35\x49",
        'Ô': b"\x35\x4f",
        'Û': b"\x35\x55",
        '^': b"\x35\x20",
    }
