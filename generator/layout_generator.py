import html
import json
import natsort
import os
import pprint
import requests

import click
import xmltodict
from .keycode_name_to_virtualkey import name_to_virtualkey
from .keycode_us_ref import Keycode
from .virtualkey_table_us import VIRTUAL_KEY_US

# scancode / keycode
SPECIAL_KEYCODES = {
    # key, shift, option, shift-option
    0x56: 0x64,  # ["<",">","≤","≥"]
    0x29: 0x35,  # ["@","#","•","Ÿ"] ² on windows
}

SHIFT_FLAG = 0x80
ALTGR_FLAG = 0x80
NO_ALTGR_FLAG = 0x00

COMMON_HEADER_COPYRIGHT = """# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
\"\"\"
This file was automatically generated using Circuitpython_Keyboard_Layouts
\"\"\"


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


"""

DEBUG = True
BUILD_DIR = os.path.join("_build", "generated")
FILE_US = "keything-us.xml"

LIGHT = "\033[37m"
GREY = "\033[90m"
RED = "\033[1;91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1;49m"

YELLOW = "\033[1;93m"
WHITE = "\033[1;37m"
NOC = "\033[0m"

"""
International Keyboard:

Letter to virtual key name
- ascii letters are easy, and indexed
- non-ascii letters go in the HIGHER_ASCII list

Virtual Key Name to scancode(s)
- NEED_ALTGR has to be filled too, somehow

Scan Code to USB keycode (sc_to_kc)
- scancode to US Virtual Key Name (vk_to_sc)
- match US keycode names and Virtual Key Names (name_to_virtualkey)
- to USB keycode from US names (name_to_kc)
"""


def filter_codepoints(text):
    return text.replace("\r", "\n")


def jprint(data):
    print("<<< " + str(len(data)) + " >>>")
    print(json.dumps(data, indent=2))


virtualkey_to_keyname = {}
for name, vkey in name_to_virtualkey.items():
    if vkey not in virtualkey_to_keyname:
        virtualkey_to_keyname[vkey] = []
    virtualkey_to_keyname[vkey].append(name)


def list_keycode_name(key, value):
    output = []
    if key in virtualkey_to_keyname:
        for name in virtualkey_to_keyname[key]:
            output.append( (name, value) )
    else:
        output = [(key, value)]
    return output


def get_name_to_keycode():
    name_to_kc = {}
    kcnums = [
        (name, getattr(Keycode, name)) for name in dir(Keycode) if name.upper() == name
    ]
    kcnums.sort(key=lambda x: x[1])
    for name, kc in kcnums:
        if name in name_to_virtualkey:
            name = name_to_virtualkey[name]
        name_to_kc[name] = kc

    if DEBUG:
        print("<<< name_to_kc : " + str(len(name_to_kc)) + " >>>")
    # jprint(name_to_kc)

    return name_to_kc


def modif(res):
    if "@With" in res:
        if res["@With"] == "VK_NUMLOCK":
            return "numpad"
        if res["@With"] == "VK_SHIFT":
            return "shift"
        if res["@With"] == "VK_CONTROL VK_MENU":
            return "altgr"
        if res["@With"] == "VK_MENU":
            return "alt"
        return ""
    else:
        return "letter"


