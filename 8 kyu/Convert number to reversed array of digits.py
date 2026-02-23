# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]

def digitize(n: int) -> list:
    return [int(x) for x in list(str(n))[::-1]]

print(digitize(123456))
