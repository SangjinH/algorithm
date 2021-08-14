

def solution(servers, sticky, requests):
    # 각각의 서버를 만들어놓고
    answer = [[] for _ in range(servers)]

    if sticky:
        answer[0].append(requests[0])

        before = requests[0]
        idx = 1
        requests = requests[1:]
        for i in range(len(requests)):
            for j in range(len(answer)):
                flag = False
                if requests[i] in answer[j]:
                    answer[j].append(requests[i])
                    flag = True
                    break
            if not flag:
                answer[idx].append(requests[i])
                idx += 1
                idx %= len(answer)

    # sticky가 false면 공정하게 분배
    else:
        for i in range(len(requests)):
            answer[i % (servers)].append(requests[i])

    return answer



print(solution(2, True, [1,2,2,3,4,1]))