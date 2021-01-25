# https://programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque

def solution(progresses, speeds):
    ans = []
    p = deque(progresses)
    s = deque(speeds)

    while True:
        if len(p) == 0:
            break

        for i in range(len(p)):
            p[i] += s[i]

        cnt = 0
        while True:
            if len(p) == 0:
                break

            if p[0] >= 100:
                p.popleft()
                s.popleft()
                cnt += 1
            else:
                break

        if cnt != 0:
            ans.append(cnt)
    return ans





progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))