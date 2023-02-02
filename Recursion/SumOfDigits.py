def sumOfDigits(n):
    assert n > 0 and type(n) == int, "Invalid Input"
    if n < 10:
        return n
    else:
        return n%10 + sumOfDigits(int(n/10))

print(sumOfDigits(220578))