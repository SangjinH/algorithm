import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
point = int(input())

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if arr[i] == num:
            # 잘려야하는 노드라고 인식하기
            dfs(i, arr)

dfs(point, arr)

answer = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)