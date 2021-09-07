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
        b'\x64'  # '<'
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
        'Ť': b"\x1f\xd4",
        'Ž': b"\x1f\xda",
        'Č': b"\x1f\xc3",
        'Ě': b"\x1f\xc5",
        'Ď': b"\x1f\xc4",
        'Ř': b"\x1f\xd2",
        'Š': b"\x1f\xd3",
        'Ň': b"\x1f\xce",
        'ť': b"\x1f\xf4",
        'ž': b"\x1f\xfa",
        'č': b"\x1f\xe3",
        'ě': b"\x1f\xe5",
        'ď': b"\x1f\xe4",
        'ř': b"\x1f\xf2",
        'š': b"\x1f\xf3",
        'ň': b"\x1f\xee",
        'ˇ': b"\x1f\xa0",
        'Â': b"\x20\xc1",
        'Î': b"\x20\xc9",
        'Ô': b"\x20\xcf",
        'â': b"\x20\xe1",
        'î': b"\x20\xe9",
        'ô': b"\x20\xef",
        '^': b"\x20\xa0",
        'Ă': b"\x21\xc1",
        'ă': b"\x21\xe1",
        '˘': b"\x21\xa0",
        'Ů': b"\x22\xd5",
        'ů': b"\x22\xf5",
        '°': b"\x22\xa0",
        'Ą': b"\x23\xc1",
        'Ę': b"\x23\xc5",
        'ą': b"\x23\xe1",
        'ę': b"\x23\xe5",
        '˛': b"\x23\xa0",
        'ż': b"\x25\xfa",
        'Ż': b"\x25\xda",
        '˙': b"\x25\xa0",
        'Ŕ': b"\x26\xd2",
        'Á': b"\x26\xc1",
        'Ĺ': b"\x26\xcc",
        'Ć': b"\x26\xc3",
        'É': b"\x26\xc5",
        'Í': b"\x26\xc9",
        'Ń': b"\x26\xce",
        'Ó': b"\x26\xcf",
        'Ú': b"\x26\xd5",
        'Ý': b"\x26\xd9",
        'Ś': b"\x26\xd3",
        'Ź': b"\x26\xda",
        'ŕ': b"\x26\xf2",
        'á': b"\x26\xe1",
        'ĺ': b"\x26\xec",
        'ć': b"\x26\xe3",
        'é': b"\x26\xe5",
        'í': b"\x26\xe9",
        'ń': b"\x26\xee",
        'ó': b"\x26\xef",
        'ú': b"\x26\xf5",
        'ý': b"\x26\xf9",
        'ś': b"\x26\xf3",
        'ź': b"\x26\xfa",
        '´': b"\x26\xa0",
        'Ő': b"\x27\xcf",
        'Ű': b"\x27\xd5",
        'ő': b"\x27\xef",
        'ű': b"\x27\xf5",
        '˝': b"\x27\xa0",
        'Ä': b"\x2d\xc1",
        'Ë': b"\x2d\xc5",
        'Ö': b"\x2d\xcf",
        'Ü': b"\x2d\xd5",
        'ä': b"\x2d\xe1",
        'ë': b"\x2d\xe5",
        'ö': b"\x2d\xef",
        'ü': b"\x2d\xf5",
        '¨': b"\x2d\xa0",
        'Ş': b"\x2e\xd3",
        'Ç': b"\x2e\xc3",
        'Ţ': b"\x2e\xd4",
        'ş': b"\x2e\xf3",
        'ç': b"\x2e\xe3",
        'ţ': b"\x2e\xf4",
        '¸': b"\x2e\xa0",
    }
