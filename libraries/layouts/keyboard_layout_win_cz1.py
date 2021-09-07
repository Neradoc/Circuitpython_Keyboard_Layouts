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
        b'\x1e'  # '!'
        b'\xb3'  # '"'
        b'\x20'  # '#'
        b'\x21'  # '$'
        b'\x22'  # '%'
        b'\x24'  # '&'
        b'\xb1'  # "'"
        b'\x26'  # '('
        b'\x27'  # ')'
        b'\x25'  # '*'
        b'\x1e'  # '+'
        b'\x36'  # ','
        b'\x2d'  # '-'
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
        b'\x33'  # ';'
        b'\x36'  # '<'
        b'\x2d'  # '='
        b'\x37'  # '>'
        b'\xb6'  # '?'
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
        b'\x31'  # '\\'
        b'\x30'  # ']'
        b'\x23'  # '^'
        b'\xb8'  # '_'
        b'\x35'  # '`'
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
        b'\x00'
        b'\xe4'  # '|'
        b'\x00'
        b'\x00'
        b'\x00'
    )
    NEED_ALTGR = '!#$%&()*-;<>@[\\]^`¤ß€'
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
        'ů': 0x33,
        '§': 0x34,
        '¤': 0x34,
        'ß': 0x64,
    }
    COMBINED_KEYS = {
        'á': b"\x2e\x61",
        'Á': b"\x2e\x41",
        'ś': b"\x2e\x73",
        'Ś': b"\x2e\x53",
        'ć': b"\x2e\x63",
        'Ć': b"\x2e\x43",
        'é': b"\x2e\x65",
        'É': b"\x2e\x45",
        'ŕ': b"\x2e\x72",
        'Ŕ': b"\x2e\x52",
        'í': b"\x2e\x69",
        'Í': b"\x2e\x49",
        'ó': b"\x2e\x6f",
        'Ó': b"\x2e\x4f",
        'ú': b"\x2e\x75",
        'Ú': b"\x2e\x55",
        'ý': b"\x2e\x79",
        'Ý': b"\x2e\x59",
        'ĺ': b"\x2e\x6c",
        'Ĺ': b"\x2e\x4c",
        'ń': b"\x2e\x6e",
        'Ń': b"\x2e\x4e",
        'ź': b"\x2e\x7a",
        'Ź': b"\x2e\x5a",
        '´': b"\x2e\x20",
        'č': b"\xae\x63",
        'Č': b"\xae\x43",
        'ď': b"\xae\x64",
        'Ď': b"\xae\x44",
        'ě': b"\xae\x65",
        'Ě': b"\xae\x45",
        'ř': b"\xae\x72",
        'Ř': b"\xae\x52",
        'ľ': b"\xae\x6c",
        'Ľ': b"\xae\x4c",
        'ň': b"\xae\x6e",
        'Ň': b"\xae\x4e",
        'š': b"\xae\x73",
        'Š': b"\xae\x53",
        'ť': b"\xae\x74",
        'Ť': b"\xae\x54",
        'ž': b"\xae\x7a",
        'Ž': b"\xae\x5a",
        'ˇ': b"\xae\x20",
        'å': b"\xb5\x61",
        'Å': b"\xb5\x41",
        'ů': b"\xb5\x75",
        'Ů': b"\xb5\x55",
        '°': b"\xb5\x20",
        'ä': b"\x31\x61",
        'Ä': b"\x31\x41",
        'ë': b"\x31\x65",
        'Ë': b"\x31\x45",
        'ï': b"\x31\x69",
        'Ï': b"\x31\x49",
        'ö': b"\x31\x6f",
        'Ö': b"\x31\x4f",
        'ü': b"\x31\x75",
        'Ü': b"\x31\x55",
        'ÿ': b"\x31\x79",
        'Ÿ': b"\x31\x59",
        '¨': b"\x31\x20",
    }
