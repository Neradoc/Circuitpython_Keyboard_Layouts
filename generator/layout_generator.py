import html
import json
import os
import pprint

import click
import xmltodict
from .keycode_names import keycode_names
from .keycode_name_to_virtualkey import name_to_virtualkey
from .keycode_us_ref import Keycode
from .usbif_keycode_scancode import usbif_keycode_scancode
from .virtualkey_table_us import VIRTUAL_KEY_US

# scancode / keycode
SPECIAL_KEYCODES = {
	# key, shift, option, shift-option
	0x56: 0x64,  # ["<",">","≤","≥"]
	0x29: 0x35,  # ["@","#","•","Ÿ"] ² on windows
}

def filter_codepoints(text):
	return text.replace("\r","\n")

DEBUG = True
BUILD_DIR = os.path.join("_build", "generated")
FILE_US = "keything-us.xml"

LIGHT  = "\033[37m"
GREY   = "\033[90m"
RED    = "\033[1;91m"
GREEN  = "\033[92m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
CYAN   = "\033[96m"
BOLD   = "\033[1;49m"

YELLOW = "\033[1;93m"
WHITE  = "\033[1;37m"
NOC    = "\033[0m"

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

def jprint(data):
	if DEBUG: print("<<< " + str(len(data)) + " >>>")
	if DEBUG: print(json.dumps(data, indent=2))

def get_name_to_keycode():
	name_to_kc = {}
	kcnums = [
		(name, getattr(Keycode, name))
		for name in dir(Keycode)
		if name.upper() == name
	]
	kcnums.sort(key = lambda x: x[1])
	for name, kc in kcnums:
		if name in name_to_virtualkey:
			name = name_to_virtualkey[name]
		name_to_kc[name] = kc

	if DEBUG: print("<<< name_to_kc : " + str(len(name_to_kc)) + " >>>")
	# jprint(name_to_kc)
	
	return name_to_kc


def get_vk_to_sc(data):
	keything = xmltodict.parse(data)
	physical_keys = keything['KeyboardLayout']['PhysicalKeys']['PK']
	# jprint(physical_keys)

	vk_to_sc = {}
	for key in physical_keys:
		name = key['@VK'].replace("VK_", "")
		sckey = int(key['@SC'], 16)
		vk_to_sc[name] = {
			"scancode": sckey,
		}
		#
		if 'Result' in key:
			kresult = key['Result']
			if isinstance(kresult, dict):
				kresult = [ kresult ]
			if isinstance(kresult, list):
				for res in kresult:
					if "@VK" in res:
						kname = res['@VK'].replace("VK_", "")
						vk_to_sc[kname] = {
							"scancode": sckey,
						}
						text = html.unescape(res["@Text"])
						if "@With" in res:
							if res["@With"] == "VK_NUMLOCK":
								vk_to_sc[kname]['num'] = text
							if res["@With"] == "VK_SHIFT":
								vk_to_sc[kname]['shift'] = text
							if res["@With"] == "VK_CONTROL VK_MENU":
								vk_to_sc[kname]['altgr'] = text
							if res["@With"] == "VK_MENU":
								vk_to_sc[kname]['alt'] = text
						else:
							vk_to_sc[kname]['letter'] = text
						continue
					# print("-", res)
					# VK_NUMLOCK VK_SHIFT VK_MENU
					# altgr = VK_CONTROL VK_MENU
					if '@Text' not in res:
						if '@TextCodepoints' in res:
							text = chr(int(res["@TextCodepoints"],16))
							text = filter_codepoints(text)
						else:
							if "DeadKeyTable" in res:
								for deadres in res["DeadKeyTable"]["Result"]:
									if deadres["@With"] == " ":
										text = deadres["@Text"]
										if "@With" in res:
											if res["@With"] == "VK_NUMLOCK":
												vk_to_sc[name]['num'] = text
											if res["@With"] == "VK_SHIFT":
												vk_to_sc[name]['shift'] = text
											if res["@With"] == "VK_CONTROL VK_MENU":
												vk_to_sc[name]['altgr'] = text
											if res["@With"] == "VK_MENU":
												vk_to_sc[name]['alt'] = text
										else:
											vk_to_sc[name]['letter'] = text
								if DEBUG: print("DEAD", vk_to_sc[name],)
							continue
					else:
						text = html.unescape(res["@Text"])
					if "@With" in res:
						if res["@With"] == "VK_NUMLOCK":
							vk_to_sc[name]['num'] = text
						if res["@With"] == "VK_SHIFT":
							vk_to_sc[name]['shift'] = text
						if res["@With"] == "VK_CONTROL VK_MENU":
							vk_to_sc[name]['altgr'] = text
						if res["@With"] == "VK_MENU":
							vk_to_sc[name]['alt'] = text
					else:
						vk_to_sc[name]['letter'] = text
			else:
				if DEBUG: print("What is Result ?", kresult)

	if DEBUG: print("<<< vk_to_sc : " + str(len(vk_to_sc)) + " >>>")
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

