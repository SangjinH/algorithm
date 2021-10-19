import pprint
import sys
input = sys.stdin.readline

char_1 = [0] + list(input().rstrip())
char_2 = [0] + list(input().rstrip())

# print(char_1, char_2)

dp = [[0]*(len(char_1)) for _ in range(len(char_2))]

for i in range(1, len(char_2)):
    for j in range(1, len(char_1)):
        temp = 0
        if char_2[i] == char_1[j]:
            # print("match")
            temp = dp[i-1][j-1] + 1

        if temp:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], temp)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

x = len(char_2)-1
y = len(char_1)-1

check = dp[-1][-1]
answer = []
while x > 0 and y > 0:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        answer.append(char_1[y])
        x -= 1
        y -= 1


print(dp[-1][-1])
print("".join(answer[::-1]))