def reverse_seq(n):
    n_ = [int(n)]
    number = 0 
    
    for x in range(1, n_[-1] + 1):
        if x == n_:
            number += 1

    return number

print(reverse_seq('123456'))