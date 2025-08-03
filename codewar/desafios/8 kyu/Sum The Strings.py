def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0 
    return str(a + b)


print(sum_str(10, 11))