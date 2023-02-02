def pivot(customList, pivot_index, end_index):
    swap = pivot_index
    for j in range(pivot_index+1, end_index+1):
        if customList[j] < customList[pivot_index]:
            swap += 1
            customList[swap], customList[j] = customList[j], customList[swap]
    
    customList[swap], customList[pivot_index] = customList[pivot_index], customList[swap]
    return swap

def quickSort_helper(customList, l, r):
    if l < r:
        pvt = pivot(customList, l, r)

        quickSort_helper(customList, l, pvt - 1)
        quickSort_helper(customList, pvt + 1, r)

    return customList

def quickSort(customList):
    return quickSort_helper(customList, 0, len(customList) - 1)


cList = [5,2,4,7,8,6,9,12,3]
print(quickSort(cList))
# print(cList)

                