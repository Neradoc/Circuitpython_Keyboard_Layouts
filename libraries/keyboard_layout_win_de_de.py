# SPDX-FileCopyrightText: 2020, Bitboy85
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.de_de`
=======================================================
# The index of the array represents the 8-bit ascii code.
# The tupple of each index represents the keys needed to be pressed for this ascii character
# For example: on german layouts @ is written by ALT_R(AltGr) + q
# keycodes of 0x00 are ignored, those represent non-printable chars or characters
# which cannot be entered by key combination

* Author(s): Bitboy85
"""
#pylint: disable=duplicate-code


from keyboard_layout import KeyboardLayout


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayoutWinDeDe(KeyboardLayout):
    ASCII_TO_KEYCODE = (
        b"\x00"             # NUL
        b"\x00"             # SOH
        b"\x00"             # STX
        b"\x00"             # ETX
        b"\x00"             # EOT
        b"\x00"             # ENQ
        b"\x00"             # ACK
        b"\x00"             # BEL
        b"\x2a"             # BS	Backspace
        b"\x2b"             # TAB	Tab
        b"\x28"             # LF	Enter
        b"\x00"             # VT
        b"\x00"             # FF
        b"\x00"             # CR
        b"\x00"             # SO
        b"\x00"             # SI
        b"\x00"             # DEL
        b"\x00"             # DC1
        b"\x00"             # DC2
        b"\x00"             # DC3
        b"\x00"             # DC4
        b"\x00"             # NAK
        b"\x00"             # SYN
        b"\x00"             # ETB
        b"\x00"             # CAN
        b"\x00"             # EM
        b"\x00"             # SUB
        b"\x00"             # ESC
        b"\x00"             # FS
        b"\x00"             # GS
        b"\x00"             # RS
        b"\x00"             # US

        b"\x2c"		                    # SPACE
        b"\x9e"	    # !
        b"\x9f"	    # "
        b"\x31"                         # #
        b"\xa1"     # $
        b"\xa2"     # %
        b"\xa3"     # &
        b"\xb1"     # '
        b"\xa5"     # (
        b"\xa6"     # )
        b"\xb0"     # *
        b"\x30"                         # +
        b"\x36"                         # ,
        b"\x38"                         # -
        b"\x37"                         # .
        b"\xa4"     # /
        b"\x27"                         # 0
        b"\x1e"                         # 1
        b"\x1f"                         # 2
        b"\x20"                         # 3
        b"\x21"                         # 4
        b"\x22"                         # 5
        b"\x23"                         # 6
        b"\x24"                         # 7
        b"\x25"                         # 8
        b"\x26"                         # 9
        b"\xb7"     # :
        b"\xb6"     # ;
        b"\x64"                         # <
        b"\xa7"     # =
        b"\xe4"     # >
        b"\xad"     # ?
        b"\x14",      # @
        b"\x84"     # A
        b"\x85"     # B
        b"\x86"     # C
        b"\x87"     # D
        b"\x88"     # E
        b"\x89"     # F
        b"\x8a"     # G
        b"\x8b"     # H
        b"\x8c"     # I
        b"\x8d"     # J
        b"\x8e"     # K
        b"\x8f"     # L
        b"\x90"     # M
        b"\x91"     # N
        b"\x92"     # O
        b"\x93"     # P
        b"\x94"     # Q
        b"\x95"     # R
        b"\x96"     # S
        b"\x97"     # T
        b"\x98"     # U
        b"\x99"     # V
        b"\x9a"     # W
        b"\x9b"     # X
        b"\x9d"     # Y
        b"\x9c"     # Z
        b"\x25",      # [
        b"\x2d",      # bslash \
        b"\x26",      # ]
        b"\x35"                         # ^
        b"\xb8"     # _
        b"\xae"     # `
        b"\x04"                         # a
        b"\x05"                         # b
        b"\x06"                         # c
        b"\x07"                         # d
        b"\x08"                         # e
        b"\x09"                         # f
        b"\x0a"                         # g
        b"\x0b"                         # h
        b"\x0c"                         # i
        b"\x0d"                         # j
        b"\x0e"                         # k
        b"\x0f"                         # l
        b"\x10"                         # m
        b"\x11"                         # n
        b"\x12"                         # o
        b"\x13"                         # p
        b"\x14"                         # q
        b"\x15"                         # r
        b"\x16"                         # s
        b"\x17"                         # t
        b"\x18"                         # u
        b"\x19"                         # v
        b"\x1a"                         # w
        b"\x1b"                         # x
        b"\x1d"                         # y
        b"\x1c"                         # z
        b"\x24",      # {
        b"\x64",      # |
        b"\x27",      # }
        b"\x30",      # ~
        b"\x4c"				            # DEL
        b"\x00" # [NOT printable] in some docs shown as € symbol, but not so in python
        b"\x00" # [not printable]
        b"\x00" # ‚
        b"\x00" # ƒ
        b"\x00" # „
        b"\x00" # …
        b"\x00" # †
        b"\x00" # ‡
        b"\x00" # ˆ
        b"\x00" # ‰
        b"\x00" # Š
        b"\x00" # ‹
        b"\x00" # Œ
        b"\x00" # 
        b"\x00" # Ž
        b"\x00" # [not printable]
        b"\x00" # [not printable]
        b"\x00" # ‘
        b"\x00" # ’
        b"\x00" # “
        b"\x00" # ”
        b"\x00" # •
        b"\x00" # –
        b"\x00" # —
        b"\x00" # ˜
        b"\x00" # ™
        b"\x00" # š
        b"\x00" # ›
        b"\x00" # œ
        b"\x00" # [not printable]
        b"\x00" # ž
        b"\x00" # Ÿ
        b"\x00" # [not printable]
        b"\x00" # ¡
        b"\x00" # ¢
        b"\x00" # £
        b"\x00" # ¤
        b"\x00" # ¥
        b"\x00" # ¦
        b"\xa0"     # §
        b"\x00" # ¨
        b"\x00" # ©
        b"\x00" # ª
        b"\x00" # «
        b"\x00" # ¬
        b"\x00" # [not printable]
        b"\x00" # ®
        b"\x00" # ¯
        b"\xb5"     # °
        b"\x00" # ±
        b"\x1f",      # ²
        b"\x20",      # ³
        b"\x2e"                         # ´
        b"\x10",      # µ
        b"\x00" # ¶
        b"\x00" # ·
        b"\x00" # ¸
        b"\x00" # ¹
        b"\x00" # º
        b"\x00" # »
        b"\x00" # ¼
        b"\x00" # ½
        b"\x00" # ¾
        b"\x00" # ¿
        b"\x00" # À
        b"\x00" # Á
        b"\x00" # Â
        b"\x00" # Ã
        b"\xb4"     # Ä
        b"\x00" # Å
        b"\x00" # Æ
        b"\x00" # Ç
        b"\x00" # È
        b"\x00" # É
        b"\x00" # Ê
        b"\x00" # Ë
        b"\x00" # Ì
        b"\x00" # Í
        b"\x00" # Î
        b"\x00" # Ï
        b"\x00" # Ð
        b"\x00" # Ñ
        b"\x00" # Ò
        b"\x00" # Ó
        b"\x00" # Ô
        b"\x00" # Õ
        b"\xb3"     # Ö
        b"\x00" # ×
        b"\x00" # Ø
        b"\x00" # Ù
        b"\x00" # Ú
        b"\x00" # Û
        b"\xaf"     # Ü
        b"\x00" # Ý
        b"\x00" # Þ
        b"\x2d"                         # ß
        b"\x00" # à
        b"\x00" # á
        b"\x00" # â
        b"\x00" # ã
        b"\x34"                         # ä
        b"\x00" # å
        b"\x00" # æ
        b"\x00" # ç
        b"\x00" # è
        b"\x00" # é
        b"\x00" # ê
        b"\x00" # ë
        b"\x00" # ì
        b"\x00" # í
        b"\x00" # î
        b"\x00" # ï
        b"\x00" # ð
        b"\x00" # ñ
        b"\x00" # ò
        b"\x00" # ó
        b"\x00" # ô
        b"\x00" # õ
        b"\x33"                         # ö
        b"\x00" # ÷
        b"\x00" # ø
        b"\x00" # ù
        b"\x00" # ú
        b"\x00" # û
        b"\x2f"                         # ü
        b"\x00" # ý
        b"\x00" # þ
        b"\x00" # ÿ
    )

    NEED_ALTGR = "@[\\]{|}~²³µ"
