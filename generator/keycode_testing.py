import html
import json
import natsort
import os
import pprint
import importlib.util

import click
import xmltodict

# scancode / keycode
SPECIAL_KEYCODES = {
    # key, shift, option, shift-option
    0x56: 0x64,  # ["<",">","≤","≥"]
    0x29: 0x35,  # ["@","#","•","Ÿ"] ² on windows
}

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

def load_module(file, name):
    spec = importlib.util.spec_from_file_location(name, file)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

@click.group(invoke_without_command=True)
@click.argument("keycodes", nargs=2)
def main(keycodes):
    print(keycodes)
    left = load_module(keycodes[0], "left")
    right = load_module(keycodes[1], "right")

    lnames = set(dir(left.Keycode))
    rnames = set(dir(right.Keycode))

    print("-"*70)
    print(sorted(lnames - rnames))
    print("-"*70)
    print(sorted(rnames - lnames))
    print("-"*70)

    for x in lnames & rnames:
        if x.upper() != x or x[0] == "_":
            continue
        lk = getattr(left.Keycode, x)
        rk = getattr(right.Keycode, x)
        if lk != rk:
            print(f"{x}: {lk} ≠ {rk}")


if __name__ == "__main__":
    main()
