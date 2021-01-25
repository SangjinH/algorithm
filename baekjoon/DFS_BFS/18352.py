# from collections import deque
# import sys
#
# def bfs(graph, start):
#     queue = deque()
#     queue.append(start-1)
#     visited[start-1] = 1
#     distance[start-1] = 0
#
#     while queue:
#         vertex = queue.popleft()
#         for nv in graph[vertex]:
#             if visited[nv-1] == 0:
#                 queue.append(nv-1)
#                 visited[nv-1] = 1
#                 distance[nv-1] = distance[vertex]+1
#
#
#
# n, m, k, x = map(int, input().split())
# graph = [] * n
# visited = [0] * n
#
# for _ in range(m):
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     graph[start-1].append(end)
#
# bfs(graph, x)
#
# for i in range(n):
#     if(distance[i]==k):
#         print(i+1)
#
# if k not in distance:
#     print(-1)
#
# # 입력예제
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
#
# # 결과
# # 4



#---------------------------------------- 해설
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정


# 너비 우선 탐색(BFS) 수행
q = deque([x])
print(q)
while q:
    now = q.popleft()
    print(now)
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        print(graph[now])
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)