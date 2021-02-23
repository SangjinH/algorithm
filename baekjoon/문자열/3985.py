import sys
input = sys.stdin.readline

L = int(input())
roll = [0] * L
respect_N = []
N = int(input())
actual = [0] * (N+1)
for i in range(1, N+1):
    P, K = list(map(int, input().split()))

    respect_N.append(K-P+1)

    for j in range(P-1, K):
        if roll[j] == 0:
            roll[j] = i
            actual[i] += 1

for i in range(len(respect_N)):
    if respect_N[i] == max(respect_N):
        print(i+1)
        break

print(actual.index(max(actual)))
