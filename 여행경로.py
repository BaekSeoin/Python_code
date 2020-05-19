def dfs(cur):
    global answer, tickets_dict, visit, length, stop

    if len(answer) == length:
        stop = True
        return

    try:
        for index,nextPos in enumerate(tickets_dict[cur]):
            if visit[cur][index] == 0:
                visit[cur][index] = 1
                answer.append(nextPos)
                dfs(nextPos)
                if stop:
                    return
                visit[cur][index] = 0
                answer.pop()
    except:
        return


def solution(tickets):
    global answer, tickets_dict, visit, length, stop
    answer = []

    tickets_dict = dict()
    visit = dict()

    for i in tickets:
        try:
            tickets_dict[i[0]].append(i[1])
            tickets_dict[i[0]] = sorted(tickets_dict[i[0]])
            visit[i[0]].append(0)
        except:
            tickets_dict[i[0]] = []
            visit[i[0]] = []
            tickets_dict[i[0]].append(i[1])
            visit[i[0]].append(0)


    cur = "ICN"
    answer.append(cur)
    length = len(tickets) + 1
    stop = False
    dfs(cur)
    return answer

tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
print(solution(tickets))