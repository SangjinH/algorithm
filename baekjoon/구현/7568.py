# https://www.acmicpc.net/problem/7568
# 백준 7568번, 구현 : 덩치
import sys
input = sys.stdin.readline

n = int(input().rstrip())

people_list = []
for _ in range(n):
    people_list.append(list(map(int, input().rstrip().split())))
#
# people_list = sorted(people_list,  key=lambda x: x[0], reverse=True)
#
#
# for i in range(n-1):
#     if people_list[i][1] > people_list[i+1][1]:
rank_list = []

for i in range(n):
    bigyo = people_list[i]
    cnt = 1
    for j in range(n):
        if bigyo[0] < people_list[j][0] and bigyo[1] < people_list[j][1]:
            cnt += 1
    rank_list.append(cnt)

for i in rank_list:
    print(i, end=' ')