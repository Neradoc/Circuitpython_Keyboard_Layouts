#!/bin/bash

python3 -m generator -k _xml/win/kbdlayout-info-us.xml -o
python3 tests/keyboard_test.py _build/generated/keyboard_layout_win_us.py

python3 -m generator -k _xml/win/kbdlayout-info-fr.xml -o
python3 tests/keyboard_test.py _build/generated/keyboard_layout_win_fr.py

python3 -m generator -k _xml/win/kbdlayout-info-cz.xml -o
python3 tests/keyboard_test.py _build/generated/keyboard_layout_win_cz.py
