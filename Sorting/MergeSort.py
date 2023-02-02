# Helper Function -- Merges two subaraays with sorting
def merge(customList, l, m, r):            # l = First Index of List, m = Middle Index, r = Last Index
    n1 = m - l + 1                         # Number of elements in first sub array
    n2 = r - m                             # Number of elements in second sub array

    L = [0] * n1
    R = [0] * n2

    for i in range(0,n1):
        L[i] = customList[l + i]
    
    for j in range(0,n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)


cList = [2,5,4,7,8,6,9,12,3]
mergeSort(cList, 0, 8)
print(cList)