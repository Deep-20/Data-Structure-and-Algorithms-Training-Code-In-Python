

def houseRobberMemo(money, currentHouse, memo):
    if currentHouse > len(money) - 1:
        return 0
    else:
        if currentHouse not in memo:
            memo[currentHouse] = max(money[currentHouse] + houseRobberMemo(money, currentHouse + 2, memo),
                                     houseRobberMemo(money, currentHouse + 1, memo))
        return memo[currentHouse]

print(houseRobberMemo([6, 7, 1, 30, 8, 2, 4], 0, {}))