import os
import sys
import click
import importlib.util
import xmltodict
sys.path.append("libraries/common")
sys.path.append("libraries/layouts")
sys.path.append("libraries/keycodes")

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
