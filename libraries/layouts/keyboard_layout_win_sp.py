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
        b'\x20'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x2d'  # "'"
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
        b'\x35'  # '\\'
        b'\x30'  # ']'
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
        b'\x34'  # '{'
        b'\x1e'  # '|'
        b'\x31'  # '}'
        b'\x00'  # '~' (Dead key)
        b'\x00'
    )
    NEED_ALTGR = '#@[\\]{|}¬€'
    HIGHER_ASCII = {
        '·': 0xa0,
        '€': 0x22,
        '¬': 0x23,
        '¡': 0x2e,
        '¿': 0xae,
        'ñ': 0x33,
        'Ñ': 0xb3,
        'º': 0x35,
        'ª': 0xb5,
        'ç': 0x31,
        'Ç': 0xb1,
    }
    COMBINED_KEYS = {
        'ã': b"\x21\xe1",
        'ñ': b"\x21\xee",
        'õ': b"\x21\xef",
        'Ã': b"\x21\xc1",
        'Ñ': b"\x21\xce",
        'Õ': b"\x21\xcf",
        '~': b"\x21\xa0",
        'à': b"\x2f\x61",
        'è': b"\x2f\x65",
        'ì': b"\x2f\x69",
        'ò': b"\x2f\x6f",
        'ù': b"\x2f\x75",
        'À': b"\x2f\x41",
        'È': b"\x2f\x45",
        'Ì': b"\x2f\x49",
        'Ò': b"\x2f\x4f",
        'Ù': b"\x2f\x55",
        '`': b"\x2f\x20",
        'â': b"\xaf\x61",
        'ê': b"\xaf\x65",
        'î': b"\xaf\x69",
        'ô': b"\xaf\x6f",
        'û': b"\xaf\x75",
        'Â': b"\xaf\x41",
        'Ê': b"\xaf\x45",
        'Î': b"\xaf\x49",
        'Ô': b"\xaf\x4f",
        'Û': b"\xaf\x55",
        '^': b"\xaf\x20",
        'á': b"\x34\x61",
        'é': b"\x34\x65",
        'í': b"\x34\x69",
        'ó': b"\x34\x6f",
        'ú': b"\x34\x75",
        'ý': b"\x34\x79",
        'Á': b"\x34\x41",
        'É': b"\x34\x45",
        'Í': b"\x34\x49",
        'Ó': b"\x34\x4f",
        'Ú': b"\x34\x55",
        'Ý': b"\x34\x59",
        '´': b"\x34\x20",
        'ä': b"\xb4\x61",
        'ë': b"\xb4\x65",
        'ï': b"\xb4\x69",
        'ö': b"\xb4\x6f",
        'ü': b"\xb4\x75",
        'ÿ': b"\xb4\x79",
        'Ä': b"\xb4\x41",
        'Ë': b"\xb4\x45",
        'Ï': b"\xb4\x49",
        'Ö': b"\xb4\x4f",
        'Ü': b"\xb4\x55",
        '¨': b"\xb4\x20",
    }
