

def numFactorMemo(n, memo):
    if n in [0, 1, 2]:
        return 1
    elif n == 3:
        return 2
    else:
        if n not in memo:
            memo[n] = numFactorMemo(n-1, memo) + numFactorMemo(n-3, memo) + numFactorMemo(n-4, memo)
        return memo[n]

print(numFactorMemo(5,{}))