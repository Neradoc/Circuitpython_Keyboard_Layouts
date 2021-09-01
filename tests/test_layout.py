import os
import importlib.util
import click
import sys
sys.path.append("libraries")

def load_module(file, name):
    spec = importlib.util.spec_from_file_location(name, file)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

@click.group(invoke_without_command=True)
@click.argument("keycodes", nargs=2)
@click.option("--lname", "-l", default="left")
@click.option("--rname", "-r", default="right")
def main(keycodes, lname, rname):
    print(keycodes)
    left = load_module(keycodes[0], "left")
    right = load_module(keycodes[1], "right")

    lASCII = left.KeyboardLayout.ASCII_TO_KEYCODE
    rASCII = right.KeyboardLayout.ASCII_TO_KEYCODE

    for x in range(len(lASCII)):
        c = chr(x)
        if lASCII[x] != rASCII[x]:
            print(f"{x}/{repr(c)}: {repr(lASCII[x])} ≠ {repr(rASCII[x])}")

    if left.KeyboardLayout.NEED_ALTGR != right.KeyboardLayout.NEED_ALTGR:
        print("NEED_ALTGR")
        print("   ", left.KeyboardLayout.NEED_ALTGR)
        print("   ", right.KeyboardLayout.NEED_ALTGR)

    lHIGH = left.KeyboardLayout.HIGHER_ASCII
    rHIGH = right.KeyboardLayout.HIGHER_ASCII

    for H in lHIGH:
        if H not in rHIGH:
            print(f"Only {lname} :", repr(H), hex(lHIGH[H]))
    for H in rHIGH:
        if H not in lHIGH:
            print(f"Only {rname}:", repr(H), hex(rHIGH[H]))
        elif rHIGH[H] != lHIGH[H]:
            print("Different :", repr(H), hex(lHIGH[H]), hex(rHIGH[H]))


if __name__ == "__main__":
    main()
