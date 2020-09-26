# David Martinez
#9/26/2020

import sys
import math
from colorama import Fore, Back, Style 

x = sys.argv
listArgv = []
argvLen = len(x)
numList = x[1:argvLen]

print("length: "+ str(argvLen))
print("arg is: "+ str(x))
print(numList)

numLen = len(numList)
print(numLen)
sortedList= sorted(numList)

min = 0
max = 0
mean = 0
median = 0
mode = 0
range = 0

def Min():
    #Find Mimimum
    global min
    global sortedList
    min = sortedList[0]
def Max(sortedNums):
    #Find Max of set
    global max
    global numLen
    max = sortedList[numLen-1]  
def Mean(sortedNums):
    #Find Mean of set
    global mean
    global numLen
    numTotals = 0
    for x in sortedNums:
        c = float(x)
        numTotals = float(numTotals) + c
    #
    mean = numTotals / numLen

numLen2 = numLen
numLen3 = numLen

def medianF(sortedNums):
    #find median
    
    numList2 = sortedNums

    if((numLen2 % 2) == 0):
        print("even length")
        #print(numLen2)
        initialReducer = numLen2 +1
        rounds =  int(numLen2) / 2  # rounds of loping to clip beginning and end
        rounds = rounds - 1
        lastDel = initialReducer - 2

        while rounds > 0:
            #print("removing")
            del numList2[lastDel]
            del numList2[0]
            lastDel -= 2
            rounds -= 1
            print(numList2)
        #medSum = (float(numList2[0]) + float(numList[1]))
        med1 = float(numList2[0])
        med2 = float(numList2[1])
        medSum = med1 + med2
        medianLoc = medSum / 2
        print(medSum)
        global median
        median = medianLoc
        print(median)

    # FOR ODD Lengthed data
    elif((numLen3 % 2) != 0):
        print("odd length")
        initialReducer = numLen2 +1
        rounds =  numLen2 // 2  # rounds of loping to clip beginning and end
        rounds = rounds # no need to subract like previous because odd will reduce to one final number
        lastDel = initialReducer - 2

        while rounds > 0:
            #print("removing")
            del numList2[lastDel]
            del numList2[0]
            lastDel -= 2
            rounds -= 1
            print(numList2)
            medianLoc = float(numList2[0])
            print("median sum is: "+ str(medianLoc))
            median = medianLoc
            print(median)

    #
#
def Mode(sortedNums):
    global mode
    sortedNums = sorted(sortedNums)
    dictM = {}
    setList = []
    # create set list by finding every number in set with no duplicates
    for x in sortedNums:
        if x in setList:
            continue
        else:
            setList.append(x)
    print("set is: "+ str(setList))

    #start each counter at 0  for dictionary
    for x in setList:
        dictM[x] = 0
    print(dictM)

    # find how many times the each number of set occurs within the original data set
    for x in setList:
        for y in sortedNums:
            if(x == y):
                dictM[x] += 1
                print(x)
    print(dictM)

    keys = list(dictM.keys())
    vals = list(dictM.values())
    """
    r = len(setList)
    rows, cols = (r, 2) 
    arr = [[0]*cols]*rows 
    print(arr) 
    """

    arr = []
    e = 0
    for x in dictM:
        print(x)
        print(dictM[x])
        print("e is: "+ str(e))
        arr.append([x,dictM[x]])
        e += 1
        print(arr)
    #
    arr = sorted(arr, key = lambda x: x[1]) #sort by second element in lists
    print(arr)
    print("lenght of list: "+ str(len(arr)))
    # index [0] is the number while index [1] is the number of times it occurs
    if arr[-1][1] == arr[-2][1]:
        mode = arr[-1][0], arr[-2][0]
        print(mode)
        

    else:
        print(arr[-1][0])
        mode = arr[-1][0]
#
# MUST BE CALLED AFTER MIN AND MAX HAVE ALREADY BEEN UPDATED WITH DATA SET
def Range(sortedNums):
    global range
    global max
    global min
    range = float(max) - float(min)

Min()
Mode(sortedList)
Max(sortedList)
Mean(sortedList)
medianF(sortedList)
Range(sortedList)

print(Fore.GREEN+ Style.BRIGHT+ Back.BLACK+" ")
ptMin = Fore.GREEN + "Minimum: "+str(min)
ptMax = "Maximum: " + str(max)
print("+--------------------+")
print("|"+ptMin.center(25," ")+"|")
print("|"+ ptMax.center(20," ")+"|")
print("+--------------------+")

print("Mean: "+ str(mean))
print("Median: "+ str(median))
print("Mode(s): "+ str(mode))
print("Range: "+ str(range))
print(Style.RESET_ALL)
         



