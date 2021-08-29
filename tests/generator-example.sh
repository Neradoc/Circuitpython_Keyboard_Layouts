#!/bin/sh

python3 -m generator -f _xml/win/kbdlayout-info-us.xml -o
python3 generator/testing_keycode.py _build/generated/keycode_win_us.py generator/keycode_us_ref.py
python3 generator/testing_layout.py _build/generated/keyboard_layout_win_us.py generator/keyboard_layout_us_ref.py

python3 -m generator -f _xml/win/kbdlayout-info-fr.xml -o
python3 generator/testing_layout.py _build/generated/keycode_win_fr.py libraries/keyboard_layout_win_fr.py

python3 -m generator -f _xml/win/kbdlayout-info-de.xml -o
python3 generator/testing_layout.py _build/generated/keycode_win_de.py libraries/keyboard_layout_win_de_de.py
