from collections import deque

def solution(people, limit):
    people.sort()

    people = deque(people)
    count = 0

    POP = True

    while people:
        if POP:
            x = people.popleft()
        try:
            y = people.pop()
        except:
            count += 1
            break

        if x + y > limit:
            if y > (limit / 2):
                count += 1
            if x > (limit / 2):
                count += 1
                POP = True
            else:
                POP = False
        else:
            count += 1
            POP = True
    if POP == False:
        count += 1

    return count


people =[70, 80, 50]
limit = 100
print(solution(people, limit))