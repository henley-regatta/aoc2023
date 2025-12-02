#!/usr/bin/env python3
# 2023 Day 2 Part 1
#-------------------
#It's not a schematic it's a very silly map
#
# Parse numbers off a map, but only sum those 
# adjacent to a symbol (any non-space char other than '.')

datafile="data/day3.txt"

#######################################################
def parseNumbersFromLine(line) :
    inNum=False
    nStr=""
    sPos=0
    listOfNumbers=[]
    for x in range(0,len(line)) :
        if line[x] in "0123456789":
            nStr += line[x]
            if not inNum :
                sPos=x      
                inNum=True 
        else :
            if inNum : #number has finished
                listOfNumbers.append([sPos,sPos+len(nStr)-1,nStr])
                nStr=""
                inNum=False 
    #handle end of line
    if inNum :
        listOfNumbers.append([sPos,sPos+len(nStr)-1,nStr])
        
    return listOfNumbers

#######################################################
def parseSymbolsFromLine(line) :
    listOfSymbols=[]
    for x in range(0,len(line)) :
        if line[x] not in ".0123456789":
            listOfSymbols.append(x)
    return listOfSymbols

#######################################################
#######################################################
#######################################################
if __name__ == "__main__" :
    numbers=[]
    symbols=[]
    orglines=[]
    with open(datafile,'r') as df:
        for line in df: 
            line = line.strip()
            orglines.append(list(line))
            numbers.append(parseNumbersFromLine(line))
            symbols.append(parseSymbolsFromLine(line))

    #number-by-number search for hits
    #it's a hit if there's a symbol: a) at startX-1 b) at endX+1 c) at y-1 with a to b d) at y+1 with a to b
    bigNumSum=0
    y=-1
    for row in numbers :
        y+=1
        for num in row :
            isValid=False
            xMin = num[0]-1
            xMax = num[1]+1
            yMin = y-1
            if yMin<0 : 
                yMin=0
            yMax = y+1
            if yMax >= len(numbers) :
                yMax=len(numbers)-1
            for checky in range(yMin,yMax+1) :
                syms = symbols[checky]
                for symPos in syms :
                    if symPos >= xMin and symPos <= xMax :
                        isValid=True
                        bigNumSum += int(num[2])
                        for x in range(num[0],num[1]+1) :
                            orglines[y][x] = 'Y'
                        break
                if isValid :
                    break 
            if not isValid:
                #X-out the original number
                for x in range(num[0],num[1]+1) :
                    orglines[y][x] = 'X'
    for l in orglines :
        print(''.join(l))
    print(f"\n\nthe answer you seek is: {bigNumSum}")