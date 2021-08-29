#!/bin/bash

LISTE="fr de br swe"

for lang in $LISTE; do
	python3 -m generator -f _xml/win/kbdlayout-info-$lang.xml -o
	cp _build/generated/keyboard_layout_win_$lang.py libraries/
	cp _build/generated/keycode_win_$lang.py libraries/
done
