def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    
cList = [2,5,4,7,8,6,9,12,3]
bubbleSort(cList)
print(cList)