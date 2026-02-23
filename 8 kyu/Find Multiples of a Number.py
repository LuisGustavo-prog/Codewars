# def find_multiples(integer, limit):
#     lis = []
    
#     for x in range(integer, limit + 1, integer):
#         lis.append(x)
    
#     return lis

def find_multiples(integer, limit):
    return [x for x in range(integer, limit + 1, integer)]

print(find_multiples(5, 25))
