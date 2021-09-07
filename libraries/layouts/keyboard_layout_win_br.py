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
        b'\xb5'  # '"'
        b'\xa0'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa4'  # '&'
        b'\x35'  # "'"
        b'\xa6'  # '('
        b'\xa7'  # ')'
        b'\xa5'  # '*'
        b'\xae'  # '+'
        b'\x36'  # ','
        b'\x2d'  # '-'
        b'\x37'  # '.'
        b'\x14'  # '/'
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
        b'\x38'  # ';'
        b'\xb6'  # '<'
        b'\x2e'  # '='
        b'\xb7'  # '>'
        b'\x1a'  # '?'
        b'\x9f'  # '@'
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
        b'\x30'  # '['
        b'\x64'  # '\\'
        b'\x31'  # ']'
        b'\x00'
        b'\xad'  # '_'
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
        b'\xb0'  # '{'
        b'\xe4'  # '|'
        b'\xb1'  # '}'
        b'\x00'
        b'\x00'
    )
    NEED_ALTGR = '/?¢£§ª¬°²³¹º₢'
    HIGHER_ASCII = {
        '¹': 0x1e,
        '²': 0x1f,
        '³': 0x20,
        '£': 0x21,
        '¢': 0x22,
        '¬': 0x23,
        '§': 0x2e,
        '°': 0x08,
        'ª': 0x30,
        'ç': 0x33,
        'Ç': 0xb3,
        'º': 0x31,
        '₢': 0x06,
    }
    COMBINED_KEYS = {
        'ä': b"\xa3\x61",
        'ë': b"\xa3\x65",
        'ï': b"\xa3\x69",
        'ö': b"\xa3\x6f",
        'ü': b"\xa3\x75",
        'ÿ': b"\xa3\x79",
        'Ä': b"\xa3\x41",
        'Ë': b"\xa3\x45",
        'Ï': b"\xa3\x49",
        'Ö': b"\xa3\x4f",
        'Ü': b"\xa3\x55",
        '¨': b"\xa3\x20",
        'á': b"\x2f\x61",
        'é': b"\x2f\x65",
        'í': b"\x2f\x69",
        'ó': b"\x2f\x6f",
        'ú': b"\x2f\x75",
        'ý': b"\x2f\x79",
        'Á': b"\x2f\x41",
        'É': b"\x2f\x45",
        'Í': b"\x2f\x49",
        'Ó': b"\x2f\x4f",
        'Ú': b"\x2f\x55",
        'Ý': b"\x2f\x59",
        '´': b"\x2f\x20",
        'à': b"\xaf\x61",
        'è': b"\xaf\x65",
        'ì': b"\xaf\x69",
        'ò': b"\xaf\x6f",
        'ù': b"\xaf\x75",
        'À': b"\xaf\x41",
        'È': b"\xaf\x45",
        'Ì': b"\xaf\x49",
        'Ò': b"\xaf\x4f",
        'Ù': b"\xaf\x55",
        '`': b"\xaf\x20",
        'ã': b"\x34\x61",
        'õ': b"\x34\x6f",
        'ñ': b"\x34\x6e",
        'Ã': b"\x34\x41",
        'Õ': b"\x34\x4f",
        'Ñ': b"\x34\x4e",
        '~': b"\x34\x20",
        'â': b"\xb4\x61",
        'ê': b"\xb4\x65",
        'î': b"\xb4\x69",
        'ô': b"\xb4\x6f",
        'û': b"\xb4\x75",
        'Â': b"\xb4\x41",
        'Ê': b"\xb4\x45",
        'Î': b"\xb4\x49",
        'Ô': b"\xb4\x4f",
        'Û': b"\xb4\x55",
        '^': b"\xb4\x20",
    }
