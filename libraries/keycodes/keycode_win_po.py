# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class Keycode:
    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0a
    H = 0x0b
    I = 0x0c
    J = 0x0d
    K = 0x0e
    L = 0x0f
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1a
    X = 0x1b
    Y = 0x1c
    Z = 0x1d
    ALT = 0xe2
    END = 0x4d
    F1 = 0x3a
    F2 = 0x3b
    F3 = 0x3c
    F4 = 0x3d
    F5 = 0x3e
    F6 = 0x3f
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45
    F13 = 0x68
    F14 = 0x69
    F15 = 0x6a
    F16 = 0x6b
    F17 = 0x6c
    F18 = 0x6d
    F19 = 0x6e
    F20 = 0x6f
    F21 = 0x70
    F22 = 0x71
    F23 = 0x72
    F24 = 0x73
    GUI = 0xe3
    ONE = 0x1e
    SIX = 0x23
    TAB = 0x2b
    TIL = 0x31
    TWO = 0x1f
    FIVE = 0x22
    FOUR = 0x21
    HOME = 0x4a
    NINE = 0x26
    ZERO = 0x27
    AGUDO = 0x30
    ALTGR = 0xe6
    COMMA = 0x36
    EIGHT = 0x25
    ENTER = 0x28
    GRAVE = 0x30
    MINUS = 0x38
    PAUSE = 0x48
    QUOTE = 0x34
    SEVEN = 0x24
    SHIFT = 0xe1
    SPACE = 0x2c
    THREE = 0x20
    TREMA = 0x2f
    APPLICATION = 0x65
    BACKSLASH = 0x35
    BACKSPACE = 0x2a
    CAPS_LOCK = 0x39
    CIRCUNFLEXO = 0x31
    COMMAND = 0xe3
    CONTROL = 0xe0
    DELETE = 0x4c
    DOWN_ARROW = 0x51
    EQUALS = 0x2f
    ESCAPE = 0x29
    FORWARD_SLASH = 0x31
    GRAVE_ACCENT = 0x33
    INSERT = 0x49
    KEYPAD_ASTERISK = 0x55
    KEYPAD_EIGHT = 0x60
    KEYPAD_FIVE = 0x5d
    KEYPAD_FORWARD_SLASH = 0x54
    KEYPAD_FOUR = 0x5c
    KEYPAD_MINUS = 0x56
    KEYPAD_NINE = 0x61
    KEYPAD_NUMLOCK = 0x53
    KEYPAD_ONE = 0x59
    KEYPAD_PERIOD = 0x63
    KEYPAD_PLUS = 0x57
    KEYPAD_SEVEN = 0x5f
    KEYPAD_SIX = 0x5e
    KEYPAD_THREE = 0x5b
    KEYPAD_TWO = 0x5a
    KEYPAD_ZERO = 0x62
    LEFT_ALT = 0xe2
    LEFT_ARROW = 0x50
    LEFT_BRACKET = 0x2d
    LEFT_CONTROL = 0xe0
    LEFT_GUI = 0xe3
    LEFT_SHIFT = 0xe1
    OEM_102 = 0x64
    OPTION = 0xe2
    PAGE_DOWN = 0x4e
    PAGE_UP = 0x4b
    PERIOD = 0x37
    PRINT_SCREEN = 0x46
    RETURN = 0x28
    RIGHT_ALT = 0xe6
    RIGHT_ARROW = 0x4f
    RIGHT_BRACKET = 0x2e
    RIGHT_CONTROL = 0xe4
    RIGHT_GUI = 0xe7
    RIGHT_SHIFT = 0xe5
    SCROLL_LOCK = 0x47
    SEMICOLON = 0x30
    SPACEBAR = 0x2c
    UP_ARROW = 0x52
    WINDOWS = 0xe3

    @classmethod
    def modifier_bit(cls, keycode):
        """Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0."""
        return (
            1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
        )
    