def get_usb_keycodes():
	usb_sc_to_kc = {}
	for (keycode, scancode, note) in usbif_keycode_scancode:
		if scancode != 0:
			if scancode in usb_sc_to_kc:
				old = usb_sc_to_kc[scancode]
				if DEBUG: print(f"{RED}Scancode is twice {scancode} > {keycode} or {old}{NOC}")
			else:
				usb_sc_to_kc[scancode] = keycode
	return usb_sc_to_kc

########################################################################

class LayoutData:
	def __init__(self, asciis, charas, altgr, high):
		self.asciis = asciis
		self.charas = charas
		self.altgr = altgr
		self.high = high

def get_layout_data(virtual_key_defs_lang):
	asciis = [0] * 128
	charas = [""] * 128
	SHIFT_FLAG = 0x80
	NEED_ALTGR = ""
	HIGHER_ASCII = {}
	
	sc_to_kc = get_scancode_to_keycode()
	usb_sc_to_kc = get_usb_keycodes()

	# loop the list of virtual keycodes that exist in the language
	for num, virtualkey in enumerate(virtual_key_defs_lang):
		# the info on the key
		key_info = virtual_key_defs_lang[virtualkey]
		# scancode of the key
		scancode = key_info["scancode"]
	
		# matching keycodes
		keycode = None
		if scancode in sc_to_kc:
			keycode = sc_to_kc[scancode]
		if scancode in SPECIAL_KEYCODES:
			if keycode is None:
				keycode = SPECIAL_KEYCODES[scancode]
				if DEBUG: print(CYAN + f"SPECIAL scancode:{scancode} > keycode:{keycode}" + NOC)
			else:
				if keycode != SPECIAL_KEYCODES[scancode]:
					if DEBUG: print(RED + "Different:", keycode, SPECIAL_KEYCODES[scancode])
		"""
		# This does nothing good
		if scancode in usb_sc_to_kc:
			if keycode is None:
				keycode = usb_sc_to_kc[scancode]
				print(GREEN + f"USB IF scancode:{scancode} > keycode:{keycode}" + NOC)
			else:
				if keycode != usb_sc_to_kc[scancode]
					print(RED + "USB Different:", keycode, usb_sc_to_kc[scancode])
		"""
		if keycode is None:
			# TODO: check there's none missing
			if DEBUG: print(BLUE + "Unknown scancode", virtualkey, scancode)
			if DEBUG: print("    ", key_info, NOC)
			continue
		# find the letter somehow
	
		if scancode == 0x12:
			if DEBUG: print("<>"*40)

		# letter as defined in the keyboard definition
		if "letter" in key_info:
			letter = key_info["letter"]
			pos = ord(letter)
			if DEBUG: print("L", num, pos, letter, scancode, hex(keycode))
			if pos < 128:
				if not charas[pos]:
					asciis[pos] = keycode
					charas[pos] = letter
			else:
				if letter not in HIGHER_ASCII:
					HIGHER_ASCII[letter] = keycode
				else:
					if DEBUG: print(RED+"double", letter, HIGHER_ASCII[letter], NOC)

		if "shift" in key_info:
			letter = key_info["shift"]
			pos = ord(letter)
			if DEBUG: print("S", num, pos, letter, scancode, hex(keycode | SHIFT_FLAG))
			if pos < 128:
				if letter == "+":
					if DEBUG: print("+", charas[pos])
				if not charas[pos]:
					asciis[pos] = keycode | SHIFT_FLAG
					charas[pos] = letter
					if DEBUG: print("------ SHIFT ", charas[pos])
			else:
				if letter not in HIGHER_ASCII:
					HIGHER_ASCII[letter] = keycode | SHIFT_FLAG
				else:
					if DEBUG: print(RED+"double", letter, HIGHER_ASCII[letter], NOC)

		if "altgr" in key_info:
			letter = key_info["altgr"]
			if letter in NEED_ALTGR:
				if DEBUG: print(RED+"Already in NEED_ALTGR", letter, NOC)
			else:
				NEED_ALTGR += letter
			pos = ord(letter)
			if DEBUG: print("A", num, pos, letter, scancode, hex(keycode))
			if pos < 128:
				if not charas[pos]:
					asciis[pos] = keycode
					charas[pos] = letter
			else:
				if letter not in HIGHER_ASCII:
					HIGHER_ASCII[letter] = keycode
				else:
					if DEBUG: print(RED+"double", letter, HIGHER_ASCII[letter], NOC)

		if "num" in key_info:
			letter = key_info["num"]
			# if DEBUG: print("NUM", key_info)
	
		if letter == "+":
			if DEBUG: print("--- LETTER IS + ------------------------------------")
	
	return LayoutData(
		asciis,
		charas,
		NEED_ALTGR,
		HIGHER_ASCII,
	)


