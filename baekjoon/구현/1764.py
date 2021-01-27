# https://www.acmicpc.net/problem/1764
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# members = [input().strip()]
# result = []
# for _ in range(n+m-1):
#     data = input().strip()
#     if data in members:
#         result.append(data)
#     else:
#         members.append(data)
#
# print(len(result))
# for i in sorted(result):
#     print(i)

members = []
result = []
for _ in range(n+m):
    members.append(input().strip())
members.sort()
cnt = 0
for i in range(len(members)-1):
    if members[i] == members[i+1]:
        result.append(members[i])
        cnt += 1
print(cnt)
for i in result:
    print(i)