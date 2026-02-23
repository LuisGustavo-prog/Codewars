# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false

def solution(text: str, ending: str) -> bool:
    return True if ending == text[-len(ending):] else False

print(solution(text='samurai', ending='ai'))
