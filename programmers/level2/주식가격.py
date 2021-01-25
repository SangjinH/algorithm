# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        bigyo = q.popleft()

        cnt = 0
        for i in q:
            cnt += 1
            if bigyo > i:
                break
            if bigyo <= i:
                continue
        answer.append(cnt)
    return answer





prices = [2, 2, 1, 3, 10, 1]
print(solution(prices))