# https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

white = 0
blue = 0

def cut(x, y , n):
    global white, blue
    standard = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if standard != arr[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    if standard == 0:
        white += 1
        return

    else:
        blue += 1
        return

cut(0, 0, n)
print(white)
print(blue)