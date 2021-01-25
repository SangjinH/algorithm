# https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    q = deque(people)
    while q:
        if q[0] + q[len(q) - 1] <= limit:
            if len(q) == 1:
                answer += 1
                break
            answer += 1
            q.popleft()
            q.pop()
        else:
            answer += 1
            q.popleft()
    return answer


people = [70, 80, 50]
limit = 100

print(solution(people, limit))
