import sys
input = sys.stdin.readline
from collections import defaultdict, deque

"""
P는 수열 0 ~ N-1 까지
B[P[i]] = A[i]


P = [2, 3, 1]
B[2] = A[0]
B[3] = A[1]
B[1] = A[2]

A가 주어졌을때, P를 적용한 결과가 오름차순인 수열은 ?
여러개일 수 있다.
"""

N = int(input())
A = list(map(int, input().split()))

arr = defaultdict(deque)
B = sorted(A)

for i in range(len(B)):
    arr[B[i]].append(i)

for i in range(len(A)):
    print(arr[A[i]].popleft(), end=" ")






