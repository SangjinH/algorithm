import sys
input = sys.stdin.readline


def sub_list(arr, cnt):
    if cnt == M:
        if arr not in result:
            for i in arr:
                print(i, end=' ')
            print()
            return

    for i in range(N):
        if not check[i]:
            arr.append(num_list[i])
            check[i] = True
            cnt += 1
            sub_list(arr, cnt)
            check[i] = False
            cnt -= 1
            arr.remove(num_list[i])


N, M = list(map(int, input().split()))
num_list = list(map(int, input().split()))
num_list.sort()

check = [False] * N
result = []
sub_list([], 0)
