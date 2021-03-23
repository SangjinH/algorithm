from collections import defaultdict


def findItinerary(tickets):

    def dfs(routes, start, cnt_list):
        if len(routes) == len(tickets) + 1:
            if cnt_list == check:
                result.append(routes[:])

            return

        for i in graph[start]:
            routes += [i]

            dfs(routes, i, cnt_list)
            routes.pop()

        return

    graph = defaultdict(list)
    check = [0] * len(graph)
    key_list = sorted(list(graph.keys()))

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        check[key_list.index(ticket[1])] += 1

    print(check)
    result = []

findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
)