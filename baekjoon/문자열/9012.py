# https://www.acmicpc.net/problem/9012
# 백준 9012, 문자열 , 괄호 세기
import sys
input = sys.stdin.readline

n = int(input().rstrip())

gaulho_list = []
for _ in range(n):
    gaulho_list.append(input().rstrip())

# print(gaulho_list)

for i in range(len(gaulho_list)):
    rights = 0
    lefts = 0
    for j in gaulho_list[i]:
        if j == '(':
            rights += 1
        elif j == ')':
            lefts += 1
        if lefts > rights:
            break

    if rights != lefts:
        print('NO')
    elif rights == lefts:
        print('YES')