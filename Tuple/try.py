myTuple = (1,2,3,[4,5])

# myTuple[3] = myTuple[3].append(4)                   Error
# print(myTuple)

# myTuple[4] = 1                                      Error
# print(myTuple)

# myTuple = (3,4,5)                                   Entire tuple can be reassigned
# print(myTuple)

# del myTuple[2]                                      Error
# print(myTuple)

# del myTuple                                         Entire tuple can be deleted

init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)