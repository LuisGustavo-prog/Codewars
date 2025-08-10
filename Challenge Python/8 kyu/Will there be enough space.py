def enough(cap, on, wait):
    number_passager = abs(on + wait)
     
    if cap >= number_passager:
        return 0
    else:
        return abs(cap - number_passager)