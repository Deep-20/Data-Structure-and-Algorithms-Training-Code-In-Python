def binarySearch(customList, value):
    left = 0
    right = len(customList) - 1
    middle = (left + right) // 2

    while customList[middle] != value and left <= right:
        if customList[middle] < value:
            left = middle + 1
        elif customList[middle] > value:
            right = middle - 1
        middle = (left + right) // 2
    
    if customList[middle] == value:
        return middle
    else:
        return -1

cList = [1,2,3,4,5,6,7,8,9]
print(binarySearch(cList, 0))