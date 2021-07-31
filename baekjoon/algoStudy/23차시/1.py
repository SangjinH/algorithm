import sys
input = sys.stdin.readline
from itertools import permutations
#
#
# total = list(permutations(list(range(1, 10)), 3))
#
# n = int(input())
#
# for _ in range(n):
#     temp, s, b = list(input().split())
#     s = int(s)
#     b = int(b)
#     temp = list(temp)
#     for i in range(3):
#         temp[i] = int(temp[i])
#
#     idx = 0
#     while idx < len(total):
#         check = total[idx]
#         # print('check', check)
#         # print('temp', temp)
#
#         s_cnt = 0
#         b_cnt = 0
#
#         for j in range(3):
#             if check[j] in temp:
#                 if check[j] == temp[j]:
#                     # print(111111111111111111)
#                     s_cnt += 1
#                 else:
#                     b_cnt += 1
#
#         if s_cnt == s and b_cnt == b:
#             idx += 1
#         else:
#             total.remove(total[idx])
#             # print(total)


# print(len(total))

nums = list(range(1, 10))

num_list = list(permutations(nums, 9))

for i in num_list:
    print(''.join(str(i)))
