

def minCostToReachLastCell(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    if rows == 1 and columns == 1:
        return matrix[0][0]
    elif rows == 1 and columns > 1:
        return matrix[0][0] + minCostToReachLastCell([ item[1:] for item in matrix])
    elif rows > 1 and columns == 1:
        return matrix[0][0] + minCostToReachLastCell(matrix[1:])
    else:
        result1 = matrix[0][0] + minCostToReachLastCell([ item[1:] for item in matrix])
        result2 = matrix[0][0] + minCostToReachLastCell(matrix[1:])
        return min(result1, result2)


matrix = [[4, 7, 8, 6, 4],
         [6, 7, 3, 9, 2],
         [3, 8, 1, 2, 4],
         [7, 1, 7, 3, 7],
         [2, 9, 8, 9, 3]]

print(minCostToReachLastCell(matrix))