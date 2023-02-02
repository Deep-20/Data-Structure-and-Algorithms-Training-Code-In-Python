def factorial(n):
    if n >= 0 and type(n) == int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return "Invalid Input!!"

ans = factorial(5)
print(ans)