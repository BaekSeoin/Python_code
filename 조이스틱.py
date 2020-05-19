from collections import deque


def bfs(List, name):
    global length, alpha

    visit = dict()
    visit[List[0][0]] = True


    while List:
        cur = List.popleft()
        curName = cur[0]

        curPointer = cur[1]
        curAlphabet = cur[2]

        prevDir = cur[3]
        count = cur[4]

        if curName == name:
            return count

        if curName[curPointer] != name[curPointer]:
            if curAlphabet + 1 == 26:
                nextAlphabet = 0
            else:
                nextAlphabet = curAlphabet + 1
            nextName = curName[:curPointer] + alpha[nextAlphabet] + curName[curPointer + 1:]

            try:
                x = visit[nextName]
            except:

                List.append((nextName, curPointer, nextAlphabet, 0, count + 1))
                #print(count+1,nextName, curName)
                visit[nextName] = True

            if curAlphabet - 1 == -1:
                nextAlphabet = 25
            else:
                nextAlphabet = curAlphabet - 1
            nextName = curName[:curPointer] + alpha[nextAlphabet] + curName[curPointer + 1:]
            try:
                x = visit[nextName]
            except:
                List.append((nextName, curPointer, nextAlphabet, 0, count + 1))
                visit[nextName] = True
                #print(count+1, nextName, curName)

        else:
            for i in range(2):
                if i == 1:
                    if prevDir == 2:
                        continue
                    if curPointer - 1 == -1:
                        nextPointer = length - 1
                    else:
                        nextPointer = curPointer - 1

                    word = curName[nextPointer]
                    nextAlphabet = alpha.index(word)
                    List.append((curName, nextPointer, nextAlphabet, 1, count + 1))
                else:
                    if prevDir == 1:
                        continue
                    if curPointer + 1 == length:
                        nextPointer = 0
                    else:
                        nextPointer = curPointer + 1
                    word = curName[nextPointer]
                    nextAlphabet = alpha.index(word)
                    List.append((curName, nextPointer, nextAlphabet, 2, count + 1))


def solution(name):
    global length, alpha

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(name)


    initial = 'A' * length

    List = deque()
    List.append((initial, 0, 0, 0, 0))

    answer = bfs(List, name)

    return answer

print(solution('AAA'))