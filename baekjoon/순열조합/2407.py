import sys
input = sys.stdin.readline
from math import factorial
N, M = list(map(int, input().split()))
print(factorial(N)//(factorial(M)*factorial(N-M)))