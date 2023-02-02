def selectionSort(customList):
    for i in range(len(customList)):
        minIndex = i
        for j in range(i+1, len(customList)):
            if customList[j] < customList[minIndex]:
                minIndex = j
        
        customList[minIndex], customList[i] = customList[i], customList[minIndex]

cList = [2,5,4,7,8,6,9,12,3]
selectionSort(cList)
print(cList)