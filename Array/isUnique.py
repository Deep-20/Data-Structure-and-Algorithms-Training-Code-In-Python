# CHeck if all elements in list are unique

numbers = [2,67,5,1,6,8,12,67,44]

set1 = set(numbers)

if len(numbers) == len(set1):
    print("True")
else:
    print("False")