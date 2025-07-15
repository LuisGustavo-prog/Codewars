import math
def century(year):
    century = year / 100
    
    if isinstance(century, float):
        return math.ceil(century)
    else:
        return century

print(century(1900))