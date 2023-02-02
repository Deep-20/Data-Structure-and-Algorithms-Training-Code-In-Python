

def lcs(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0
    elif string1[0] == string2[0]:
        return 1 + lcs(string1[1:], string2[1:])
    else:
        return max(lcs(string1[1:], string2),
                  lcs(string1, string2[1:]))

print(lcs("elephant", "ddd"))