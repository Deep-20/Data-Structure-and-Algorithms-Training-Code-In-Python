def twoSum(numbers, sum):
    pair = []
    complement = []
    for i in numbers:
        if (sum - i) in complement:
            pair.extend([sum - i,i])
            return pair
        else:
            complement.append(i)

print(twoSum([2,6,3,9,11], 9))
