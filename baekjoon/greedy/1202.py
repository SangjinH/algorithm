# https://www.acmicpc.net/problem/1202
# 보석도둑

# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
#
# treasure_info = []
# for _ in range(n):
#     m, v = map(int, input().split())
#     treasure_info.append((m, v))
#
# bag_info = []
# for _ in range(k):
#     bag_info.append(int(input()))


# results = []
# for i in bag_info:
#     avail = 0
#     for j in treasure_info:
#         if j[0] <= i:
#             avail = max(avail, j[1])
#
#     results.append(avail)
#     # print(results)
#
#     for k in range(len(treasure_info)):
#         if treasure_info[k][1] == avail:
#             del treasure_info[k]
#             break
#
# print(sum(results))

# treasure_info.sort()
# bag_info.sort()
#
# # status = [False] * len(treasure_info)
# result = []
# for i in bag_info:
#     find_max = []
#     for j in treasure_info:
#         if j[0] > i:
#             break
#         else:
#             find_max.append(j[1])
#     result.append(max(find_max))
#
#     for i in treasure_info:
#         if i[1] == max(find_max):
#             treasure_info.remove(i)
#             break
# print(sum(result))

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

treasure_info = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(treasure_info, (m, v))

bag_info = []
for _ in range(k):
    bag_info.append(int(input()))

bag_info.sort()

c = 0
p = []
for i in bag_info:

    while treasure_info and i >= treasure_info[0][0]:
        m, v = heapq.heappop(treasure_info)
        heapq.heappush(p, -v)

    if p:
        c -= heapq.heappop(p)
    elif not treasure_info:
        break
print(c)