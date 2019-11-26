#!/bin/sh

cd /home/pi/ivt490-datalog || exit 1

git checkout datalog >/dev/null 2>&1 || exit 1

git add *.txt >/dev/null 2>&1
git commit -m "log update $(date)" >/dev/null 2>&1 &&
git push origin datalog >/dev/null 2>&1
