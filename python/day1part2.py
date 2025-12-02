#!/usr/bin/env python3
# 2023 Day 1 Part 2
#-------------------
# something something blah calibration document
#
# take first and last digit but -sneaky,sneaky-
# some of the numbers are spelt out. And share
# letters - eightwo = 82
#
import re 

datafile="data/day1.txt"

#Process lines from the datafile, extract the numbers
dRex = re.compile('\\d')
answerResult=0
with open(datafile,'r') as df:
    for l in df:
        ol=l.strip()
        #HACK - because 1st and last letters of number can be shared with preceeding/following number, just put the ACTUAL number in the middle.
        l = l.strip().replace('one','o1e').replace('two','t2o').replace('three','thr3e').replace('four','fo4r').replace('five','fi5e').replace('six','s6x').replace('seven','se7en').replace('eight','ei8ht').replace('nine','ni9e')
        digits = dRex.findall(l)
        print(f"{ol}->{l} contains {digits}",end="...")
        if len(digits) <2 :
            num = int(digits[0] + digits[0])
        else :
            num = int(digits[0] + digits[-1])
        print(f" taking {num}")
        answerResult += num

print(f"solution: {answerResult}")