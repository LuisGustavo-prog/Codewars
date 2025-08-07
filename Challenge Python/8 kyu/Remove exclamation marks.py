def remove_exclamation_marks(s):
    s_ = list(s)
    result = []

    for x in s_:
        if x != '!':
            result.append(x)
    
    return ' '.join(result)

print(remove_exclamation_marks('Hello World!'))