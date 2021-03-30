import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(N)]

check = ['W', 'B']

ans = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if arr[x][y] != check[(x + y)%2]:
                    cnt += 1

        tmp = min(cnt, 64-cnt)
        if tmp < ans:
            ans = tmp

print(ans)