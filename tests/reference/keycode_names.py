keycode_names = {
    "MOD_LCTRL": 0x01,
    "MOD_LSHIFT": 0x02,
    "MOD_LALT": 0x04,
    "MOD_LMETA": 0x08,
    "MOD_RCTRL": 0x10,
    "MOD_RSHIFT": 0x20,
    "MOD_RALT": 0x40,
    "MOD_RMETA": 0x80,
    # Letters
    "A": 0x04,  # Keyboard a and A
    "B": 0x05,  # Keyboard b and B
    "C": 0x06,  # Keyboard c and C
    "D": 0x07,  # Keyboard d and D
    "E": 0x08,  # Keyboard e and E
    "F": 0x09,  # Keyboard f and F
    "G": 0x0A,  # Keyboard g and G
    "H": 0x0B,  # Keyboard h and H
    "I": 0x0C,  # Keyboard i and I
    "J": 0x0D,  # Keyboard j and J
    "K": 0x0E,  # Keyboard k and K
    "L": 0x0F,  # Keyboard l and L
    "M": 0x10,  # Keyboard m and M
    "N": 0x11,  # Keyboard n and N
    "O": 0x12,  # Keyboard o and O
    "P": 0x13,  # Keyboard p and P
    "Q": 0x14,  # Keyboard q and Q
    "R": 0x15,  # Keyboard r and R
    "S": 0x16,  # Keyboard s and S
    "T": 0x17,  # Keyboard t and T
    "U": 0x18,  # Keyboard u and U
    "V": 0x19,  # Keyboard v and V
    "W": 0x1A,  # Keyboard w and W
    "X": 0x1B,  # Keyboard x and X
    "Y": 0x1C,  # Keyboard y and Y
    "Z": 0x1D,  # Keyboard z and Z
    # Numbers
    "1": 0x1E,  # Keyboard 1 and !
    "2": 0x1F,  # Keyboard 2 and @
    "3": 0x20,  # Keyboard 3 and #
    "4": 0x21,  # Keyboard 4 and $
    "5": 0x22,  # Keyboard 5 and %
    "6": 0x23,  # Keyboard 6 and ^
    "7": 0x24,  # Keyboard 7 and &
    "8": 0x25,  # Keyboard 8 and *
    "9": 0x26,  # Keyboard 9 and (
    "0": 0x27,  # Keyboard 0 and )
    # Other keys
    "ENTER": 0x28,  # Keyboard Return (ENTER)
    "ESC": 0x29,  # Keyboard ESCAPE
    "BACKSPACE": 0x2A,  # Keyboard DELETE (Backspace)
    "TAB": 0x2B,  # Keyboard Tab
    "SPACE": 0x2C,  # Keyboard Spacebar
    "MINUS": 0x2D,  # Keyboard - and _
    "EQUAL": 0x2E,  # Keyboard = and +
    "LEFTBRACE": 0x2F,  # Keyboard [ and {
    "RIGHTBRACE": 0x30,  # Keyboard ] and }
    "BACKSLASH": 0x31,  # Keyboard \ and |
    "HASHTILDE": 0x32,  # Keyboard Non-US # and ~
    "SEMICOLON": 0x33,  # Keyboard ; and :
    "APOSTROPHE": 0x34,  # Keyboard ' and "
    "GRAVE": 0x35,  # Keyboard ` and ~
    "COMMA": 0x36,  # Keyboard , and <
    "DOT": 0x37,  # Keyboard . and >
    "SLASH": 0x38,  # Keyboard / and ?
    "CAPSLOCK": 0x39,  # Keyboard Caps Lock
    # F keys
    "F1": 0x3A,  # Keyboard F1
    "F2": 0x3B,  # Keyboard F2
    "F3": 0x3C,  # Keyboard F3
    "F4": 0x3D,  # Keyboard F4
    "F5": 0x3E,  # Keyboard F5
    "F6": 0x3F,  # Keyboard F6
    "F7": 0x40,  # Keyboard F7
    "F8": 0x41,  # Keyboard F8
    "F9": 0x42,  # Keyboard F9
    "F10": 0x43,  # Keyboard F10
    "F11": 0x44,  # Keyboard F11
    "F12": 0x45,  # Keyboard F12
    # Non print keys
    "SYSRQ": 0x46,  # Keyboard Print Screen
    "SCROLLLOCK": 0x47,  # Keyboard Scroll Lock
    "PAUSE": 0x48,  # Keyboard Pause
    "INSERT": 0x49,  # Keyboard Insert
    "HOME": 0x4A,  # Keyboard Home
    "PAGEUP": 0x4B,  # Keyboard Page Up
    "DELETE": 0x4C,  # Keyboard Delete Forward
    "END": 0x4D,  # Keyboard End
    "PAGEDOWN": 0x4E,  # Keyboard Page Down
    "RIGHT": 0x4F,  # Keyboard Right Arrow
    "LEFT": 0x50,  # Keyboard Left Arrow
    "DOWN": 0x51,  # Keyboard Down Arrow
    "UP": 0x52,  # Keyboard Up Arrow
    # Numpad
    "NUMLOCK": 0x53,  # Keyboard Num Lock and Clear
    "KPSLASH": 0x54,  # Keypad /
    "KPASTERISK": 0x55,  # Keypad *
    "KPMINUS": 0x56,  # Keypad -
    "KPPLUS": 0x57,  # Keypad +
    "KPENTER": 0x58,  # Keypad ENTER
    "KP1": 0x59,  # Keypad 1 and End
    "KP2": 0x5A,  # Keypad 2 and Down Arrow
    "KP3": 0x5B,  # Keypad 3 and PageDn
    "KP4": 0x5C,  # Keypad 4 and Left Arrow
    "KP5": 0x5D,  # Keypad 5
    "KP6": 0x5E,  # Keypad 6 and Right Arrow
    "KP7": 0x5F,  # Keypad 7 and Home
    "KP8": 0x60,  # Keypad 8 and Up Arrow
    "KP9": 0x61,  # Keypad 9 and Page Up
    "KP0": 0x62,  # Keypad 0 and Insert
    "KPDOT": 0x63,  # Keypad . and Delete
    # Other
    "102ND": 0x64,  # Keyboard Non-US \ and |
    "COMPOSE": 0x65,  # Keyboard Application
    "POWER": 0x66,  # Keyboard Power
    "KPEQUAL": 0x67,  # Keypad =
    # More F keys
    "F13": 0x68,  # Keyboard F13
    "F14": 0x69,  # Keyboard F14
    "F15": 0x6A,  # Keyboard F15
    "F16": 0x6B,  # Keyboard F16
    "F17": 0x6C,  # Keyboard F17
    "F18": 0x6D,  # Keyboard F18
    "F19": 0x6E,  # Keyboard F19
    "F20": 0x6F,  # Keyboard F20
    "F21": 0x70,  # Keyboard F21
    "F22": 0x71,  # Keyboard F22
    "F23": 0x72,  # Keyboard F23
    "F24": 0x73,  # Keyboard F24
    # Special commands
    "OPEN": 0x74,  # Keyboard Execute
    "HELP": 0x75,  # Keyboard Help
    "PROPS": 0x76,  # Keyboard Menu
    "FRONT": 0x77,  # Keyboard Select
    "STOP": 0x78,  # Keyboard Stop
    "AGAIN": 0x79,  # Keyboard Again
    "UNDO": 0x7A,  # Keyboard Undo
    "CUT": 0x7B,  # Keyboard Cut
    "COPY": 0x7C,  # Keyboard Copy
    "PASTE": 0x7D,  # Keyboard Paste
    "FIND": 0x7E,  # Keyboard Find
    "MUTE": 0x7F,  # Keyboard Mute
    "VOLUMEUP": 0x80,  # Keyboard Volume Up
    "VOLUMEDOWN": 0x81,  # Keyboard Volume Down
    # 0x82  Keyboard Locking Caps Lock
    # 0x83  Keyboard Locking Num Lock
    # 0x84  Keyboard Locking Scroll Lock
    "KPCOMMA": 0x85,  # Keypad Comma
    # 0x86  Keypad Equal Sign
    "RO": 0x87,  # Keyboard International1
    "KATAKANAHIRAGANA": 0x88,  # Keyboard International2
    "YEN": 0x89,  # Keyboard International3
    "HENKAN": 0x8A,  # Keyboard International4
    "MUHENKAN": 0x8B,  # Keyboard International5
    "KPJPCOMMA": 0x8C,  # Keyboard International6
    # 0x8d  Keyboard International7
    # 0x8e  Keyboard International8
    # 0x8f  Keyboard International9
    "HANGEUL": 0x90,  # Keyboard LANG1
    "HANJA": 0x91,  # Keyboard LANG2
    "KATAKANA": 0x92,  # Keyboard LANG3
    "HIRAGANA": 0x93,  # Keyboard LANG4
    "ZENKAKUHANKAKU": 0x94,  # Keyboard LANG5
    # 0x95  Keyboard LANG6
    # 0x96  Keyboard LANG7
    # 0x97  Keyboard LANG8
    # 0x98  Keyboard LANG9
    # 0x99  Keyboard Alternate Erase
    # 0x9a  Keyboard SysReq/Attention
    # 0x9b  Keyboard Cancel
    # 0x9c  Keyboard Clear
    # 0x9d  Keyboard Prior
    # 0x9e  Keyboard Return
    # 0x9f  Keyboard Separator
    # 0xa0  Keyboard Out
    # 0xa1  Keyboard Oper
    # 0xa2  Keyboard Clear/Again
    # 0xa3  Keyboard CrSel/Props
    # 0xa4  Keyboard ExSel
    # 0xb0  Keypad 00
    # 0xb1  Keypad 000
    # 0xb2  Thousands Separator
    # 0xb3  Decimal Separator
    # 0xb4  Currency Unit
    # 0xb5  Currency Sub-unit
    "KPLEFTPAREN": 0xB6,  # Keypad (
    "KPRIGHTPAREN": 0xB7,  # Keypad )
    # 0xb8  Keypad {
    # 0xb9  Keypad }
    # 0xba  Keypad Tab
    # 0xbb  Keypad Backspace
    # 0xbc  Keypad A
    # 0xbd  Keypad B
    # 0xbe  Keypad C
    # 0xbf  Keypad D
    # 0xc0  Keypad E
    # 0xc1  Keypad F
    # 0xc2  Keypad XOR
    # 0xc3  Keypad ^
    # 0xc4  Keypad %
    # 0xc5  Keypad <
    # 0xc6  Keypad >
    # 0xc7  Keypad &
    # 0xc8  Keypad &&
    # 0xc9  Keypad |
    # 0xca  Keypad ||
    # 0xcb  Keypad :
    # 0xcc  Keypad #
    # 0xcd  Keypad Space
    # 0xce  Keypad @
    # 0xcf  Keypad !
    # 0xd0  Keypad Memory Store
    # 0xd1  Keypad Memory Recall
    # 0xd2  Keypad Memory Clear
    # 0xd3  Keypad Memory Add
    # 0xd4  Keypad Memory Subtract
    # 0xd5  Keypad Memory Multiply
    # 0xd6  Keypad Memory Divide
    # 0xd7  Keypad +/-
    # 0xd8  Keypad Clear
    # 0xd9  Keypad Clear Entry
    # 0xda  Keypad Binary
    # 0xdb  Keypad Octal
    # 0xdc  Keypad Decimal
    # 0xdd  Keypad Hexadecimal
    # Modifier keys
    "LEFTCTRL": 0xE0,  # Keyboard Left Control
    "LEFTSHIFT": 0xE1,  # Keyboard Left Shift
    "LEFTALT": 0xE2,  # Keyboard Left Alt
    "LEFTMETA": 0xE3,  # Keyboard Left GUI
    "RIGHTCTRL": 0xE4,  # Keyboard Right Control
    "RIGHTSHIFT": 0xE5,  # Keyboard Right Shift
    "RIGHTALT": 0xE6,  # Keyboard Right Alt
    "RIGHTMETA": 0xE7,  # Keyboard Right GUI
    # Media keys
    "MEDIA_PLAYPAUSE": 0xE8,
    "MEDIA_STOPCD": 0xE9,
    "MEDIA_PREVIOUSSONG": 0xEA,
    "MEDIA_NEXTSONG": 0xEB,
    "MEDIA_EJECTCD": 0xEC,
    "MEDIA_VOLUMEUP": 0xED,
    "MEDIA_VOLUMEDOWN": 0xEE,
    "MEDIA_MUTE": 0xEF,
    "MEDIA_WWW": 0xF0,
    "MEDIA_BACK": 0xF1,
    "MEDIA_FORWARD": 0xF2,
    "MEDIA_STOP": 0xF3,
    "MEDIA_FIND": 0xF4,
    "MEDIA_SCROLLUP": 0xF5,
    "MEDIA_SCROLLDOWN": 0xF6,
    "MEDIA_EDIT": 0xF7,
    "MEDIA_SLEEP": 0xF8,
    "MEDIA_COFFEE": 0xF9,
    "MEDIA_REFRESH": 0xFA,
    "MEDIA_CALC": 0xFB,
}
