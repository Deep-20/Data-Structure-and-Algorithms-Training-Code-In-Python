


def fibonacciMemo(n, memo):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n not in memo:
            memo[n] = fibonacciMemo(n-1, memo) + fibonacciMemo(n-2, memo)
        return memo[n]

print(fibonacciMemo(5,{}))