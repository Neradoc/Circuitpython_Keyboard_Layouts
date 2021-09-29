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
        'ä': 0xa361,
        'ë': 0xa365,
        'ï': 0xa369,
        'ö': 0xa36f,
        'ü': 0xa375,
        'ÿ': 0xa379,
        'Ä': 0xa341,
        'Ë': 0xa345,
        'Ï': 0xa349,
        'Ö': 0xa34f,
        'Ü': 0xa355,
        '¨': 0xa320,
        'á': 0x2f61,
        'é': 0x2f65,
        'í': 0x2f69,
        'ó': 0x2f6f,
        'ú': 0x2f75,
        'ý': 0x2f79,
        'Á': 0x2f41,
        'É': 0x2f45,
        'Í': 0x2f49,
        'Ó': 0x2f4f,
        'Ú': 0x2f55,
        'Ý': 0x2f59,
        '´': 0x2f20,
        'à': 0xaf61,
        'è': 0xaf65,
        'ì': 0xaf69,
        'ò': 0xaf6f,
        'ù': 0xaf75,
        'À': 0xaf41,
        'È': 0xaf45,
        'Ì': 0xaf49,
        'Ò': 0xaf4f,
        'Ù': 0xaf55,
        '`': 0xaf20,
        'ã': 0x3461,
        'õ': 0x346f,
        'ñ': 0x346e,
        'Ã': 0x3441,
        'Õ': 0x344f,
        'Ñ': 0x344e,
        '~': 0x3420,
        'â': 0xb461,
        'ê': 0xb465,
        'î': 0xb469,
        'ô': 0xb46f,
        'û': 0xb475,
        'Â': 0xb441,
        'Ê': 0xb445,
        'Î': 0xb449,
        'Ô': 0xb44f,
        'Û': 0xb455,
        '^': 0xb420,
    }
