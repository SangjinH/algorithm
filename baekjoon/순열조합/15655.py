import sys
input = sys.stdin.readline

def combi(cnt, arr):

    if cnt == M:
        if sorted(arr) not in result:
            tmp = arr[:]
            result.append(tmp)
            for i in tmp:
                print(i, end=' ')
            print()

    for i in range(N):
        if not check[i]:
            arr.append(num_list[i])
            check[i] = True
            cnt += 1
            combi(cnt, arr)
            check[i] = False
            cnt -= 1
            arr.remove(num_list[i])
    return 


N, M = list(map(int, input().split()))
num_list = sorted(list(map(int, input().split())))
result = []
check = [False] * N
combi(0, [])
