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
        b'\xa1'  # '!'
        b'\x9f'  # '"'
        b'\x1b'  # '#'
        b'\x33'  # '$'
        b'\xa2'  # '%'
        b'\x06'  # '&'
        b'\x9e'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\x38'  # '*'
        b'\xa0'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
        b'\xa3'  # '/'
        b'\x35'  # '0'
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
        b'\x36'  # ';'
        b'\x10'  # '<'
        b'\xa4'  # '='
        b'\x1d'  # '>'
        b'\xb6'  # '?'
        b'\x19'  # '@'
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
        b'\x09'  # '['
        b'\x14'  # '\\'
        b'\x0a'  # ']'
        b'\x00'  # '^' (Dead key)
        b'\xb8'  # '_'
        b'\x24'  # '`'
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
        b'\x05'  # '{'
        b'\x1a'  # '|'
        b'\x11'  # '}'
        b'\x1e'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '#$&*;<>@[\\]`{|}~¤ÄÍ×ßäí÷ĐđŁł€'
    HIGHER_ASCII = {
        'ö': 0x27,
        'Ö': 0xa7,
        'ü': 0x2d,
        'Ü': 0xad,
        'ó': 0x2e,
        'Ó': 0xae,
        'Ä': 0x08,
        '€': 0x18,
        'Í': 0x0c,
        'ő': 0x2f,
        'Ő': 0xaf,
        '÷': 0x2f,
        'ú': 0x30,
        'Ú': 0xb0,
        '×': 0x30,
        'ä': 0x04,
        'đ': 0x16,
        'Đ': 0x07,
        'í': 0x0d,
        'ł': 0x0e,
        'Ł': 0x0f,
        'é': 0x33,
        'É': 0xb3,
        'á': 0x34,
        'Á': 0xb4,
        'ß': 0x34,
        '§': 0xb5,
        'ű': 0x31,
        'Ű': 0xb1,
        '¤': 0x31,
    }
    COMBINED_KEYS = {
        'Ť': 0x1fd4,
        'Ž': 0x1fda,
        'Č': 0x1fc3,
        'Ě': 0x1fc5,
        'Ď': 0x1fc4,
        'Ř': 0x1fd2,
        'Š': 0x1fd3,
        'Ň': 0x1fce,
        'ť': 0x1ff4,
        'ž': 0x1ffa,
        'č': 0x1fe3,
        'ě': 0x1fe5,
        'ď': 0x1fe4,
        'ř': 0x1ff2,
        'š': 0x1ff3,
        'ň': 0x1fee,
        'ˇ': 0x1fa0,
        'Â': 0x20c1,
        'Î': 0x20c9,
        'Ô': 0x20cf,
        'â': 0x20e1,
        'î': 0x20e9,
        'ô': 0x20ef,
        '^': 0x20a0,
        'Ă': 0x21c1,
        'ă': 0x21e1,
        '˘': 0x21a0,
        'Ů': 0x22d5,
        'ů': 0x22f5,
        '°': 0x22a0,
        'Ą': 0x23c1,
        'Ę': 0x23c5,
        'ą': 0x23e1,
        'ę': 0x23e5,
        '˛': 0x23a0,
        'ż': 0x25fa,
        'Ż': 0x25da,
        '˙': 0x25a0,
        'Ŕ': 0x26d2,
        'Á': 0x26c1,
        'Ĺ': 0x26cc,
        'Ć': 0x26c3,
        'É': 0x26c5,
        'Í': 0x26c9,
        'Ń': 0x26ce,
        'Ó': 0x26cf,
        'Ú': 0x26d5,
        'Ý': 0x26d9,
        'Ś': 0x26d3,
        'Ź': 0x26da,
        'ŕ': 0x26f2,
        'á': 0x26e1,
        'ĺ': 0x26ec,
        'ć': 0x26e3,
        'é': 0x26e5,
        'í': 0x26e9,
        'ń': 0x26ee,
        'ó': 0x26ef,
        'ú': 0x26f5,
        'ý': 0x26f9,
        'ś': 0x26f3,
        'ź': 0x26fa,
        '´': 0x26a0,
        'Ő': 0x27cf,
        'Ű': 0x27d5,
        'ő': 0x27ef,
        'ű': 0x27f5,
        '˝': 0x27a0,
        'Ä': 0x2dc1,
        'Ë': 0x2dc5,
        'Ö': 0x2dcf,
        'Ü': 0x2dd5,
        'ä': 0x2de1,
        'ë': 0x2de5,
        'ö': 0x2def,
        'ü': 0x2df5,
        '¨': 0x2da0,
        'Ş': 0x2ed3,
        'Ç': 0x2ec3,
        'Ţ': 0x2ed4,
        'ş': 0x2ef3,
        'ç': 0x2ee3,
        'ţ': 0x2ef4,
        '¸': 0x2ea0,
    }
