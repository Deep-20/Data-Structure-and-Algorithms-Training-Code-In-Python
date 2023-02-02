

def numberFactorSolution(sum):
    if sum in [0, 1, 2]:
        return 1
    elif sum == 3:
        return 2
    else:
        subP1 = numberFactorSolution(sum - 1)
        subP2 = numberFactorSolution(sum - 3)
        subP3 = numberFactorSolution(sum - 4)
        return subP1 + subP2 + subP3


print(numberFactorSolution(4))

        
