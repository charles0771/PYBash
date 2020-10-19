#!/bin/bash
if [ `whoami` == 'root' ]; then
		python3 PyBash.py
else
	echo 'The software needs root privileges. Enter your password here and then execute exactly this without quotes: "python3 PyBash.py".'
		su
fi

python3 PyBash.py
