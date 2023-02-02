
def numOfPathsToReachLastCell(matrix, totalCost):

    rows = len(matrix)
    columns = len(matrix[0])

    if rows == 1 and columns == 1:
        if totalCost - matrix[0][0] == 0:
            return 1
        else:
            return 0
    elif rows > 1 and columns == 1:
        if totalCost - matrix[0][0] >= 0:
            return numOfPathsToReachLastCell(matrix[1:], totalCost - matrix[0][0])
        else:
            return 0
    elif rows == 1 and columns > 1:
        if totalCost - matrix[0][0] >= 0:
            return numOfPathsToReachLastCell([ item[1:] for item in matrix], totalCost - matrix[0][0])
        else:
            return 0
    else:
        if totalCost - matrix[0][0] >= 0:
            result1 = numOfPathsToReachLastCell(matrix[1:], totalCost - matrix[0][0])
            result2 = numOfPathsToReachLastCell([ item[1:] for item in matrix], totalCost - matrix[0][0])

            return result1 + result2
        else:
            return 0


matrix = [[4, 7, 1, 6],
         [5, 7, 3, 9],
         [3, 2, 1, 2],
         [7, 1, 6, 3]]

print(numOfPathsToReachLastCell(matrix, 25))