def get_vk_to_sc(data):
    keything = xmltodict.parse(data)
    physical_keys = keything["KeyboardLayout"]["PhysicalKeys"]["PK"]
    # jprint(physical_keys)

    vk_to_sc = {}
    for key in physical_keys:
        name = key["@VK"].replace("VK_", "")
        sckey = int(key["@SC"], 16)
        vk_to_sc[name] = {
            "scancode": sckey,
        }
        #
        if "Result" in key:
            kresult = key["Result"]
            if isinstance(kresult, dict):
                kresult = [kresult]
            if isinstance(kresult, list):
                for res in kresult:
                    if "@VK" in res:
                        kname = res["@VK"].replace("VK_", "")
                        vk_to_sc[kname] = {
                            "scancode": sckey,
                        }
                        text = html.unescape(res["@Text"])
                        vk_to_sc[kname][modif(res)] = text
                    elif "@Text" not in res:
                        if "@TextCodepoints" in res:
                            text = chr(int(res["@TextCodepoints"], 16))
                            text = filter_codepoints(text)
                        else:
                            if "DeadKeyTable" in res:
                                if modif(res) == "": continue
                                firstkey = res["DeadKeyTable"]["@Accent"]
                                if "@Name" in res["DeadKeyTable"]:
                                    deadname = res["DeadKeyTable"]["@Name"].replace(" ","_")
                                else:
                                    deadname = "_accent" + "".join(["_" + str(ord(x)) for x in firstkey])
                                # dead key base: in keycode, not in layout
                                if deadname not in vk_to_sc:
                                    vk_to_sc[deadname] = {
                                        "scancode": sckey,
                                        "dead": True,
                                    }
                                else:
                                    if DEBUG:
                                        print("Dead Key", deadname, "already here")
                                vk_to_sc[deadname][modif(res)] = firstkey
                                for deadres in res["DeadKeyTable"]["Result"]:
                                    secondkey = deadres["@With"]
                                    deadtext = deadres["@Text"]
                                    dk_name = f"_{deadname}_{secondkey}"
                                    if dk_name not in vk_to_sc:
                                        vk_to_sc[dk_name] = {
                                            "scancode": sckey,
                                            "firstkey": firstkey,
                                        }
                                    vk_to_sc[dk_name]["secondkey"] = secondkey
                                    vk_to_sc[dk_name][modif(res)] = deadtext
                                    if DEBUG:
                                        pprint.pprint(vk_to_sc[dk_name])
                                if DEBUG:
                                    print(
                                        "DEAD",
                                        vk_to_sc[name],
                                    )
                            continue
                    else:
                        text = html.unescape(res["@Text"])
                    vk_to_sc[name][modif(res)] = text
            else:
                if DEBUG:
                    print("What is Result ?", kresult)

    if DEBUG:
        print("<<< vk_to_sc : " + str(len(vk_to_sc)) + " >>>")
    # jprint(vk_to_sc)

    return vk_to_sc


def get_scancode_to_keycode():
    name_to_kc = get_name_to_keycode()
    name_to_kc_left = set(name_to_kc)
    vk_to_sc = get_vk_to_sc(VIRTUAL_KEY_US)
    vk_to_sc_left = set(vk_to_sc)

    sc_to_kc = {}
    for key in name_to_kc:
        if key in vk_to_sc:
            vk_to_sc_left.remove(key)
            name_to_kc_left.remove(key)
            sc_to_kc[vk_to_sc[key]["scancode"]] = name_to_kc[key]

    return sc_to_kc


# TODO: add non-US scancodes/keycodes in `sc_to_kc`


"""
The actual conversion from scan codes to key codes
Missing unidentified names
NUMPAD is particularly missing (it's refed as arrows, page up, etc.)
"""
# jprint(sc_to_kc)
# print("name_to_kc_left", len(name_to_kc_left), sorted(name_to_kc_left))
# print("vk_to_sc_left", len(vk_to_sc_left), sorted(vk_to_sc_left))
# kc_to_sc = dict([(y,x) for (x,y) in sc_to_kc.items()])

########################################################################


class LayoutData:
    def __init__(self, asciis, charas, altgr, high, keycodes, combined):
        self.asciis = asciis
        self.charas = charas
        self.altgr = altgr
        self.high = high
        self.keycodes = keycodes
        self.combined = combined
    def __repr__(self):
        return repr({
            "asciis": self.asciis,
            "charas": self.charas,
            "altgr": self.altgr,
            "high": self.high,
            "keycodes": self.keycodes,
            "combined": self.combined,
        })


