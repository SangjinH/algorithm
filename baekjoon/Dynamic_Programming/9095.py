# 백준 9095, DP 1,2,3 더하기
import sys
from math import factorial

input = sys.stdin.readline



def count(n):

    result = 0

    mock_3 = n//3
    for i in range(mock_3+1):
        cnt_3 = i
        num3 = n - (i*3)
        # print(num3)

        mock_2 = num3//2

        for j in range(mock_2+1):
            num2 = num3
            cnt_2 = j
            num2 = num2 - j*2
            # print(num2)

            cnt_1 = num2

            cnt = cnt_3 + cnt_2 + cnt_1

            result += int(factorial(cnt)/(factorial(cnt_1)*factorial(cnt_2)*factorial(cnt_3)))

    return result


case_num = int(input().rstrip())
nums = []

for _ in range(case_num):
    nums.append(int(input().rstrip()))

for i in nums:
    print(count(i))