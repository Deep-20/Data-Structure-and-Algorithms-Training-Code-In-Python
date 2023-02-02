def decimalToBinary(n):
    assert type(n) == int, "Invalid Input!!"
    if n == 0:
        return 0
    else:
        return (decimalToBinary(int(n/2)) * 10) + (n%2)

print(decimalToBinary(-13))

