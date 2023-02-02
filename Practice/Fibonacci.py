def Fibonacci(n):
    assert n>=0 and type(n) == int,"Fibnaaci number cannot be negative or non integer"
    if n in [0,1]:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
        
print(Fibonacci(6))
