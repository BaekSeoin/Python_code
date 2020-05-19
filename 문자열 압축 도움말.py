def solution(s):
    answer = len(s)

    for press in range(1, len(s) // 2 + 1):
        final = ''
        idx = 1
        for i in range(0, len(s), press):
            word = s[i:i + press]
            try:
                nextWord = s[i + press: i + press + press]
                if word == nextWord:
                    idx += 1
                else:
                    if idx != 1:
                        final += str(idx)
                    final += word
                    idx = 1
            except:
                if idx != 1:
                    final += str(idx)
                final += word
        answer = min(answer, len(final))

    return answer

s = "aabbaccc"
print(solution(s))