def power(x,n):
    assert type(n) == int, "Invalid Input!!"
    if n == 0:
        return 1
    elif n < 0:
        return (1/x) * power(x, n + 1)
    else:
        return x * power(x, n-1)


print(power(-2,-1))