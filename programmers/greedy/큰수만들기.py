# k개의 수를 제거했을때, 얻을 수 있는 가장 큰 숫자
# k개를 제거할때, 가장 먼저 작은 원소를 제거
# 가장 작은 원소를 제거하는것이 최고.
# 다음 원소가 더 큰 원소가 나왔을때
from collections import deque


def solution(number, k):
    number = list(map(int, list(number)))

    cnt = 0

    q = deque([])
    for i in number:
        if not q or cnt == k:
            q.append(i)

        else:
            while q:

                if q[-1] < i:
                    q.pop()
                    cnt += 1
                    if cnt == k:
                        break
                else:
                    break
            q.append(i)

    if cnt == k:
        return "".join(map(str, q))
    else:
        return "".join(list(map(str, q))[:cnt - k])