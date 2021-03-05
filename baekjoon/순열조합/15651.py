import sys
input = sys.stdin.readline


def dupl(arr, cnt):

    if cnt == M:
        print(*arr)
        return

    for i in range(len(num_list)):
        arr.append(num_list[i])
        cnt += 1
        dupl(arr, cnt)
        arr.pop()
        cnt -= 1


N, M = list(map(int, input().split()))
num_list = list(range(1, N+1))
dupl([], 0)