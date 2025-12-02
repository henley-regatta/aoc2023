#!/usr/bin/env python3
# 2023 Day 2 Part 2
#-------------------
#It's not a schematic it's a very silly map
#
# Parse numbers off a map, but only sum the product of 
# numbers adjacent to a "*" symbol

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
def parseRatiosFromLine(line) :
    listOfRatios=[]
    for x in range(0,len(line)) :
        if line[x] == "*": 
            listOfRatios.append(x)
    return listOfRatios

#######################################################
#######################################################
#######################################################
if __name__ == "__main__" :
    numbers=[]
    ratios=[]
    orglines=[]
    with open(datafile,'r') as df:
        for line in df: 
            line = line.strip()
            orglines.append(list(line))
            numbers.append(parseNumbersFromLine(line))
            ratios.append(parseRatiosFromLine(line))

    #Ratio-by-Ratio search for matching numbers
    #it's a hit if there's a number: a) at startX-1 b) at endX+1 c) at y-1 with a to b d) at y+1 with a to b
    adjacentToRatio={}
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
                syms = ratios[checky]
                for symPos in syms :
                    if symPos >= xMin and symPos <= xMax :
                        isValid=True
                        for x in range(num[0],num[1]+1) :
                            orglines[y][x] = 'Y'
                        symPosCode=f"x{symPos}y{checky}"
                        if symPosCode not in adjacentToRatio :
                            adjacentToRatio[symPosCode] = [int(num[2])]
                        else :
                            adjacentToRatio[symPosCode].append(int(num[2]))
                        break
                if isValid :
                    break 
            if not isValid:
                #X-out the original number
                for x in range(num[0],num[1]+1) :
                    orglines[y][x] = 'X'
    for l in orglines :
        print(''.join(l))
    
    #One last pass thru the results. It's a gear ratio only if it contains
    #2 numbers
    bigAnswerSum=0
    for r in adjacentToRatio.keys() :
        if len(adjacentToRatio[r])==2 :
            bigAnswerSum += adjacentToRatio[r][0] * adjacentToRatio[r][1]
    print(f"The answer you seek is: {bigAnswerSum}")