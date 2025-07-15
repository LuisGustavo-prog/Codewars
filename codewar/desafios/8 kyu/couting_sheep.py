def count_sheeps(sheep):
    if True in sheep:
        return sheep.count(True)
    else:
        return 0

print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))