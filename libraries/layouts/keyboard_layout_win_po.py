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
        'ä': 0x2fe1,
        'ë': 0x2fe5,
        'ï': 0x2fe9,
        'ö': 0x2fef,
        'ü': 0x2ff5,
        'ÿ': 0x2ff9,
        'Ä': 0x2fc1,
        'Ë': 0x2fc5,
        'Ï': 0x2fc9,
        'Ö': 0x2fcf,
        'Ü': 0x2fd5,
        '¨': 0x2fa0,
        'á': 0x3061,
        'é': 0x3065,
        'í': 0x3069,
        'ó': 0x306f,
        'ú': 0x3075,
        'ý': 0x3079,
        'Á': 0x3041,
        'É': 0x3045,
        'Í': 0x3049,
        'Ó': 0x304f,
        'Ú': 0x3055,
        'Ý': 0x3059,
        '´': 0x3020,
        'à': 0xb061,
        'è': 0xb065,
        'ì': 0xb069,
        'ò': 0xb06f,
        'ù': 0xb075,
        'À': 0xb041,
        'È': 0xb045,
        'Ì': 0xb049,
        'Ò': 0xb04f,
        'Ù': 0xb055,
        '`': 0xb020,
        'ã': 0x3161,
        'õ': 0x316f,
        'ñ': 0x316e,
        'Ã': 0x3141,
        'Õ': 0x314f,
        'Ñ': 0x314e,
        '~': 0x3120,
        'â': 0xb161,
        'ê': 0xb165,
        'î': 0xb169,
        'ô': 0xb16f,
        'û': 0xb175,
        'Â': 0xb141,
        'Ê': 0xb145,
        'Î': 0xb149,
        'Ô': 0xb14f,
        'Û': 0xb155,
        '^': 0xb120,
    }
