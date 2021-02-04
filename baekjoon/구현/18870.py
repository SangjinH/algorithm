# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
# print(num_list)

set_list = sorted(list(set(num_list)))
# print(set_list)

d = {}
for i in range(len(set_list)):
    d[set_list[i]] = i
for i in num_list:
    print(d[i], end=' ')
