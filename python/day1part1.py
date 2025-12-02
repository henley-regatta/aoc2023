#!/usr/bin/env python3
# 2023 Day 1 Part 1
#-------------------
# something something blah calibration document
# Read lines and construct a number from the FIRST
# and LAST digits found on the line.
#
import re 


datafile="data/day1.txt"

#Process lines from the datafile, extract the numbers
dRex = re.compile('\\d')
answerResult=0
with open(datafile,'r') as df:
    for l in df:
        digits = dRex.findall(l)
        print(f"{l.strip()} contains {digits}",end="...")
        if len(digits) <2 :
            num = int(digits[0] + digits[0])
        else :
            num = int(digits[0] + digits[-1])
        print(f" taking {num}")
        answerResult += num

print(f"solution: {answerResult}")