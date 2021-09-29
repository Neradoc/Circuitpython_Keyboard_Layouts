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
        'ã': 0x1fe1,
        'Ã': 0x1fc1,
        'ñ': 0x1fee,
        'Ñ': 0x1fce,
        'õ': 0x1fef,
        'Õ': 0x1fcf,
        '~': 0x1fa0,
        'à': 0x24e1,
        'è': 0x24e5,
        'ì': 0x24e9,
        'ò': 0x24ef,
        'ù': 0x24f5,
        'À': 0x24c1,
        'È': 0x24c5,
        'Ì': 0x24c9,
        'Ò': 0x24cf,
        'Ù': 0x24d5,
        '`': 0x24a0,
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
