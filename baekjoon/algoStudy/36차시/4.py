import sys
input = sys.stdin.readline

from collections import Counter, defaultdict, deque

count = defaultdict(int)

N = int(input())
nums = deque(map(int, input().split()))

result = [-1] * len(nums)

for i in nums:
    count[i] += 1

while nums:
    flag = False
    now = nums.popleft()
    standard = count[now]
    for i in nums:
        if count[i] > standard:
            flag = i
            break

    if flag:
        print(i, end=" ")
    else:
        print(-1, end=" ")