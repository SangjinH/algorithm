import sys
input = sys.stdin.readline


n, m = map(int, input().split())

arr = [[], []]

for i in range(2):
    for _ in range(n):
        arr[i].append(list(map(int, input().rstrip())))


def same(arr1, arr2, n, m):
    for i in range(n):
        for j in range(m):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True


cnt = 0
flag = False
for i in range(n-2):
    for j in range(m-2):
        if arr[0][i][j] != arr[1][i][j]:
            for k in range(3):
                for l in range(3):
                    arr[0][i+k][j+l] = abs(arr[0][i+k][j+l]-1)

            cnt += 1

for i in range(n):
    for j in range(m):
        if arr[0][i][j] != arr[1][i][j]:
            flag = True
            break

if not flag:
    print(cnt)
else:
    print(-1)
