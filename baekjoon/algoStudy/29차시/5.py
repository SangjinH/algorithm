import sys
input = sys.stdin.readline

"""
두 개의 연속된 부분 수열 중 
합이 T 가 되는 수열의 갯수 찾기

"""


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for i in range(1, len(A)):
    A[i] += A[i-1]

for i in range(1, len(B)):
    B[i] += B[i-1]


print(A)
print(B)