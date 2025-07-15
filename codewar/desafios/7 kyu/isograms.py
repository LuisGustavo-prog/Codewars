def is_isogram(string):
    string_lower = string.lower()
    
    for st in string_lower:
        if string_lower.count(st) >= 2:
            return False
    return True


print(is_isogram('Dermatoglyphics'))