#!/bin/sh

python3 -m generator -f _xml/keything-us.xml -o
python3 generator/keycode_testing.py _build/generated/keycode_win_us.py generator/keycode_us_ref.py
