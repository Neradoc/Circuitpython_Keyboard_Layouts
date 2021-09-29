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
        b'\x35'  # '"'
        b'\x20'  # '#'
        b'\x21'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x9f'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\x2d'  # '*'
        b'\xa1'  # '+'
        b'\x31'  # ','
        b'\x2e'  # '-'
        b'\x38'  # '.'
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
        b'\xb8'  # ':'
        b'\xb1'  # ';'
        b'\x35'  # '<'
        b'\xa7'  # '='
        b'\x1e'  # '>'
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
        b'\x9c'  # 'Y'
        b'\x9d'  # 'Z'
        b'\x25'  # '['
        b'\x2d'  # '\\'
        b'\x26'  # ']'
        b'\x00'
        b'\xae'  # '_'
        b'\x00'  # '`' (Dead key)
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
    NEED_ALTGR = '#$<>@[\\]i{|}£½ßæ€₺'
    HIGHER_ASCII = {
        '£': 0x1f,
        '½': 0x22,
        '€': 0x08,
        '₺': 0x17,
        'ı': 0x0c,
        'ğ': 0x2f,
        'Ğ': 0xaf,
        'ü': 0x30,
        'Ü': 0xb0,
        'æ': 0x04,
        'ß': 0x16,
        'ş': 0x33,
        'Ş': 0xb3,
        'İ': 0xb4,
        'é': 0xb5,
        'ö': 0x36,
        'Ö': 0xb6,
        'ç': 0x37,
        'Ç': 0xb7,
    }
    COMBINED_KEYS = {
        'â': 0xa061,
        'ê': 0xa065,
        'î': 0xa0131,
        'ô': 0xa06f,
        'û': 0xa075,
        'Â': 0xa041,
        'Ê': 0xa045,
        'Î': 0xa0130,
        'Ô': 0xa04f,
        'Û': 0xa055,
        '^': 0xa020,
        'ä': 0x2fe1,
        'ë': 0x2fe5,
        'ï': 0x2f1b1,
        'ö': 0x2fef,
        'ü': 0x2ff5,
        'Ä': 0x2fc1,
        'Ë': 0x2fc5,
        'Ï': 0x2f1b0,
        'Ö': 0x2fcf,
        'Ü': 0x2fd5,
        '¨': 0x2fa0,
        'ã': 0x30e1,
        'õ': 0x30ef,
        'ñ': 0x30ee,
        'Ã': 0x30c1,
        'Õ': 0x30cf,
        'Ñ': 0x30ce,
        '~': 0x30a0,
        'á': 0x33e1,
        'é': 0x33e5,
        'í': 0x331b1,
        'ó': 0x33ef,
        'ú': 0x33f5,
        'Á': 0x33c1,
        'É': 0x33c5,
        'Í': 0x331b0,
        'Ó': 0x33cf,
        'Ú': 0x33d5,
        '´': 0x33a0,
        'à': 0x31e1,
        'è': 0x31e5,
        'ì': 0x311b1,
        'ò': 0x31ef,
        'ù': 0x31f5,
        'À': 0x31c1,
        'È': 0x31c5,
        'Ì': 0x311b0,
        'Ò': 0x31cf,
        'Ù': 0x31d5,
        '`': 0x31a0,
    }
