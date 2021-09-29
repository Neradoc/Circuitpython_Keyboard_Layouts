#!/bin/sh

echo "##########################################################"
echo "# US        ##############################################"
python3 -m generator -k _xml/win/kbdlayout-info-us.xml -o
echo "# KEYCODE   ##############################################"
python3 tests/compare_keycodes.py -l new -r old _build/generated/keycode_win_us.py generator/keycode_us_ref.py
echo "# LAYOUT    ##############################################"
python3 tests/compare_layouts.py -l new -r old _build/generated/keyboard_layout_win_us.py tests/reference/keyboard_layout_us.py

echo "##########################################################"
echo "# FR        ##############################################"
python3 -m generator -k _xml/win/kbdlayout-info-fr.xml -o
echo "# LAYOUT    ##############################################"
python3 tests/compare_layouts.py -l new -r old _build/generated/keyboard_layout_win_fr.py libraries/layouts/keyboard_layout_win_fr.py
echo "# WRITE     ##############################################"
python3 tests/keyboard_test.py _build/generated/keyboard_layout_win_fr.py

echo "##########################################################"
echo "# DE        ##############################################"
python3 -m generator -k _xml/win/kbdlayout-info-de.xml -o
echo "# LAYOUT    ##############################################"
python3 tests/compare_layouts.py -l new -r old _build/generated/keyboard_layout_win_de.py libraries/layouts/keyboard_layout_win_de.py

echo "##########################################################"
echo "# CZ        ##############################################"
python3 -m generator -k _xml/win/kbdlayout-info-cz.xml -o
echo "# WRITE     ##############################################"
python3 tests/keyboard_test.py _build/generated/keyboard_layout_win_cz.py
