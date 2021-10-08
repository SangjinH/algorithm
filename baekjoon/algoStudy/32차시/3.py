import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))

print(nums)

if M == 1:
    print(sum(nums))

else:
