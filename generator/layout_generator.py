"""
Make International Keyboard:

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
import html
import json
import natsort
import os
import requests

import click
import xmltodict
from .keycode_name_to_virtualkey import name_to_virtualkey
from .keycode_us_ref import Keycode
from .virtualkey_table_us import VIRTUAL_KEY_US

""" debug level dev: only show dev prints (use for print debugging) """
DEBUG_DEV = -1
""" debug level error: only show errors """
DEBUG_ERROR = 1
""" debug level info: show everything """
DEBUG_INFO = 2
""" debug level silent: show nothing """
DEBUG_SILENT = 0
""" default debug level: show errors """
DEBUG_LEVEL = DEBUG_ERROR
""" default target directory for --output """
BUILD_DIR = os.path.join("_build", "generated")

""" scancodes / keycodes that are not in keycode_us_ref """
SPECIAL_KEYCODES = {
    # key, shift, option, shift-option
    0x56: 0x64,  # ["<",">","≤","≥"]
    0x29: 0x35,  # ["@","#","•","Ÿ"] ² on windows
}
""" character names to display in the layout comments """
CHARACTER_NAMES = {
    8: "BACKSPACE",
    # 13: repr("\r"),
    0x1B: "ESC",
}
""" flag in the keycode that says if SHIFT is required for a letter """
SHIFT_FLAG = 0x80
""" flag in the combined keys codes for ALTGR with the first key """
ALTGR_FLAG = 0x80
""" no altgr flag for the first combined key """
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


def _echo(*text, nl=True, **kwargs):
    """printout things using click joining all varargs"""
    text = [
        (item if isinstance(item, str) else repr(item))
        for item in text
    ]
    click.secho(" ".join(text), nl=nl, **kwargs)


def echo(*text, nl=True, **kwargs):
    """print as info"""
    if DEBUG_LEVEL >= DEBUG_INFO:
        _echo(*text, nl=nl, **kwargs)


def echoE(*text, nl=True, **kwargs):
    """print as error, in red by default"""
    if "fg" not in kwargs:
        kwargs["fg"] = "red"
    if DEBUG_LEVEL >= DEBUG_ERROR:
        _echo(*text, nl=nl, **kwargs)


def echoD(*text, nl=True, **kwargs):
    """print only in dev mode, use for print debugging"""
    if DEBUG_LEVEL == DEBUG_DEV:
        _echo(*text, nl=nl, **kwargs)


def jprint(data, nl=True, **kwargs):
    """dump a structure as json"""
    echo("<<< " + str(len(data)) + " >>>", nl, **kwargs)
    echo(json.dumps(data, indent=2), nl, **kwargs)


def get_v_to_k():
    """create the reverse virtualkey/keyname table"""
    virtualkey_to_keyname = {}
    for name, vkey in name_to_virtualkey.items():
        if vkey not in virtualkey_to_keyname:
            virtualkey_to_keyname[vkey] = []
        virtualkey_to_keyname[vkey].append(name)
    return virtualkey_to_keyname


virtualkey_to_keyname = get_v_to_k()


def filter_codepoints(text):
    """filter converted codepoints from XML"""
    return text.replace("\r", "\n")


def list_keycode_name(key, value):
    """list the keycode names associated with a virtual key name"""
    output = []
    if key in virtualkey_to_keyname:
        for name in virtualkey_to_keyname[key]:
            output.append((name, value))
    else:
        output = [(key, value)]
    return output


def get_name_to_keycode():
    """
    create the table mapping virtual key names to keycodes
    from the adafruit_hid Keycode file
    """
    name_to_kc = {}
    kcnums = [
        (name, getattr(Keycode, name))
        for name in dir(Keycode)
        if name.upper() == name
    ]
    kcnums.sort(key=lambda x: x[1])
    for name, kc in kcnums:
        if name in name_to_virtualkey:
            name = name_to_virtualkey[name]
        name_to_kc[name] = kc

    echo("<<< name_to_kc : " + str(len(name_to_kc)) + " >>>")
    # jprint(name_to_kc)

    return name_to_kc


def modif(res):
    """
    From a "Result" entry, get the modifier id string
    """
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
    """
    Analyse the XML file to make the table of all keys.
    Each entry:
    - is indexed by a virtual key name or made-up name
    - is associated with a scancode
    - has a letter associated with different modifiers (or lack thereof)
    - dead keys and combined keys have additional information
    - dead = True means it's the dead key (don't press it alone)
    - firstkey/secondkey are the respective keys for dead key combinations
    """
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
        # get the "results" from the entry
        if "Result" in key:
            kresult = key["Result"]
            if isinstance(kresult, dict):
                kresult = [kresult]
            if not isinstance(kresult, list):
                echo("What is Result ?", kresult)
                continue
        else:
            continue
        #
        for res in kresult:
            if "@VK" in res:
                # if the result has its own virtualkey name, use that
                kname = res["@VK"].replace("VK_", "")
                vk_to_sc[kname] = {
                    "scancode": sckey,
                }
                text = html.unescape(res["@Text"])
                vk_to_sc[kname][modif(res)] = text
            elif "@Text" in res:
                # if it has a text, it's simple
                text = html.unescape(res["@Text"])
                vk_to_sc[name][modif(res)] = text
            elif "@TextCodepoints" in res:
                # if it has a codepoint, convert it
                text = chr(int(res["@TextCodepoints"], 16))
                text = filter_codepoints(text)
                vk_to_sc[name][modif(res)] = text
            elif "DeadKeyTable" in res:
                # if it is a dead key with a deadkey table, go through it
                if modif(res) == "":
                    # unwanted modifier (ctrl or other)
                    continue
                # the first key in the sequence (the "dead key" or accent)
                firstkey = res["DeadKeyTable"]["@Accent"]
                # the name of the dead key for the Keycode table
                if "@Name" in res["DeadKeyTable"]:
                    deadname = res["DeadKeyTable"]["@Name"].replace(" ", "_")
                else:
                    # if none, generate one with "_" to exclude it from Keycode
                    deadname = "_accent" + "".join(
                        ["_" + str(ord(x)) for x in firstkey]
                    )
                # dead key base: in keycode, not in layout
                if deadname not in vk_to_sc:
                    vk_to_sc[deadname] = {
                        "scancode": sckey,
                        "dead": True,
                    }
                else:
                    echoE("Dead Key", deadname, "already here")
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

    echo("<<< vk_to_sc : " + str(len(vk_to_sc)) + " >>>")
    # jprint(vk_to_sc)

    return vk_to_sc


def get_scancode_to_keycode():
    """create the table associating scancodes and keycodes from the US XML file"""
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


# TODO: are there missing non-US scancodes/keycodes in `sc_to_kc` ?


########################################################################


class LayoutData:
    """
    Asimple struct class to carry around the layout information.
    - asciis has the keycode information for each low ascii character (with shift bit)
    - charas has said characters, for display in the comment string and testing existence
    - atgr is the list of letters that need alt-gr pressed
    - high is the list of high-ascii/unicode letters and their keycode
    - keycodes is the table associating key names with keycodes (for the Keycode class)
    - combined is the table of combined keys
    A combined key has two bytes:
    - the keycode to the first key, with the high bit as the shift bit
    - the letter for the second key (assumed to be low ascii)
    - the second key's high bit is the altgr bit for the first key
    """
    def __init__(self, asciis, charas, altgr, high, keycodes, combined):
        self.asciis = asciis
        self.charas = charas
        self.altgr = altgr
        self.high = high
        self.keycodes = keycodes
        self.combined = combined

    def __repr__(self):
        return repr(
            {
                "asciis": self.asciis,
                "charas": self.charas,
                "altgr": self.altgr,
                "high": self.high,
                "keycodes": self.keycodes,
                "combined": self.combined,
            }
        )


def get_layout_data(virtual_key_defs_lang):
    """Create the layout data from a language file."""
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
                echo(f"SPECIAL scancode:{scancode} > keycode:{keycode}", fg="cyan")
            else:
                if keycode != SPECIAL_KEYCODES[scancode]:
                    echoE("Different:", keycode, SPECIAL_KEYCODES[scancode])
        if keycode is None:
            # TODO: check there's none missing
            echo("Unknown scancode", virtualkey, scancode, fg="blue")
            echo("    ", key_info, fg="blue")
            continue

        KEYCODES.update(list_keycode_name(virtualkey, keycode))
        # KEYCODES[virtualkey] = keycode

        # find the letter somehow
        # letter as defined in the keyboard definition
        if "letter" in key_info:
            letter = key_info["letter"]
            dead = "dead" in key_info
            pos = ord(letter)
            echo("L", num, pos, letter, scancode, hex(keycode))
            if "secondkey" in key_info:
                firstkey = keycode
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, NO_ALTGR_FLAG)
            elif pos < 128:
                if not charas[pos]:
                    if not dead:
                        asciis[pos] = keycode
                        charas[pos] = letter
                    else:
                        echoD("dead", key_info)
                    KEYCODES.update(list_keycode_name(virtualkey, keycode))
                    # KEYCODES[virtualkey] = keycode
            else:
                if letter not in HIGHER_ASCII:
                    if not dead:
                        HIGHER_ASCII[letter] = keycode
                    else:
                        echoD("dead", key_info)
                    KEYCODES.update(list_keycode_name(virtualkey, keycode))
                    # KEYCODES[virtualkey] = keycode
                else:
                    echoE("double", letter, HIGHER_ASCII[letter])

        if "shift" in key_info and "dead" not in key_info:
            letter = key_info["shift"]
            pos = ord(letter)
            echo("S", num, pos, letter, scancode, hex(keycode | SHIFT_FLAG))
            if "secondkey" in key_info:
                firstkey = keycode | SHIFT_FLAG
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, NO_ALTGR_FLAG)
            elif pos < 128:
                if not charas[pos]:
                    asciis[pos] = keycode | SHIFT_FLAG
                    charas[pos] = letter
                    echo("------ SHIFT ", charas[pos])
            else:
                if letter not in HIGHER_ASCII:
                    HIGHER_ASCII[letter] = keycode | SHIFT_FLAG
                else:
                    echoE("double", letter, HIGHER_ASCII[letter])

        def add_alt_gr(letter):
            if letter in NEED_ALTGR:
                echoE("Already in NEED_ALTGR", letter)
            else:
                NEED_ALTGR.append(letter)

        if "altgr" in key_info and "dead" not in key_info:
            letter = key_info["altgr"]
            dead = "dead" in key_info
            pos = ord(letter)
            echo("A", num, pos, letter, scancode, hex(keycode))
            if "secondkey" in key_info:
                # NOTE: don't add to the altgr list
                firstkey = keycode
                secondkey = key_info["secondkey"]
                COMBINED_KEYS[letter] = (firstkey, secondkey, ALTGR_FLAG)
                # not the character still
                if pos < 128:
                    asciis[pos] = -1
                    charas[pos] = letter
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
                    echoE("double", letter, HIGHER_ASCII[letter])

        if "numpad" in key_info:
            letter = key_info["numpad"]
            echo("NUM", key_info)

    echo(json.dumps(KEYCODES, indent=2))
    echo(f"--- {len(KEYCODES)} ---")

    return LayoutData(
        asciis,
        charas,
        NEED_ALTGR,
        HIGHER_ASCII,
        KEYCODES,
        COMBINED_KEYS,
    )


def make_layout_file(layout_data):
    """make the layout file contents"""
    output_file_data = (
        COMMON_HEADER_COPYRIGHT
        + "from keyboard_layout import KeyboardLayoutBase\n"
        + f"class KeyboardLayout(KeyboardLayoutBase):\n"
        "    ASCII_TO_KEYCODE = (\n"
    )
    for x in range(128):
        keycode = layout_data.asciis[x]
        chara = layout_data.charas[x]
        output_file_data += "        b'\\x{:02x}'".format(max(0, keycode))
        charepr = ""
        if chara:
            charepr = repr(chara)
            if chara in CHARACTER_NAMES:
                charepr = CHARACTER_NAMES[chara]
        if x in CHARACTER_NAMES:
            charepr = CHARACTER_NAMES[x]
        if charepr:
            output_file_data += "  # " + charepr
            if keycode == 0:
                output_file_data += " (Ignored)"
            if keycode == -1:
                output_file_data += " (Dead key)"
        output_file_data += "\n"
    output_file_data += (
        "    )\n"
        "    NEED_ALTGR = " + repr("".join(sorted(layout_data.altgr))) + "\n"
        "    HIGHER_ASCII = {\n"
    )
    for k, c in layout_data.high.items():
        output_file_data += f"        {repr(k)}: 0x{c:02x},\n"
    output_file_data += "    }\n" "    COMBINED_KEYS = {\n"
    for k, c in layout_data.combined.items():
        first, second, altgr = c
        second = ord(second) | altgr
        output_file_data += (
            f"        {repr(k)}: "
            f'b"\\x{first:02x}\\x{second:02x}",'
            "\n"
        )
    output_file_data += "    }\n"
    return output_file_data


def output_layout_file(output_file, output_file_data):
    """write out the layout file"""
    with open(output_file, "w") as fp:
        fp.write(output_file_data)


def make_keycode_file(layout_data):
    """make the keycode file contents"""
    output_file_data = COMMON_HEADER_COPYRIGHT + "class Keycode:\n"

    def ck(x):
        l = x[0]
        if len(l) == 2:
            l = l + " "
        if len(l) > 5:
            l = l.ljust(20)
        return (len(l), l)

    for name, code in natsort.natsorted(layout_data.keycodes.items(), key=ck):
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
    """write out the keycode file"""
    with open(output_file, "w") as fp:
        fp.write(output_file_data)


@click.group(invoke_without_command=True)
@click.option(
    "--keyboard", "-k", required=True,
    help="The XML layout file, or URL to the layout on kbdlayout.info."
)
@click.option(
    "--lang", "-l", default="",
    help="The language string to use in the output file name, defaults to the last part of the file name or the language part of the URL."
)
@click.option(
    "--platform", "-p", default="win",
    help="The platform string to use in the output file name. Only windows currently."
)
@click.option(
    "--output", "-o", is_flag=True,
    help="Activate writing out the layout and keycode files."
)
@click.option(
    "--output-layout", default="",
    help="Override the layout output file path and name."
)
@click.option(
    "--output-keycode", default="",
    help="Override the keycode output file path and name."
)
@click.option(
    "--debug", "-d", default=1,
    help="Set the debug level, -1 (dev only), 0 (silent), 1 (errors), 2 (all), default is 1"
)
@click.option("--show", "-s", default="")
def main(keyboard, lang, platform, output, output_layout, output_keycode, debug, show):
    """Make keyboard layout files from layout XML data."""
    global DEBUG_LEVEL
    DEBUG_LEVEL = debug
    echo(">", keyboard, fg="green")
    echo(">", platform, fg="green")
    echo(">", lang, fg="green")
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
        if not show:
            echoE(f"Write to {output_layout}", fg="cyan")
        else:
            echo(f"Write to {output_layout}", fg="cyan")
        output_layout_file(output_layout, data_layout)
    if show == "layout" or show == "s":
        print(data_layout)

    data_keycode = make_keycode_file(layout_data)
    if output or output_keycode:
        os.makedirs(BUILD_DIR, exist_ok=True)
        if not output_keycode:
            output_keycode = os.path.join(
                BUILD_DIR, f"keycode_{platform.lower()}_{lang.lower()}.py"
            )
        if not show:
            echoE(f"Write to {output_keycode}", fg="cyan")
        else:
            echo(f"Write to {output_keycode}", fg="cyan")
        output_keycode_file(output_keycode, data_keycode)
    if show == "keycode" or show == "s":
        print(data_keycode)


if __name__ == "__main__":
    main()
