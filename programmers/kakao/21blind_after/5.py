"""
0 은 양
1 은 늑대

"""
from collections import deque



def solution(info, edges):
    answer = 0

    graph = [[] for _ in range(len(info))]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    # print(graph)
    print(info)
    checked = [False] * len(info)
    node_info = [[] for _ in range(len(info))]

    def dfs(curr, sheep, wolf):
        if sheep == wolf:
            return [sheep, wolf-1]

        for i in graph[curr]:
            # 양이라면
            if not checked[i]:
                if info[i] == 0:
                    checked[i] = True
                    node_info[i] = dfs(i, sheep+1, wolf)

                else:
                    checked[i] = True
                    node_info[i] = dfs(i, sheep, wolf + 1)

    dfs(0, 1, 0)
    print(node_info)

    return answer



print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
