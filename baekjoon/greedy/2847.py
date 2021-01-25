# https://www.acmicpc.net/problem/2847
# 백준,  게임을 만든 동준이
import sys
input = sys.stdin.readline

n = int(input())
score_list = []
for _ in range(n):
    score_list.append(int(input()))

score_list.reverse()

ans = 0
for i in range(n-1):
    if score_list[i] < score_list[i+1]:
        dif = abs(score_list[i+1] - score_list[i])+1
        score_list[i+1] -= dif
        ans += dif

print(score_list)