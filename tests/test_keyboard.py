import os
import sys
import click

class Keyboard:
    def __init__(self, *whatever):
        pass
    def press(self, *keycodes):
        print(" +", ["0x"+f"{k:02x}".upper() for k in keycodes], end="")
    def release(self, *keycodes):
        print(" -", ["0x"+f"{k:02x}".upper() for k in keycodes], end="")
    def release_all(self):
        print(" ;")
    def send(self, *keycodes):
        print(" <", ["0x"+f"{k:02x}".upper() for k in keycodes], ">")


@click.group(invoke_without_command=True)
@click.argument("keycodes", nargs=1)
def main(keycodes):
    print(keycodes)

    keyboard = Keyboard()
    sys.path.append(os.path.dirname(keycodes))
    sys.path.append("libraries/common")
    sys.path.append("libraries/layouts")
    sys.path.append("libraries/keycodes")

    layout_module = __import__(os.path.basename(keycodes)[:-3])
    layout = layout_module.KeyboardLayout(keyboard)
    print("="*70)
    TESTS = (
        ("0x14 [0xE1 0x14] 0x1E [0xE1 0x1E] [0xE6 0x27] 0x2C", "aA&1@ "),
        ("[0xE6 0x26] (pas 0x2F 0x2C)", "^"),
        ("[0xE6 0x26] 0x14 0x2f 0x14", "^aâ"),  # fr
        ("[0xE6 0x1F] 0x2C [0xE6 0x1F] [0xE1 0x11]", "~Ñ"),  # fr
        ("[0xE1 0x2F] 0x12 0x2f [0xE1 0x08]", "öÊ"),  # fr
        ("???", "ůĢ˝"),  # cz
    )
    for a, b in TESTS:
        try:
            print(a)
            layout.write(b)
        except ValueError as er:
            click.secho(er, fg="red")


if __name__ == "__main__":
    main()
