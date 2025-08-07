def divisors(n):
    count = 0

    for number in range(1, n + 1):
        if n % number == 0:
            count += 1
    return count



print(divisors(4))
