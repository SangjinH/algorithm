"""
어떤 분류의 작업을 처리하기로 했다면 모두 끝마칠때까지 분류함
처리하는 도중이거나 처리가 끝나과 동시에 같은 분류의 작업이 새로 요청되면
                            새로운 작업도 이어서 처리
하나가 끝나면 다른분류 중 중요도 합이 높은 분류처리
여러개라면 분류번호가 낮은 순

처음들어온놈은 무조건 처리해야함
시간은 상관없으나 처리되는 순서가 중요
"""
from pprint import pprint

import heapq
from collections import deque, defaultdict

def solution(jobs):

    start_t = jobs[0][0]
    take_t = jobs[0][1]
    end_t = start_t + take_t
    sec_num = jobs[0][2]

    answer = [jobs[0][-2]]

    if len(jobs) == 1:
        return answer

    jobs = deque(jobs[1:])

    waiting = defaultdict(list)
    for i in range(start_t+1, 10000001):
        if not jobs:
            break

        if i <= end_t + 1 and jobs[0][2] == sec_num:
            end_t += jobs[1]

        else:
            if i <= jobs[0][0] < end_t:
                work = jobs.popleft()
                if work[2] not in waiting.keys():
                    waiting[work[2]].append([work[-1], work[1]])
                else:
                    print(waiting[work[2]])
                    waiting[work[2]][0][0] += work[-1]
                    waiting[work[2]][0][1] += work[1]

            else:




        print(waiting)




    return answer


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]))
print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))
print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]))
