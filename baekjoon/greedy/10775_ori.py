import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

gates = [False] * G
cnt = 0
for _ in range(P):
    num = int(input())

    exist = False
    for i in range(num-1 , -1, -1):
        if not gates[i]:
            gates[i] = True
            exist = True
            cnt += 1
            break

    if not exist:
        break

print(cnt)