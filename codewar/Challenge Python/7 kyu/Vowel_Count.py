def get_count(sentence):
    count = 0
    list_sentence = ['a', 'e', 'i', 'o', 'u']
    for char in sentence.lower():
        if char in list_sentence:
            count += 1
    return count

print(get_count('abaa'))