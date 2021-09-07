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
        b'\xa0'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x2d'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xaf'  # '*'
        b'\x2f'  # '+'
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
        b'\x25'  # '['
        b'\x35'  # '\\'
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
        b'\x1c'  # 'y'
        b'\x1d'  # 'z'
        b'\x24'  # '{'
        b'\xb5'  # '|'
        b'\x27'  # '}'
        b'\x00'
        b'\x00'
    )
    NEED_ALTGR = '@[]{}£§€'
    HIGHER_ASCII = {
        '£': 0x20,
        '§': 0x21,
        '€': 0x22,
        '«': 0x2e,
        '»': 0xae,
        'ç': 0x33,
        'Ç': 0xb3,
        'º': 0x34,
        'ª': 0xb4,
    }
    COMBINED_KEYS = {
        'ä': b"\x2f\xe1",
        'ë': b"\x2f\xe5",
        'ï': b"\x2f\xe9",
        'ö': b"\x2f\xef",
        'ü': b"\x2f\xf5",
        'ÿ': b"\x2f\xf9",
        'Ä': b"\x2f\xc1",
        'Ë': b"\x2f\xc5",
        'Ï': b"\x2f\xc9",
        'Ö': b"\x2f\xcf",
        'Ü': b"\x2f\xd5",
        '¨': b"\x2f\xa0",
        'á': b"\x30\x61",
        'é': b"\x30\x65",
        'í': b"\x30\x69",
        'ó': b"\x30\x6f",
        'ú': b"\x30\x75",
        'ý': b"\x30\x79",
        'Á': b"\x30\x41",
        'É': b"\x30\x45",
        'Í': b"\x30\x49",
        'Ó': b"\x30\x4f",
        'Ú': b"\x30\x55",
        'Ý': b"\x30\x59",
        '´': b"\x30\x20",
        'à': b"\xb0\x61",
        'è': b"\xb0\x65",
        'ì': b"\xb0\x69",
        'ò': b"\xb0\x6f",
        'ù': b"\xb0\x75",
        'À': b"\xb0\x41",
        'È': b"\xb0\x45",
        'Ì': b"\xb0\x49",
        'Ò': b"\xb0\x4f",
        'Ù': b"\xb0\x55",
        '`': b"\xb0\x20",
        'ã': b"\x31\x61",
        'õ': b"\x31\x6f",
        'ñ': b"\x31\x6e",
        'Ã': b"\x31\x41",
        'Õ': b"\x31\x4f",
        'Ñ': b"\x31\x4e",
        '~': b"\x31\x20",
        'â': b"\xb1\x61",
        'ê': b"\xb1\x65",
        'î': b"\xb1\x69",
        'ô': b"\xb1\x6f",
        'û': b"\xb1\x75",
        'Â': b"\xb1\x41",
        'Ê': b"\xb1\x45",
        'Î': b"\xb1\x49",
        'Ô': b"\xb1\x4f",
        'Û': b"\xb1\x55",
        '^': b"\xb1\x20",
    }
