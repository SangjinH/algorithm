"""
디스크 컨트롤러

"""

import heapq


# def solution(jobs):
#     cnt = 0
#     total = 0
#
#     while jobs:
#         heapq.heapify(jobs)
#         task = heapq.heappop(jobs)
#         cnt += 1
#         total += task[1]
#
#         for i in jobs:
#             if i[0] < task[0]+task[1]:
#                 i[1] += task[0]+task[1] - i[0]
#
#     print(total)
    # answer = 0
    # return answer


# print(solution(jobs=[[0, 3], [1, 9], [2, 6]]))


a = [[0, 4], [0, 2], [1, 4], [1, 2]]
heapq.heapify(a)
print(a)