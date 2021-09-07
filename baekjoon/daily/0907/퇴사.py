import sys
input = sys.stdin.readline

# N+1 일째 퇴사

N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

P.append(0)


print(T)
print(P)

# for i in range(len(T)):
#