def get_layout_data(virtual_key_defs_lang):
    asciis = [0] * 128
    charas = [""] * 128
    NEED_ALTGR = []
    HIGHER_ASCII = {}
    COMBINED_KEYS = {}

    scancode_to_keycode = get_scancode_to_keycode()

    KEYCODES = {}

    # loop the list of virtual keycodes that exist in the language
    for num, virtualkey in enumerate(virtual_key_defs_lang):
        # the info on the key
        key_info = virtual_key_defs_lang[virtualkey]
        # scancode of the key
        scancode = key_info["scancode"]

        # matching keycodes
        keycode = None
        if scancode in scancode_to_keycode:
            keycode = scancode_to_keycode[scancode]
        if scancode in SPECIAL_KEYCODES:
            if keycode is None:
                keycode = SPECIAL_KEYCODES[scancode]
                if DEBUG:
                    print(
                        CYAN + f"SPECIAL scancode:{scancode} > keycode:{keycode}" + NOC
                    )
            else:
                if keycode != SPECIAL_KEYCODES[scancode]:
                    if DEBUG:
                        print(RED + "Different:", keycode, SPECIAL_KEYCODES[scancode])
        if keycode is None:
            # TODO: check there's none missing
            if DEBUG:
                print(BLUE + "Unknown scancode", virtualkey, scancode)
                print("    ", key_info, NOC)
            continue

        KEYCODES.update(list_keycode_name(virtualkey, keycode))
        # KEYCODES[virtualkey] = keycode

        # find the letter somehow
        # letter as defined in the keyboard definition
        if "letter" in key_info:
            letter = key_info["letter"]
            dead = "dead" in key_info
            pos = ord(letter)
            if DEBUG:
                print("L", num, pos, letter, scancode, hex(keycode))
            if "secondkey" in key_info:
                firstkey = keycode
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, NO_ALTGR_FLAG)
            elif pos < 128:
                if not charas[pos]:
                    if not dead:
                        asciis[pos] = keycode
                        charas[pos] = letter
                    KEYCODES.update(list_keycode_name(virtualkey, keycode))
                    # KEYCODES[virtualkey] = keycode
            else:
                if letter not in HIGHER_ASCII:
                    if not dead:
                        HIGHER_ASCII[letter] = keycode
                    KEYCODES.update(list_keycode_name(virtualkey, keycode))
                    # KEYCODES[virtualkey] = keycode
                else:
                    if DEBUG:
                        print(RED + "double", letter, HIGHER_ASCII[letter], NOC)

        if "shift" in key_info and "dead" not in key_info:
            letter = key_info["shift"]
            pos = ord(letter)
            if DEBUG:
                print("S", num, pos, letter, scancode, hex(keycode | SHIFT_FLAG))
            if "secondkey" in key_info:
                firstkey = keycode | SHIFT_FLAG
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, NO_ALTGR_FLAG)
            elif pos < 128:
                if not charas[pos]:
                    asciis[pos] = keycode | SHIFT_FLAG
                    charas[pos] = letter
                    if DEBUG:
                        print("------ SHIFT ", charas[pos])
            else:
                if letter not in HIGHER_ASCII:
                    HIGHER_ASCII[letter] = keycode | SHIFT_FLAG
                else:
                    if DEBUG:
                        print(RED + "double", letter, HIGHER_ASCII[letter], NOC)

        def add_alt_gr(letter):
            if letter in NEED_ALTGR:
                if DEBUG:
                    print(RED + "Already in NEED_ALTGR", letter, NOC)
            else:
                NEED_ALTGR.append(letter)

        if "altgr" in key_info and "dead" not in key_info:
            letter = key_info["altgr"]
            dead = "dead" in key_info
            pos = ord(letter)
            if DEBUG:
                print("A", num, pos, letter, scancode, hex(keycode))
            if "secondkey" in key_info:
                # NOTE: don't add to the altgr list
                firstkey = keycode
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, ALTGR_FLAG)
            elif pos < 128:
                if not charas[pos]:
                    add_alt_gr(letter)
                    asciis[pos] = keycode
                    charas[pos] = letter
            else:
                if letter not in HIGHER_ASCII:
                    add_alt_gr(letter)
                    HIGHER_ASCII[letter] = keycode
                else:
                    if DEBUG:
                        print(RED + "double", letter, HIGHER_ASCII[letter], NOC)

        if "numpad" in key_info:
            letter = key_info["numpad"]
            if DEBUG:
                print("NUM", key_info)

    if DEBUG:
        print(json.dumps(KEYCODES, indent=2))
        print(f"--- {len(KEYCODES)} ---")

    return LayoutData(
        asciis,
        charas,
        NEED_ALTGR,
        HIGHER_ASCII,
        KEYCODES,
        COMBINED_KEYS,
    )


