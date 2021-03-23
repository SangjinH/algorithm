from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):

        if not prerequisites:
            return True

        def dfs(routes, start):

            routes += [start]
            if len(routes) > numCourses:
                return

            for i in route_dic[start]:
                dfs(routes, i)

            if len(routes) <= numCourses:
                result.append(routes[:])
                return

        route_dic = defaultdict(list)

        for i in range(len(prerequisites)):
            route_dic[prerequisites[i][0]].append(prerequisites[i][1])

        result = []

        for course in prerequisites:
            dfs([], course[0])

        print(result)
        if result:
            return True
        else:
            return False

s = Solution()
print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))