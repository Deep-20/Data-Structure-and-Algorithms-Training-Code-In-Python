

def houseRobberTabulation(money):
    # tb = [0, 0]
    tb = [0] * (len(money) + 2)

    for i in range(len(money)-1, -1, -1):
        # tb.insert(0, max(money[i] + tb[1], tb[0]))
        tb[i] = max(money[i] + tb[i+2], tb[i+1])

    return tb[0]


print(houseRobberTabulation([6, 7, 1, 30, 8, 2, 4]))