


def fractionalKnapsackSolution(item, knapsackWeight):
    for i in range(len(item)):
        density = item[i][1]/ item[i][0]
        item[i].append(density)

    item.sort(key = lambda x : x[2], reverse = True)

    # print(item)
    sum = 0
    value = 0

    for i in item:
        if sum + i[0] <= knapsackWeight:
            sum += i[0]
            value += i[1]
            # print(i[0], end = " ")
        else:
            difference = knapsackWeight - sum
            value += i[2] * difference
        
        if sum == knapsackWeight:
            break

    return value


items = [[30, 120],
        [20, 100],
        [10, 60]
        ]

print(fractionalKnapsackSolution(items, 50))