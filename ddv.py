#!/usr/bin/python3
"""I have a Dvorak-over-Dvorak situation with my UHK (which thinks that the host layout is always QWERTY) and my system, which is actually Dvorak.
This affects some macroses on my keyboard, because the keyboard sends the wrong keys when I ask it  to type some text.
The following is a map of this gibberish back to normal, so I can use the output of this script in "write" function in macroses.
usage:
../uhk% echo d.nnr | ./ddv.py
hello
"""
import sys


IO = ("',.pyfgcrl/=aoeuidhtns-\;qjkxbmwvz", "-wvlfuijpnz]ar.gcedybo[\s'htqxm,k;")
MAP = dict(zip(IO[1], IO[0]))

print("".join([MAP.get(s,s) for s in sys.stdin.read()]), end='')  # if not in the map, probably is the same symbol

