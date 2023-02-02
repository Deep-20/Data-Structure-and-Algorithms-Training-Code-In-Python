def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j = j - 1
        customList[j + 1] = key


cList = [2,5,4,7,8,6,9,12,3]
insertionSort(cList)
print(cList)
