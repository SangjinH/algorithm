# https://www.acmicpc.net/problem/21317  DFS로 풀어보기
import sys
input = sys.stdin.readline

result = int(1e9)


def dfs(location, jumped, energy):
    global result

    if location == n:
        result = min(result, energy)
        return
    elif location > n:
        return

    # 아직 도착하지 않았다면
    else:
        # 큰 점프를 하지 않았다면
        if not jumped:
            jumped = True
            energy += k
            dfs(location+3, jumped, energy)
            jumped = False
            energy -= k

        energy += rocks[location-1][1]
        dfs(location+2, jumped, energy)
        energy -= rocks[location-1][1]

        energy += rocks[location-1][0]
        dfs(location+1, jumped, energy)
        energy -= rocks[location-1][0]


n = int(input())
rocks = []

for _ in range(n-1):
    rocks.append(list(map(int, input().split())))

k = int(input())

dfs(1, False, 0)
print(result)