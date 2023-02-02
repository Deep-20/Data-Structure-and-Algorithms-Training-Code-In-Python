def gcd(a,b):
    assert type(a) == int and type(b) == int and a > 0 and b > 0, "Invalid Input"
    if a > b:
        if a%b == 0:
            return b
        else:
            return gcd(a % b, b)
    elif a < b:
        if b%a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        return a
    
print(gcd(48,18))
