

def fibonacciTabulation(n):
    table = [0,1]

    for i in range(2,n):
        table.append(table[i-1] + table[i-2])
    return table[n-1]

print(fibonacciTabulation(5))