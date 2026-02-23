# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n: int) -> str:
    return ''.join([f'{x} sheep... ' for x in range(1, n + 1)])

print(count_sheep(10))
