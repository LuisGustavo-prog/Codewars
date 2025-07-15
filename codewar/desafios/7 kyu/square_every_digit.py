def square_digits(num):
    number = [num]
    number_ = []
    for nu in number:
        megatron = nu ** 2
        number_.append(megatron)

    return number_


print(square_digits(9))