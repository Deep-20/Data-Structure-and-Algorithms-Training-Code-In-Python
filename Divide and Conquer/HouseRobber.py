

def houseRobberSolution(money):

    if len(money) == 0:
        return 0
    elif len(money) == 1:
        return money[0]
    elif len(money) == 2:
        return max(money[0], money[1])
    else:
        if money[0] > money[1]:
            return money[0] +  houseRobberSolution(money[2:])
        else:
            return money[1] + houseRobberSolution(money[3:])

print(houseRobberSolution([6, 7, 1, 30, 8, 2]))