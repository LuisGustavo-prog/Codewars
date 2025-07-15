def solution(text, ending):
    final = text[-len(ending):]

    return final == ending

print(solution("samurai", "ai"))