def make_output_file(output_file, layout_data, platform, lang):
	output_file_data = (
		"from keyboard_layout import KeyboardLayout\n"
		+ f"class KeyboardLayout{platform.title()}{lang.title()}(KeyboardLayout):\n"
		"    ASCII_TO_KEYCODE = (\n"
	)
	for x in range(128):
		keycode = layout_data.asciis[x]
		chara = layout_data.charas[x]
		output_file_data += f"        b'\\x{keycode:02x}'  # {repr(chara)}\n"
	output_file_data += (
		"    )\n"
		"    NEED_ALTGR = "+repr(layout_data.altgr)+"\n"
		"    HIGHER_ASCII = {\n"
	)
	for k, c in layout_data.high.items():
		output_file_data += f"        {repr(k)}: 0x{c:02x},\n"
	output_file_data += "    }\n"

	with open(output_file, "w") as fp:
		fp.write(output_file_data)

def compare_lang(layout_data, lang="fr"):
	import sys
	sys.path.append("./libraries")
	if lang == "fr":
		from keyboard_layout_win_fr import KeyboardLayoutWinFr as KeyboardLayoutLang
	elif lang == "de":
		from keyboard_layout_win_de_de import KeyboardLayoutWinDeDe as KeyboardLayoutLang
	else:
		return
	for x in range(128):
		this = layout_data.asciis[x]
		ref = KeyboardLayoutLang.ASCII_TO_KEYCODE[x]
		if this != ref:
			print(f"{str(x).ljust(4)} {repr(chr(x))}: {this:02x} != {ref:02x}")

# 	print(repr(layout_data.altgr))
# 	for k, c in layout_data.high.items():
# 		print(f"- {repr(k)}: 0x{c:02x}")

# TODO: le backtick et tilde sont dans la DeadKeyTable à with=" "
# € ne prend pas de shift, mais il en a un dans la table

# print( ("#"*70 + "\n") * 4 )
# print(output_file_data)


@click.group(invoke_without_command=True)
@click.option("--file", "-f", required=True)
@click.option("--lang", "-l", default="")
@click.option("--platform", "-p", default="win")
@click.option("--output", "-o", is_flag=True)
@click.option("--output-file", default="")
@click.option("--debug/--no-debug", "-d", is_flag=True)
def main(file, lang, platform, output, output_file, debug):
	global DEBUG
	DEBUG = debug
	if not platform:
		platform = "Win"
	if not lang:
		lang = file.split('.')[0].split('_')[-1].split('-')[-1]
	# file = FILE_INTERNATIONAL
	if DEBUG:
		print(">", file)
		print(">", platform)
		print(">", lang)
	with open(file, "r") as fp:
		data = fp.read()
	virtual_key_defs_lang = get_vk_to_sc(data)
	layout_data = get_layout_data(virtual_key_defs_lang)
	if DEBUG:
		compare_lang(layout_data, lang)
	if output or output_file:
		os.makedirs(BUILD_DIR, exist_ok=True)
		if not output_file:
			output_file = os.path.join(BUILD_DIR, f"test_keyboard_layout_{platform.lower()}_{lang.lower()}.py")
		print(CYAN + f"Write to {output_file}" + NOC)
		make_output_file(output_file, layout_data, platform, lang)

if __name__ == "__main__":
	main()
