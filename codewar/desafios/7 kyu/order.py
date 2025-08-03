def descending_order(num):
    number_str = list(str(num))
    number_str.sort(reverse=True)
    return int(''.join(number_str))
    
    

print(descending_order(1010))