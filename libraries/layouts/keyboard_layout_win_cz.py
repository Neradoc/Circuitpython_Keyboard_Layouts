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
        'č': 0x1fe3,
        'Č': 0x1fc3,
        'ď': 0x1fe4,
        'Ď': 0x1fc4,
        'ě': 0x1fe5,
        'Ě': 0x1fc5,
        'ľ': 0x1fec,
        'Ľ': 0x1fcc,
        'ň': 0x1fee,
        'Ň': 0x1fce,
        'ř': 0x1ff2,
        'Ř': 0x1fd2,
        'š': 0x1ff3,
        'Š': 0x1fd3,
        'ť': 0x1ff4,
        'Ť': 0x1fd4,
        'ž': 0x1ffa,
        'Ž': 0x1fda,
        'ˇ': 0x1fa0,
        'â': 0x20e1,
        'Â': 0x20c1,
        'ê': 0x20e5,
        'Ê': 0x20c5,
        'î': 0x20e9,
        'Î': 0x20c9,
        'ô': 0x20ef,
        'Ô': 0x20cf,
        'û': 0x20f5,
        'Û': 0x20d5,
        '^': 0x20a0,
        'ă': 0x21e1,
        'Ă': 0x21c1,
        'ğ': 0x21e7,
        'Ğ': 0x21c7,
        '˘': 0x21a0,
        'å': 0x22e1,
        'Å': 0x22c1,
        'ů': 0x22f5,
        'Ů': 0x22d5,
        '°': 0x22a0,
        'ą': 0x23e1,
        'Ą': 0x23c1,
        'ę': 0x23e5,
        'Ę': 0x23c5,
        'į': 0x23e9,
        'Į': 0x23c9,
        'ų': 0x23f5,
        'Ų': 0x23d5,
        '˛': 0x23a0,
        'à': 0x24e1,
        'À': 0x24c1,
        'è': 0x24e5,
        'È': 0x24c5,
        'ì': 0x24e9,
        'Ì': 0x24c9,
        'ò': 0x24ef,
        'Ò': 0x24cf,
        'ù': 0x24f5,
        'Ù': 0x24d5,
        '`': 0x24a0,
        'ė': 0x25e5,
        'Ė': 0x25c5,
        'ı': 0x25e9,
        'İ': 0x25c9,
        'ż': 0x25fa,
        'Ż': 0x25da,
        '·': 0x25a0,
        'á': 0x26e1,
        'Á': 0x26c1,
        'ć': 0x26e3,
        'Ć': 0x26c3,
        'é': 0x26e5,
        'É': 0x26c5,
        'í': 0x26e9,
        'Í': 0x26c9,
        'ĺ': 0x26ec,
        'Ĺ': 0x26cc,
        'ń': 0x26ee,
        'Ń': 0x26ce,
        'ó': 0x26ef,
        'Ó': 0x26cf,
        'ŕ': 0x26f2,
        'Ŕ': 0x26d2,
        'ś': 0x26f3,
        'Ś': 0x26d3,
        'ú': 0x26f5,
        'Ú': 0x26d5,
        'ý': 0x26f9,
        'Ý': 0x26d9,
        'ź': 0x26fa,
        'Ź': 0x26da,
        '´': 0x26a0,
        'ő': 0x27ef,
        'Ő': 0x27cf,
        'ű': 0x27f5,
        'Ű': 0x27d5,
        '˝': 0x27a0,
        'ä': 0x2de1,
        'Ä': 0x2dc1,
        'ë': 0x2de5,
        'Ë': 0x2dc5,
        'ï': 0x2de9,
        'Ï': 0x2dc9,
        'ö': 0x2def,
        'Ö': 0x2dcf,
        'ü': 0x2df5,
        'Ü': 0x2dd5,
        'ÿ': 0x2df9,
        'Ÿ': 0x2dd9,
        '¨': 0x2da0,
        'ç': 0x2ee3,
        'Ç': 0x2ec3,
        'ģ': 0x2ee7,
        'Ģ': 0x2ec7,
        'ķ': 0x2eeb,
        'Ķ': 0x2ecb,
        'ļ': 0x2eec,
        'Ļ': 0x2ecc,
        'ņ': 0x2eee,
        'Ņ': 0x2ece,
        'ŗ': 0x2ef2,
        'Ŗ': 0x2ed2,
        'ş': 0x2ef3,
        'Ş': 0x2ed3,
        'ţ': 0x2ef4,
        'Ţ': 0x2ed4,
        '¸': 0x2ea0,
    }
