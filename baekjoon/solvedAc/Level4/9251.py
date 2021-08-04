import sys
input = sys.stdin.readline

# 최장부분 공통수열
# 모두의 부분 수열 중 가장 긴 것을 찾는 문제

# ACAYKP
# CAPCAK

# 최장부분수열 = ACAK

first = list(input().rstrip())
second = list(input().rstrip())

# print(first)
# print(second)

# 해결 방법
# 각자리의 원소마다 가장 최근에 나온 숫자를 기입

# 두 문자열의 순서에 영향을 받는가 ?
# [ [1, 4], [0, 3], [1, 4], [], [5], [2] ]

# 1 3 4 5
# A C A K

# 두 번째 문자열이 첫 번째 온다면 ?
# [ [1], [0, 2], [5], [1], [0, 2], [4] ]

# 0 1 2 4
# A C A K

# 결국은 같은 값이 나온다.

# 각각의 위치 정보를 저장할 locations 변수를 둔다.
# locations = [[] for _ in range(len(first))]
#
# for i in range(len(first)):
#     for j in range(len(second)):
#         if first[i] == second[j]:
#             locations[i].append(j)
#
# print(locations)


# 인 줄 알았으나 찾아보니 DP 문제 ..
# DP 라는 느낌은 왔으나 어떻게 설계해야할지 모르겠어서 넘겼지만 ,,

dp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

for i in range(len(first)):
    for j in range(len(second)):
        # 끝 글자가 일치한다면
        if first[i] == second[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[-1][-1])