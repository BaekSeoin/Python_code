import sys
sys.stdin = open('input.txt','r')

t
    while 1:
        test, index = tuple(map(str, sys.stdin.readline().rstrip().split()))
        text = [i for i in test]

        dir = {}

        for i in text:
            for j in text:
                if i != j:
                    if i not in dir:
                        dir[i] = [j]
                    else:
                        dir[i].append(j)
        final = []
        depth = len(text)


        def dfs(i, word):
            global depth
            current = i
            if len(word) == depth:
                final.append(word)
                return

            for j in dir[current]:
                if j not in word:
                    word = word + j
                    dfs(j, word)
                    word = word[:-1]


        for t in text:
            word = t
            dfs(t, word)

        final.sort()

        if len(final) >= int(index):
            print(test, index, '=', end=' ')
            print(final[int(index) - 1])
        else:
            print(test, index, '=', end=' ')
            print("No permutation")
except:
    exit()