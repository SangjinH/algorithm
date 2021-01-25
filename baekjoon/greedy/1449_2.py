import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
troubles = list(map(int, input().rstrip().split()))

tape = 0
cnt = 0

for i in troubles:
    if tape >= i+0.5:
        continue
    else:
        tape = i - 0.5
        while tape < i + 0.5:
            cnt += 1
            tape += l
print(cnt)