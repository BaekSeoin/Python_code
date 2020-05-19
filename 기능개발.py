def solution(number, k):
    global answer

    answer = ''

    k = len(number) - k
    count = k

    for i in range(k):
        a = number[:len(number)-count+1]
        Max = max(a)
        MaxIndex = number.index(Max)
        answer += str(Max)
        count -= 1
        number = number[MaxIndex + 1:]

    return answer

number = '4177252841'
k = 4

print(solution(number, k))