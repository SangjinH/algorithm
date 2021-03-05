def select_sort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sizes = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x, y = i, j

                # 가로, 세로 길이 찾기
                while x<N and arr[x][j] != 0:
                    x += 1
                while y<N and arr[i][y] != 0:
                    y += 1

                # sorting시 필요한 넓이까지 추가
                sizes.append([x-i, y-j])

                # 초기화
                for a in range(i, x):
                    for b in range(j, y):
                        arr[a][b] = 0

    sizes.sort(key= lambda x: [x[0]*x[1], x[0]])

    print(f'#{tc} {len(sizes)}', end=' ')
    for i in sizes:
        for j in i:
            print(j, end=' ')
    print()
