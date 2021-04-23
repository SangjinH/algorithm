def dfs(start, ans):
    global answer
    # 방문처리
    ans += 1
    visited[start] = True

    if answer < ans:
        answer = ans

    for i in graph[start]:
        if not visited[i]:
            dfs(i, ans)
    visited[start] = False


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    answer = 0

    for _ in range(M):
        S, E = list(map(int, input().split()))
        graph[S].append(E)
        graph[E].append(S)

    for i in range(1, N+1):
        visited = [False] * (N+1)
        dfs(i, 0)

    print(f'#{tc} {answer}')