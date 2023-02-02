

def coinChangeSolution(denominations, total):
    denominations = sorted(denominations, reverse = True)

    sum = 0

    for i in denominations:
        while sum + i <= total:
            print(i, end = "  ")
            sum += i
        if sum >= total:
            break


denominations = [1, 2, 5, 10, 20, 50, 100, 1000]

coinChangeSolution(denominations, 201)