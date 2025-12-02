#!/usr/bin/env python3
# 2023 Day 2 Part 1
#-------------------
# A Walking game with Stones.
# 
# honestyly some bullshit about possible games given
# information revealed about stones in a bag with a 
# variable number of draws. Not really sure what this 
# is about but hey it's maths right.
#
# frankly it looks like parsing the games is a bigger
# piece but hey that's mechanistic.

datafile="data/day2.txt"

#######################################################
# game line looks like:
# SCOUNT = "<x> blue|red|green"
# DRAW = SCOUNT[, SCOUNT]*
# Game <n>: DRAW[; DRAW]*
def parseGame(text) :
    meta=text.split(': ')
    id=int(meta[0].split('Game ')[1])
    draws=meta[1].split('; ')
    gDraws=[]
    for draw in draws :
        dParsed={}
        stones=draw.split(', ')
        for stone in stones :
            (num,colour)=stone.split(' ',1)
            dParsed[colour] = int(num)
        gDraws.append(dParsed)
    return id,gDraws

#######################################################
# Check a game against the conditions. Fails if any 
# DRAW exceeds the defined limits
def checkGame(game) :
    limits = { 'red' : 12, 'green' : 13, 'blue' : 14 }
    for draw in game :
        for c in draw.keys() :
            if draw[c] > limits[c] :
                print(f"Saw {draw[c]} of {c}; limit is {limits[c]}")
                return False
    return True
        
#######################################################
#######################################################
#######################################################
if __name__ == "__main__" :
    resultSum = 0
    with open(datafile,'r') as df :
        for line in df:
            (id,info)=parseGame(line.strip())
            print(f"Checking Game {id}",end="...")
            if checkGame(info) :
                print(f"VALID")
                resultSum += id
    print(f"Answer: {resultSum}")
            