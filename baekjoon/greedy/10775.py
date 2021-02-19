import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

gates = [False] * G

cnt = 1
standard = int(input())

for _ in range(P-1):

    num = int(input())
    if standard < num:
        cnt += 1
        standard = num
        continue
    else:
        if cnt <= num:
            cnt += 1
            standard = num
        else:
            break

print(cnt)