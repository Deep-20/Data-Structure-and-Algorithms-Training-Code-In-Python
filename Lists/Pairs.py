def pairSum(myList, sum):
    # TODO
    ans = []

    for i in range(len(myList)):
        if sum - myList[i] in myList[i+1:]:
            temp = '' + str(myList[i]) + "+" + str(sum - myList[i])
            ans.append(temp)

    return ans

print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))