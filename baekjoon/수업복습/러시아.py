T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    W = [0] * N
    B = [0] * N
    R = [0] * N

    # 각 행을 돌면서 바꿔야할 원소의 개수파악
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'W':
                W[i] += 1
            if arr[i][j] != 'B':
                B[i] += 1
            if arr[i][j] != 'R':
                R[i] += 1

    # 누적합 구하기
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]


    # 경계선을 이동하며 최소값 갱신
    W_cnt = 0
    B_cnt = 0
    R_cnt = 0
    mini = 987654321
    for i in range(N-2):
        for j in range(i+1, N-1):
            W_cnt = W[i]
            B_cnt = B[j] - B[i]
            R_cnt = R[N-1] - R[j]

            if mini > W_cnt + B_cnt + R_cnt:
                mini = W_cnt + B_cnt + R_cnt

    print(f'#{tc} {mini}')