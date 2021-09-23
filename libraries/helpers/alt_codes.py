# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
Courtesy of https://github.com/nico7885
"""

from adafruit_hid.keycode import Keycode

class Altcode(Keycode):
    unicodeChar = "€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ"
    asciiexValue = (128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 142, 145, 146, 147, 148, 149, 150,
                    151, 152, 153, 154, 155, 156, 158, 159)

    def __init__(self, keyboard, layout):
        self.keyboard = keyboard
        self.layout = layout

    def _special_char(self, char_value):
        if char_value == 0x0A or char_value == 0x0D:
            self.keyboard.send(Keycode.ENTER)
        elif char_value == 0x09:
            self.keyboard.send(Keycode.TAB)  
        else:
            raise ValueError("Value of char is unknown:", char_value)
            
        
    def _get_value_of_char(self, char):
        # Si le caractère fait partie de la table ASCII étendue
        # renvoie la valeur ASCII étendue du caractère
        # sinon renvoie la valeur Unicode
        indice = self.unicodeChar.find(char)
        if indice != -1:
            char_val = self.asciiexValue[indice]
        else:
            char_val = ord(char)
        return char_val


    def _num_to_keypad(self, string):
        for char in string:
            if char.isdigit():
                num = int(char)
                if num > 0:
                # Ne pas utiliser la fonction send qui effectue un releaseAll
                    self.keyboard.press(self.KEYPAD_ONE + num - 1)
                    self.keyboard.release(self.KEYPAD_ONE + num - 1)
                elif num == 0:
                    self.keyboard.press(self.KEYPAD_ZERO)
                    self.keyboard.release(self.KEYPAD_ZERO)
            else:
                raise ValueError("Char is not a digit:", char)
                break


    def _win_alt_code_CP1252(self, asciiex_string):
        len_asciiex = len(asciiex_string)
        self.keyboard.press(self.ALT)
        for x in range(4-len_asciiex):
            # Ne pas utiliser la fonction send qui effectue un releaseAll
            self.keyboard.press(self.KEYPAD_ZERO)
            self.keyboard.release(self.KEYPAD_ZERO)
        self._num_to_keypad(asciiex_string)
        self.keyboard.release_all()


    def _win_alt_unicode_point(self, unicode_string):
        self.keyboard.press(self.ALT)
        self._num_to_keypad(unicode_string)
        self.keyboard.release_all()


    def windows(self, string):
        for char in string:
            char_val = self._get_value_of_char(char)
            if char_val < 32:
                # pour les valeurs TAB et \n
                self._special_char(char_val)
            elif char_val < 256:
                self._win_alt_code_CP1252(str(char_val))
            else:
                self._win_alt_unicode_point(str(char_val))


    def _linux_alt_unicode_point(self, unicode_stringHex):
        self.keyboard.send(self.CONTROL, self.SHIFT, self.U)
        for char in unicode_stringHex[2:]:
            # on n'envoie pas le shift ou le altgr ici!
            # seul la position de la touche est nécessaire!
            self.keyboard.send(self.layout.keycodes(char)[-1])
        self.keyboard.send(self.ENTER)


    def linux(self, string):
        for char in string:
            char_val = ord(char)
            if char_val < 32:
                # pour les valeurs TAB et \n
                self._special_char(char_val)
            else:
                self._linux_alt_unicode_point(hex(char_val))
