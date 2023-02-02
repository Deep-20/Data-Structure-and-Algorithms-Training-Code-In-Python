


def lps(string1):
    if len(string1) == 0:
        return ''
    elif len(string1) == 1:
        return string1[0]

    if string1[0] == string1[-1]:
        return string1[0] + lps(string1[1:-1]) + string1[0]
    else:
        result1 = lps(string1[1:])
        result2 = lps(string1[:-1])
        if len(result1) > len(result2):
            return result1
        else:
            return result2

print(lps("AMEEWMEA"))