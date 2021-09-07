import sys
input = sys.stdin.readline
from collections import deque

"""
세준이 위치 0
책도 전부 0에서 출발

책들의 원래위치가 주어지고, 한 칸 이동할때마다 걸음수 + 1
최소 걸음수는 ?
"""

N, M = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

answer = 0


def max_distance(arr):
    global answer

    for i in range(M, len(arr), M):
        answer += arr[i]*2

    answer += arr[0]
    return


def another_distance(arr):
    global answer

    for i in range(0, len(arr), M):
        answer += arr[i] * 2
    return


plus_arr = deque()
minus_arr = deque()

for loc in locations:
    if loc > 0:
        plus_arr.insert(0, loc)
    else:
        minus_arr.append(-loc)

# print(plus_arr)
# print(minus_arr)

if plus_arr and minus_arr:

    if plus_arr[0] > minus_arr[0]:
        max_distance(plus_arr)
        another_distance(minus_arr)
    else:
        another_distance(plus_arr)
        max_distance(minus_arr)

elif plus_arr:
    max_distance(plus_arr)

else:
    max_distance(minus_arr)


print(answer)