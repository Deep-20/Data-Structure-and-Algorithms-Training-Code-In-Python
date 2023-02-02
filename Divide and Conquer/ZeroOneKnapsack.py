

def zeroOneKnapsackProblem(items, capacity):
    if len(items) == 1:
        if capacity - items[0][0] >= 0:
            return items[0][1]
        return 0

    if capacity - items[0][0] >= 0:
        one = items[0][1] + zeroOneKnapsackProblem(items[1:], capacity - items[0][0])
        two = zeroOneKnapsackProblem(items[1:], capacity)
        return max(one, two)
    return 0


print(zeroOneKnapsackProblem([[3, 31],
                        [1, 26],
                        [2, 17],
                        [5,72]], 7))
