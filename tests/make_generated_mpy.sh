#!/bin/bash

for thingy in `find _build/generated`; do
	if [[ "$thingy" == *.py ]]; then
		echo $thingy
		cp "$thingy" "_build/compiled/"
	fi
done
cp libraries/common/keyboard_layout.py "_build/compiled/"

cd _build/compiled
for thingy in `find .`; do
	if [[ "$thingy" == *.py ]]; then
		mpy-cross "$thingy"
		rm "$thingy"
	fi
done
