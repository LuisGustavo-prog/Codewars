def filter_list(l):
    list_l = []

    for number in l:
        if isinstance(number, int):
            list_l.append(number)
        
    return list_l


print(filter_list([1,2,3,4,'a']))
