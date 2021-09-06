import os
import sys
import click

class Keyboard:
    def __init__(self, *whatever):
        self.chars = []
        self.codes = []
    def press(self, *keycodes):
        for x in keycodes:
            self.codes.append(x)
        #print(" +", ["0x"+f"{k:02x}".upper() for k in keycodes], end="")
    def release(self, *keycodes):
        pass
        #print(" -", ["0x"+f"{k:02x}".upper() for k in keycodes], end="")
    def release_all(self):
        self.chars.append(self.codes)
        self.codes = []
        #print(" ;")
    def send(self, *keycodes):
        self.chars.append(keycodes)
        #print(" <", ["0x"+f"{k:02x}".upper() for k in keycodes], ">")
    def start(self):
        self.chars = []
        self.codes = []


def show_list(source):
    out = []
    for x in source:
        if isinstance(x, int):
            out.append(f"0x{x:02x}")
        elif isinstance(x, list):
            out.append(show_list(x))
        else:
            out.append(repr(x))
    return "[" + " ".join(out) + "]"


@click.group(invoke_without_command=True)
@click.argument("keycodes", nargs=1)
def main(keycodes):
    print(keycodes)

    keyboard = Keyboard()
    sys.path.append(os.path.dirname(keycodes))
    sys.path.append("libraries/common")
    sys.path.append("libraries/layouts")
    sys.path.append("libraries/keycodes")

    layout_name = os.path.basename(keycodes)[:-3]
    layout_module = __import__(layout_name)
    layout = layout_module.KeyboardLayout(keyboard)

    sys.path.append("generator")
    from keycode_us_ref import Keycode as K

    SHIFT = 0xE1
    ALTGR = 0xE6

    print("="*70)
    TESTS00 = (
        (
            [K.E, [SHIFT, K.E], [SHIFT, K.SEVEN], [K.ONE], [SHIFT, K.TWO], K.SPACE],
            "eE&1@ "
        ),
    )
    TESTSFR = (
        (
            [K.E, [SHIFT, K.E], K.ONE, [K.SHIFT, K.ONE], [ALTGR, K.ZERO], K.SPACE],
            "eE&1@ "
        ),
        # not 0x2F 0x2C
        ([[ALTGR, K.NINE]], "^"),
        ([[ALTGR, K.NINE], K.E, 0x2F, K.E], "^eê"),  # fr
        ([[ALTGR, K.TWO], K.SPACE, [ALTGR, K.TWO], [SHIFT, K.N]], "~Ñ"),  # fr
        ([[SHIFT, 0x2F], K.O, 0x2F, [SHIFT, K.E]], "öÊ"),  # fr
    )
    TESTSCZ = (
        (
            [K.E, [SHIFT, K.E], [ALTGR, K.C], [SHIFT, K.ONE], [ALTGR, K.V], K.SPACE],
            "eE&1@ "
        ),
        # not 0x2F 0x2C
        ([[ALTGR, K.THREE], K.SPACE], "^"),
        ([[ALTGR, K.THREE], K.SPACE, K.E, [ALTGR, K.THREE], K.E], "^eê"),  # fr
        ([[ALTGR, K.MINUS], K.O, [ALTGR, K.THREE], [SHIFT, K.E]], "öÊ"),  # fr
        # note: ů = pas de altgr en solo
        ([0x33, [ALTGR, K.EQUALS], [SHIFT, K.G], [ALTGR, K.ZERO], K.SPACE], "ůĢ˝"),  # cz
    )

    if layout_name.endswith("fr"):
        TESTS = TESTSFR
    elif layout_name.endswith("cz"):
        TESTS = TESTSCZ
    else:
        TESTS = TESTS00

    for a, b in TESTS:
        try:
            a = show_list([ x if isinstance(x, list) else [x] for x in a ])
            keyboard.start()
            layout.write(b)
            print(a)
            chars = show_list(keyboard.chars)
            if a != chars:
                click.secho(chars, fg="red")
            else:
                click.secho(chars, fg="green")
        except ValueError as er:
            click.secho(er, fg="red")


if __name__ == "__main__":
    main()
