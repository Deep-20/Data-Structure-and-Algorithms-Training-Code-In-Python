

def convertStringMemo(string1, string2, memo):

    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    elif string1 == string2:
        return 0
    else:
        if string2 not in memo:
            if string1[0] != string2[0]:
                memo[string2] = min(1 + convertStringMemo(string1, string2[1:], memo),                              # Delete
                                    1 + convertStringMemo(string1[1:], string2, memo),                              # Insert
                                    1 + convertStringMemo(string1[1:], string2[1:], memo))                          # Replace
            else:
                memo[string2] = convertStringMemo(string1[1:], string2[1:], memo)
                
        return memo[string2]


print(convertStringMemo("catch", "carch", {}))


