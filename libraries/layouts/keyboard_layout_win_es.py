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
        'ã': 0x21e1,
        'ñ': 0x21ee,
        'õ': 0x21ef,
        'Ã': 0x21c1,
        'Ñ': 0x21ce,
        'Õ': 0x21cf,
        '~': 0x21a0,
        'à': 0x2f61,
        'è': 0x2f65,
        'ì': 0x2f69,
        'ò': 0x2f6f,
        'ù': 0x2f75,
        'À': 0x2f41,
        'È': 0x2f45,
        'Ì': 0x2f49,
        'Ò': 0x2f4f,
        'Ù': 0x2f55,
        '`': 0x2f20,
        'â': 0xaf61,
        'ê': 0xaf65,
        'î': 0xaf69,
        'ô': 0xaf6f,
        'û': 0xaf75,
        'Â': 0xaf41,
        'Ê': 0xaf45,
        'Î': 0xaf49,
        'Ô': 0xaf4f,
        'Û': 0xaf55,
        '^': 0xaf20,
        'á': 0x3461,
        'é': 0x3465,
        'í': 0x3469,
        'ó': 0x346f,
        'ú': 0x3475,
        'ý': 0x3479,
        'Á': 0x3441,
        'É': 0x3445,
        'Í': 0x3449,
        'Ó': 0x344f,
        'Ú': 0x3455,
        'Ý': 0x3459,
        '´': 0x3420,
        'ä': 0xb461,
        'ë': 0xb465,
        'ï': 0xb469,
        'ö': 0xb46f,
        'ü': 0xb475,
        'ÿ': 0xb479,
        'Ä': 0xb441,
        'Ë': 0xb445,
        'Ï': 0xb449,
        'Ö': 0xb44f,
        'Ü': 0xb455,
        '¨': 0xb420,
    }
