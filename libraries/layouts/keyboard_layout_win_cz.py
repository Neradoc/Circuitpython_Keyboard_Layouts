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
        b'\xb4'  # '!'
        b'\xb3'  # '"'
        b'\x1b'  # '#'
        b'\x33'  # '$'
        b'\xad'  # '%'
        b'\x06'  # '&'
        b'\xb1'  # "'"
        b'\xb0'  # '('
        b'\x30'  # ')'
        b'\x38'  # '*'
        b'\x1e'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
        b'\xaf'  # '/'
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
        b'\xb7'  # ':'
        b'\x35'  # ';'
        b'\x36'  # '<'
        b'\x2d'  # '='
        b'\x37'  # '>'
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
        b'\x1d'  # 'y'
        b'\x1c'  # 'z'
        b'\x05'  # '{'
        b'\x1a'  # '|'
        b'\x11'  # '}'
        b'\x1e'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '#$&*<>@[\\]{|}~¤×ß÷ĐđŁł€'
    HIGHER_ASCII = {
        'ě': 0x1f,
        'š': 0x20,
        'č': 0x21,
        'ř': 0x22,
        'ž': 0x23,
        'ý': 0x24,
        'á': 0x25,
        'í': 0x26,
        'é': 0x27,
        '€': 0x08,
        'ú': 0x2f,
        '÷': 0x2f,
        '×': 0x30,
        'đ': 0x16,
        'Đ': 0x07,
        'ł': 0x0e,
        'Ł': 0x0f,
        'ů': 0x33,
        '§': 0x34,
        'ß': 0x34,
        '¤': 0x31,
    }
    COMBINED_KEYS = {
        'č': b"\x1f\xe3",
        'Č': b"\x1f\xc3",
        'ď': b"\x1f\xe4",
        'Ď': b"\x1f\xc4",
        'ě': b"\x1f\xe5",
        'Ě': b"\x1f\xc5",
        'ľ': b"\x1f\xec",
        'Ľ': b"\x1f\xcc",
        'ň': b"\x1f\xee",
        'Ň': b"\x1f\xce",
        'ř': b"\x1f\xf2",
        'Ř': b"\x1f\xd2",
        'š': b"\x1f\xf3",
        'Š': b"\x1f\xd3",
        'ť': b"\x1f\xf4",
        'Ť': b"\x1f\xd4",
        'ž': b"\x1f\xfa",
        'Ž': b"\x1f\xda",
        'ˇ': b"\x1f\xa0",
        'â': b"\x20\xe1",
        'Â': b"\x20\xc1",
        'ê': b"\x20\xe5",
        'Ê': b"\x20\xc5",
        'î': b"\x20\xe9",
        'Î': b"\x20\xc9",
        'ô': b"\x20\xef",
        'Ô': b"\x20\xcf",
        'û': b"\x20\xf5",
        'Û': b"\x20\xd5",
        '^': b"\x20\xa0",
        'ă': b"\x21\xe1",
        'Ă': b"\x21\xc1",
        'ğ': b"\x21\xe7",
        'Ğ': b"\x21\xc7",
        '˘': b"\x21\xa0",
        'å': b"\x22\xe1",
        'Å': b"\x22\xc1",
        'ů': b"\x22\xf5",
        'Ů': b"\x22\xd5",
        '°': b"\x22\xa0",
        'ą': b"\x23\xe1",
        'Ą': b"\x23\xc1",
        'ę': b"\x23\xe5",
        'Ę': b"\x23\xc5",
        'į': b"\x23\xe9",
        'Į': b"\x23\xc9",
        'ų': b"\x23\xf5",
        'Ų': b"\x23\xd5",
        '˛': b"\x23\xa0",
        'à': b"\x24\xe1",
        'À': b"\x24\xc1",
        'è': b"\x24\xe5",
        'È': b"\x24\xc5",
        'ì': b"\x24\xe9",
        'Ì': b"\x24\xc9",
        'ò': b"\x24\xef",
        'Ò': b"\x24\xcf",
        'ù': b"\x24\xf5",
        'Ù': b"\x24\xd5",
        '`': b"\x24\xa0",
        'ė': b"\x25\xe5",
        'Ė': b"\x25\xc5",
        'ı': b"\x25\xe9",
        'İ': b"\x25\xc9",
        'ż': b"\x25\xfa",
        'Ż': b"\x25\xda",
        '·': b"\x25\xa0",
        'á': b"\x26\xe1",
        'Á': b"\x26\xc1",
        'ć': b"\x26\xe3",
        'Ć': b"\x26\xc3",
        'é': b"\x26\xe5",
        'É': b"\x26\xc5",
        'í': b"\x26\xe9",
        'Í': b"\x26\xc9",
        'ĺ': b"\x26\xec",
        'Ĺ': b"\x26\xcc",
        'ń': b"\x26\xee",
        'Ń': b"\x26\xce",
        'ó': b"\x26\xef",
        'Ó': b"\x26\xcf",
        'ŕ': b"\x26\xf2",
        'Ŕ': b"\x26\xd2",
        'ś': b"\x26\xf3",
        'Ś': b"\x26\xd3",
        'ú': b"\x26\xf5",
        'Ú': b"\x26\xd5",
        'ý': b"\x26\xf9",
        'Ý': b"\x26\xd9",
        'ź': b"\x26\xfa",
        'Ź': b"\x26\xda",
        '´': b"\x26\xa0",
        'ő': b"\x27\xef",
        'Ő': b"\x27\xcf",
        'ű': b"\x27\xf5",
        'Ű': b"\x27\xd5",
        '˝': b"\x27\xa0",
        'ä': b"\x2d\xe1",
        'Ä': b"\x2d\xc1",
        'ë': b"\x2d\xe5",
        'Ë': b"\x2d\xc5",
        'ï': b"\x2d\xe9",
        'Ï': b"\x2d\xc9",
        'ö': b"\x2d\xef",
        'Ö': b"\x2d\xcf",
        'ü': b"\x2d\xf5",
        'Ü': b"\x2d\xd5",
        'ÿ': b"\x2d\xf9",
        'Ÿ': b"\x2d\xd9",
        '¨': b"\x2d\xa0",
        'ç': b"\x2e\xe3",
        'Ç': b"\x2e\xc3",
        'ģ': b"\x2e\xe7",
        'Ģ': b"\x2e\xc7",
        'ķ': b"\x2e\xeb",
        'Ķ': b"\x2e\xcb",
        'ļ': b"\x2e\xec",
        'Ļ': b"\x2e\xcc",
        'ņ': b"\x2e\xee",
        'Ņ': b"\x2e\xce",
        'ŗ': b"\x2e\xf2",
        'Ŗ': b"\x2e\xd2",
        'ş': b"\x2e\xf3",
        'Ş': b"\x2e\xd3",
        'ţ': b"\x2e\xf4",
        'Ţ': b"\x2e\xd4",
        '¸': b"\x2e\xa0",
    }
