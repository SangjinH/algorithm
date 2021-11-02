import sys
input = sys.stdin.readline

# 연속적인 온도의 합이 제일 큰 값

N, K = map(int, input().split())
nums = list(map(int, input().split()))
stack_sum = [0]
for i in nums:
    stack_sum.append(stack_sum[-1] + i)

# print(stack_sum)
maxi = stack_sum[K]
for i in range(len(stack_sum)-K):
    temp = stack_sum[i+K] - stack_sum[i]
    # print(temp)
    if temp > maxi:
        maxi = temp

print(maxi)

