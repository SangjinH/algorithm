# https://www.acmicpc.net/problem/1966
# 백준 1966번, 구현
import sys
input = sys.stdin.readline

cases = []
n = int(input().rstrip())

for i in range(n):
    jungyo = list(map(int, input().rstrip().split()))
    num = int(input().rstrip().split())
    