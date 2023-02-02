# Given a matrix of NxN size, code to rotate the matrix by 90 degrees

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

n = len(matrix)

def transpose(matrix):
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

def reverse(matrix):
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n-j-1], matrix[i][j]

    return matrix

transposedMatrix = transpose(matrix)
print(transposedMatrix)
print(reverse(transposedMatrix))