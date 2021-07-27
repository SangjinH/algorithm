# 연속된 두 개의 수의 차이가 일정한 수열
# 양의 정수 x의 각 자리가 등차수열을 이룬다.
# 110
# 10 11 12 13 14 15 16 17 18 19

import sys
input = sys.stdin.readline

# 1부터 99까지는 모두 한수

n = int(input())
hs = 0

for i in range(1, n+1):
    if i <= 99:
        hs += 1

    else:
        nums = list(map(int, list(str(i))))

        d = nums[1] - nums[0]
        flag = True
        for j in range(1, len(nums)-1):
            if d != nums[j+1] - nums[j]:
                flag = False
                break

        if flag:
            hs += 1

print(hs)