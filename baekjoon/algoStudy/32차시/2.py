import sys
input = sys.stdin.readline

"""
1 , 3, 4 개

상근이가 먼저시작, 창영이가 후공
"""

"""
1개라면 후
2개라면 선
3개라면 후
4개라면 선

5개라면 
상근이가 1개를 두면 상근이 이김
상근이가 3개를 두면 창영이 이김
상근이가 4개를 두면 상근이 이김
5개라면 1 + 4 
6개라면 4 1 1 상근
7개라면  4 3
        3 4
        1 4 1 1
8개라면  3 

"""

n = int(input())

dp = [0] * (n+5)
dp[2] = 1
dp[4] = 1

for i in range(5, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n]:
    print("SK")
else:
    print("CY")




