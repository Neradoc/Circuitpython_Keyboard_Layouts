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
        b'\x21'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x31'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xb1'  # '*'
        b'\x2d'  # '+'
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
        b'\x64'  # '\\'
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
        b'\x2e'  # '|'
        b'\x27'  # '}'
        b'\x00'  # '~' (Dead key)
        b'\x00'
    )
    NEED_ALTGR = '$@[\\]{|}£µ€'
    HIGHER_ASCII = {
        '£': 0x20,
        '¤': 0xa1,
        '€': 0x22,
        'å': 0x2f,
        'Å': 0xaf,
        'æ': 0x33,
        'Æ': 0xb3,
        'ø': 0x34,
        'Ø': 0xb4,
        '½': 0x35,
        '§': 0xb5,
        'µ': 0x10,
    }
    COMBINED_KEYS = {
        'á': 0x2e61,
        'é': 0x2e65,
        'í': 0x2e69,
        'ó': 0x2e6f,
        'ú': 0x2e75,
        'ý': 0x2e79,
        'Á': 0x2e41,
        'É': 0x2e45,
        'Í': 0x2e49,
        'Ó': 0x2e4f,
        'Ú': 0x2e55,
        'Ý': 0x2e59,
        '´': 0x2e20,
        'à': 0xae61,
        'è': 0xae65,
        'ì': 0xae69,
        'ò': 0xae6f,
        'ù': 0xae75,
        'À': 0xae41,
        'È': 0xae45,
        'Ì': 0xae49,
        'Ò': 0xae4f,
        'Ù': 0xae55,
        '`': 0xae20,
        'ä': 0x3061,
        'ë': 0x3065,
        'ï': 0x3069,
        'ö': 0x306f,
        'ü': 0x3075,
        'ÿ': 0x3079,
        'Ä': 0x3041,
        'Ë': 0x3045,
        'Ï': 0x3049,
        'Ö': 0x304f,
        'Ü': 0x3055,
        '¨': 0x3020,
        'â': 0xb061,
        'ê': 0xb065,
        'î': 0xb069,
        'ô': 0xb06f,
        'û': 0xb075,
        'Â': 0xb041,
        'Ê': 0xb045,
        'Î': 0xb049,
        'Ô': 0xb04f,
        'Û': 0xb055,
        '^': 0xb020,
        'ã': 0x30e1,
        'õ': 0x30ef,
        'ñ': 0x30ee,
        'Ã': 0x30c1,
        'Õ': 0x30cf,
        'Ñ': 0x30ce,
        '~': 0x30a0,
    }
