import os
import sys
import click

class Keyboard:
    def __init__(self, *whatever):
        pass
    def press(self, *keycodes):
        print("press", keycodes)
    def release(self, *keycodes):
        print("release", keycodes)
    def release_all(self):
        print("release-all")
    def send(self, *keycodes):
        print("send", keycodes)


@click.group(invoke_without_command=True)
@click.argument("keycodes", nargs=1)
def main(keycodes):
    print(keycodes)

    keyboard = Keyboard()
    sys.path.append(os.path.dirname(keycodes))
    sys.path.append("libraries")

    layout_module = __import__(os.path.basename(keycodes)[:-3])
    layout = layout_module.KeyboardLayout(keyboard)
    print("="*70)

    layout.write("aA &1")
    print("-"*70)
    layout.write("^")
    layout.write("ÑöÊ")


if __name__ == "__main__":
    main()
