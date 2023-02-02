import math

# We will use Insertion Sort for sorting elements inside bucket
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j = j - 1
        customList[j + 1] = key
    return customList


def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_b - 1].append(j)
    
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    
    return customList

cList = [2,5,4,7,8,6,9,12,3]
bucketSort(cList)
print(cList)
