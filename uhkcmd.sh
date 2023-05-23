#!/bin/bash
# tell UHK to run some macro command
# example: ./uhkcmd "write hello"

hidraw=`grep 'UHK 60' /sys/class/hidraw/hidraw*/device/uevent | LC_ALL=C sort -h | head -n 1 | grep -o 'hidraw[0-9][0-9]*'`
echo -e "\x14$*" > "/dev/$hidraw"

