def linearSearch(customList, value):
    for i in range(len(customList)):
        if customList[i] == value:
            return i
    return -1

cList = [2,4,1,6,4,8,9,6,7]
print(linearSearch(cList, 9))