def get_sum(a,b):
    soma = 0

    if a > b:
        for number in range(b, a + 1):
            soma += number
        return soma
    elif b > a:
        for number in range (a, b + 1):
            soma += number
        return soma
    elif a == b:
        return a 

print(get_sum(10, 2))
