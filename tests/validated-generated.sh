#!/bin/bash

LISTE="fr:fr gr:de br:br sw:sw da:da"

for LL in $LISTE; do
	IFS=":"
	read -ra AA <<< "$LL"
	FILE=${AA[0]}
	LANG=${AA[1]}
	IFS=" "
	echo https://kbdlayout.info/kbd$FILE + $FILE $LANG
	# python3 -m generator -k _xml/win/kbdlayout-info-$lang.xml -o
	python3 -m generator -o -k https://kbdlayout.info/kbd$FILE --lang $LANG
	cp _build/generated/keyboard_layout_win_$LANG.py libraries/
	cp _build/generated/keycode_win_$LANG.py libraries/
done

# git co adding-generated-layouts