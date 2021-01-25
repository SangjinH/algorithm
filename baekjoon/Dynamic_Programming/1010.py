# https://www.acmicpc.net/problem/1010
# 백준 1010, DP 다리놓기
import sys
input = sys.stdin.readline
from math import factorial

cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    result = factorial(b)/(factorial(a)*factorial(b-a))
    print(int(result))