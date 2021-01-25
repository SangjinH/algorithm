from collections import deque


def solution(priorities, location):
    results = []

    pri_list = deque([(p, i) for i, p in enumerate(priorities)])

    while pri_list:
        pri = pri_list.popleft()

        if len(pri_list) == 0:
            results.append(pri)
            break

        values = []
        for i in pri_list:
            values.append(i[0])

        if pri[0] >= max(values):
            results.append(pri)
        else:
            pri_list.append(pri)

    for i in range(len(results)):
        if results[i][1] == location:
            return i + 1
