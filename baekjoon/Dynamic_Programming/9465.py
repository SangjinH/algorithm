# https://www.acmicpc.net/problem/9465
# 백준 9465번, 스티커
import sys
input = sys.stdin.readline

case_num = int(input())
for _ in range(case_num):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))

    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for j in range(2, len(arr[1])):
        arr[0][j] += max(arr[1][j-1], arr[1][j-2])
        arr[1][j] += max(arr[0][j-1], arr[0][j-2])

    print(max(arr[0][-1], arr[1][-1]))
#
# def dp(arr):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     for i in range(2):
#         for j in range(len(arr[1])):
#             for k in range(4):
#                 nx = i + dx[i]
#                 ny
