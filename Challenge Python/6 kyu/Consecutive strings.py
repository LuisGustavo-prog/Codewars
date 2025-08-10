def longest_consec(strarr, k):
    lis = []

    for x in range(len(strarr) - k + 1):
        lis = strarr[x:x+k]  
        cont = ''.join(lis)

        return cont

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
