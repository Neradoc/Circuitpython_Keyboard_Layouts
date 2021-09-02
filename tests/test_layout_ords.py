import os
import importlib.util
import click
import sys
sys.path.append("libraries/common")
sys.path.append("libraries/layouts")
sys.path.append("libraries/keycodes")

def load_module(file, name):
    spec = importlib.util.spec_from_file_location(name, file)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo

@click.group(invoke_without_command=True)
@click.argument("keyboard_layout", nargs=1)
def main(keyboard_layout):
    print(keyboard_layout)
    layout = load_module(keyboard_layout, "layout")

    ASCII = layout.KeyboardLayout.ASCII_TO_KEYCODE
    hîģh_äşčìÆí = layout.KeyboardLayout.HIGHER_ASCII
    ČÔMBÏŅĖĎ_ĶËÝŠ = layout.KeyboardLayout.COMBINED_KEYS

    total_char = len(hîģh_äşčìÆí) + len(ČÔMBÏŅĖĎ_ĶËÝŠ)
    unicode_chars = 0

    print("Higher ASCII")
    for x in hîģh_äşčìÆí:
        oo = ord(x)
        if oo >= 256:
            unicode_chars += 1
            print("-", x, f"{oo:04x}", "*" * (oo // 256))

    print("Combined Keys")
    for x in ČÔMBÏŅĖĎ_ĶËÝŠ:
        oo = ord(x)
        if oo >= 256:
            unicode_chars += 1
            print("-", x, f"{oo:04x}", "*" * (oo // 256))

    print("Unicode above ASCII: {pct:.1f}%".format(pct = 100 * unicode_chars / total_char))

if __name__ == "__main__":
    main()
