#!/bin/bash

LISTE="fr:fr gr:dede br:br sw:sw da:da cz1:cz1 cz:cz"

for LL in $LISTE; do
	IFS=":"
	read -ra AA <<< "$LL"
	FILE=${AA[0]}
	LANG=${AA[1]}
	IFS=" "
	echo https://kbdlayout.info/kbd$FILE + _${FILE}_ _${LANG}_
	# python3 -m generator -k _xml/win/kbdlayout-info-$lang.xml -o
	python3 -m generator -o -k https://kbdlayout.info/kbd"$FILE" --lang "$LANG"
	cp _build/generated/keyboard_layout_win_$LANG.py libraries/
	cp _build/generated/keycode_win_$LANG.py libraries/
done
