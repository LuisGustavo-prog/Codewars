def no_space(x):
    x_ = list(x)
    result = []

    for i in x_:
        if i != ' ':
            result.append(i)
    
    return ''.join(result)


print(no_space('o i'))