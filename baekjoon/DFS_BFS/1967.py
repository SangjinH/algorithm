import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

# 다익스트라 알고리즘 구현
def dijkstra(start):
    # 시작점의 거리를 0으로 초기화
    distance[start] = 0
    q = []
    # 우선순위 큐를 이용해서 처음 (거리, 시작점) 을 push
    heapq.heappush(q, (0, start))

    # 큐가 전부 다 빌 때까지
    while q:
        dist, now = heapq.heappop(q)

        # 꺼낸 길이가 만약 현재 길이보다 길다면 continue
        if dist > distance[now]:
            continue

        # 각각의 그래프에서 꺼낸 i 의 번호와 길이를 이용해서 새로 길이를 만들고
        for i in graph[now]:
            cost = dist + i[1]

            # 만약 만든 길이가 현재 길이보다 짧다면 갱신해준뒤 다시 Queue에 push
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = list(map(int, input().split()))
    graph[a].append((b, dist))
    graph[b].append((a, dist))


# 최대거기를 구하기위해선 총 두번의 거리구하기를 실행하면된다!!!
# 공식같은것.
# 총 두번의 Dijkstra를 실행해 처음한 것에서 최대길이가 나오는 인덱스를
#                     기준으로 다시한 번 실행한 후 그 거리의 최대값이 지름!!!
idx = 1
for i in range(2):
    distance = [INF] * (N+1)
    dijkstra(idx)
    idx = distance.index(max(distance[1:]))

print(max(distance[1:]))