#!/usr/bin/python3
"""If you have a Dvorak layout no your host system, you'll have QWERTY layout on UHK most of the time. 
In this configuration, when you'll use `write` statement in a macro, UHK will send wrong keycodes and output gibberish, 
much like a qwerty-person would, when trying to type on a machine with a Dvorak layout.

example:
../uhk% ./uhkcmd.sh 'write hello'
../uhk% d.nnr


This script simulates this behaviour and gives you gibberish you can then put into your macro to get a normal text.


usage:
../uhk% echo hello | ./undvorak.py
jdpps


you can then use the output in a macro to get a normal text:
../uhk% ./uhkcmd.sh 'write jdpps'
../uhk% hello

I think the better way is to just change the keymap in macro just before using the write statement, 
but this does not actually change the sent keycodes at the moment."""

import sys


IO = ("',.pyfgcrl/=aoeuidhtns-\;qjkxbmwvz" + '"<>PYFGCRL?+AOEUIDHTNS_|:QJKXBMWVZ' + '[]',  # dvorak
      "-wvlfuijpnz]ar.gcedybo[\s'htqxm,k;" + '_WVLFUIJPNZ}AR>GCEDYBO{|S"HTQXM<K:' + '/=')  # what UHK types

MAP = dict(zip(IO[1], IO[0]))

print("".join([MAP.get(s,s) for s in sys.stdin.read()]), end='')  # if not in the map, probably is the same symbol

