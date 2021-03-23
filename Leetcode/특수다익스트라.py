import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        INF = int(1e9)

        def dijkstra(start):
            q = []
            distance = [INF] * (n)
            translate = [0] * n
            # distance, 출발점, 거쳐간 거점수
            heapq.heappush(q, (0, start, -1))
            distance[start] = 0
            ans = INF

            while q:
                dist, now, trans = heapq.heappop(q)
                if distance[now] < dist:
                    continue

                for i in graph[now]:
                    cost = dist + i[1]
                    trans += 1

                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        translate[i[0]] = trans

                        if i[0] == dst and trans == K:
                            if cost < ans:
                                ans = cost

                        heapq.heappush(q, (cost, i[0], trans))
            return ans

        graph = [[] for _ in range(n)]

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        if dijkstra(src) != INF:
            return dijkstra(src)
        else:
            return -1

s =