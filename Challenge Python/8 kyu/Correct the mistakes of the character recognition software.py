def correct(s):
    lis = list(s)
    x = 0
    
    while x < len(lis):
        if lis[x] == '5':
            lis[x] = 'S'
        elif lis[x] == '0':
            lis[x] = 'O'
        elif lis[x] == '1':
            lis[x] = 'I'

        x += 1

    return ''.join(lis)

# Usando outro meio
def correct(s):
     return s.replace('1','I').replace('0','O').replace('5','S')