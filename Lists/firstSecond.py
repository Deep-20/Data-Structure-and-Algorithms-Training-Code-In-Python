def firstSecond(givenList):
    # TODO
    set1 = set(givenList)
    newList = list(set1)
    
    newList.sort()
    return newList[-1], newList[-2]

print(firstSecond([23,87,90,87,45,68,90]))