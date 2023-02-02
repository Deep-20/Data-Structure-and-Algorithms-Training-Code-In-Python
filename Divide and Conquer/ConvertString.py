

def converStringSolution(string1, string2):

    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    elif string1 == string2:
        return 0

    for i in range(len(string1)):
        if string1[i] == string2[i]:
            return converStringSolution(string1[i+1:], string2[i+1:])               # Same characters
        else:
            return min(1 + converStringSolution(string1[i+1:], string2[i+1:]), 
                        1 + converStringSolution(string1[i:], string2[i+1:]),
                            1 + converStringSolution(string1[i+1:], string2[i:]))           # Replace, Delete, Insert operation respectively

print(converStringSolution("table", "tbrltt"))