def make_layout_file(layout_data):
    output_file_data = (
        COMMON_HEADER_COPYRIGHT
        + "from keyboard_layout import KeyboardLayoutBase\n"
        + f"class KeyboardLayout(KeyboardLayoutBase):\n"
        "    ASCII_TO_KEYCODE = (\n"
    )
    for x in range(128):
        keycode = layout_data.asciis[x]
        chara = layout_data.charas[x]
        output_file_data += f"        b'\\x{keycode:02x}'  # {repr(chara)}\n"
    output_file_data += (
        "    )\n"
        "    NEED_ALTGR = " + repr("".join(sorted(layout_data.altgr))) + "\n"
        "    HIGHER_ASCII = {\n"
    )
    for k, c in layout_data.high.items():
        output_file_data += f"        {repr(k)}: 0x{c:02x},\n"
    output_file_data += (
        "    }\n"
        "    COMBINED_KEYS = {\n"
    )
    for k, c in layout_data.combined.items():
        first, second, altgr = c
        second = ord(second) | altgr
        output_file_data += (
            f"        {repr(k)}: "
            f"b\"\\x{first:02x}\\x{second:02x}\","
            "\n"
        )
    output_file_data += (
        "    }\n"
    )
    return output_file_data

def output_layout_file(output_file, output_file_data):
    with open(output_file, "w") as fp:
        fp.write(output_file_data)


def make_keycode_file(layout_data):
    output_file_data = (
        COMMON_HEADER_COPYRIGHT + "class Keycode:\n"
    )
    def ck(x):
        l = x[0]
        if len(l) == 2:
            l = l + " "
        if len(l) > 5:
            l = l.ljust(20)
        return (len(l), l)
    for name,code in natsort.natsorted(layout_data.keycodes.items(), key=ck):
        # code = layout_data.keycodes[name]
        if name[0] != "_":
            output_file_data += f"    {name} = 0x{code:02x}\n"
    output_file_data += """
    @classmethod
    def modifier_bit(cls, keycode):
        \"""Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0.\"""
        return (
            1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
        )
    """
    return output_file_data

def output_keycode_file(output_file, output_file_data):
    with open(output_file, "w") as fp:
        fp.write(output_file_data)


@click.group(invoke_without_command=True)
@click.option("--keyboard", "-k", required=True)
@click.option("--lang", "-l", default="")
@click.option("--platform", "-p", default="win")
@click.option("--output", "-o", is_flag=True)
@click.option("--output-layout", default="")
@click.option("--output-keycode", default="")
@click.option("--debug/--no-debug", "-d", is_flag=True)
@click.option("--verbose", "-v", default="")
def main(keyboard, lang, platform, output, output_layout, output_keycode, debug, verbose):
    global DEBUG
    DEBUG = debug
    if DEBUG:
        print(">", keyboard)
        print(">", platform)
        print(">", lang)
    if os.path.isfile(keyboard):
        if not lang:
            lang = keyboard.split(".")[0].split("_")[-1].split("-")[-1]
        with open(keyboard, "r") as fp:
            data = fp.read()
    else:
        if not keyboard.startswith("https://kbdlayout.info/"):
            if not lang:
                lang = keyboard.replace("/", "")
            url = "https://kbdlayout.info/kbd" + keyboard
        else:
            if not lang:
                lang = keyboard[26:]
        url = keyboard + "/download/xml"
        res = requests.get(url)
        data = res.content.decode("utf8")

    if not platform:
        platform = "Win"
    if not lang:
        lang = "xx"

    virtual_key_defs_lang = get_vk_to_sc(data)
    layout_data = get_layout_data(virtual_key_defs_lang)

    data_layout = make_layout_file(layout_data)
    if output or output_layout:
        os.makedirs(BUILD_DIR, exist_ok=True)
        if not output_layout:
            output_layout = os.path.join(
                BUILD_DIR, f"keyboard_layout_{platform.lower()}_{lang.lower()}.py"
            )
        print(CYAN + f"Write to {output_layout}" + NOC)
        output_layout_file(output_layout, data_layout)
    if verbose == "layout" or verbose == "v":
        print(data_layout)

    data_keycode = make_keycode_file(layout_data)
    if output or output_keycode:
        os.makedirs(BUILD_DIR, exist_ok=True)
        if not output_keycode:
            output_keycode = os.path.join(
                BUILD_DIR, f"keycode_{platform.lower()}_{lang.lower()}.py"
            )
        print(CYAN + f"Write to {output_keycode}" + NOC)
        output_keycode_file(output_keycode, data_keycode)
    if verbose == "keycode" or verbose == "v":
        print(data_keycode)

if __name__ == "__main__":
    main()
