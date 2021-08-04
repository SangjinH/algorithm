import sys
input = sys.stdin.readline

sosu = [True for _ in range(4000001)]

for i in range(2, int((4000001**(1/2)))):
    if sosu[i]:
        for j in range(i+i, 4000001, i):
            sosu[j] = False

sosus = []
for i in range(2, len(sosu)):
    if sosu[i]:
        sosus.append(i)

# 부분합
partial_sum = [0] * (len(sosus)+1)

for i in range(1, len(sosus)):
    partial_sum[i] = partial_sum[i-1] + sosus[i-1]
# print(sosus)

# 투 포인터
ans = 0
start = 0
end = 1

target = int(input())


while start < len(sosus) and sosus[end-1] <= target:
    if partial_sum[end] - partial_sum[start] == target:
        # print("equal")
        ans += 1
        start += 1
    elif partial_sum[end] - partial_sum[start] > target:
        # print("big")
        start += 1
    else:
        # print("small")
        if end < len(sosus)-1:
            end += 1
        else:
            start += 1

print(ans)