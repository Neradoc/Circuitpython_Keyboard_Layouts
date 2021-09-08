#!/bin/bash

mkdir -p _build/generated
mkdir -p _build/compiled

for thingy in `find _build/generated`; do
	if [[ "$thingy" == *.py ]]; then
		echo $thingy
		mpy-cross $thingy
		MPYNAME=`echo $thingy | sed -e 's/\.py$/.mpy/'`
		mv "$MPYNAME" "_build/compiled/"
	fi
done

mpy-cross libraries/common/keyboard_layout.py
mv libraries/common/keyboard_layout.mpy "_build/compiled/"
