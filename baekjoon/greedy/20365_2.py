import sys
input = sys.stdin.readline

from collections import deque

# N 개를 칠해야하고,
# 최소한의 갯수로 칠하고 싶다.

N = int(input())
colors = list(map(str, input().rstrip()))


"""
한 번 생각을 해보자.

B
B
R
B
R
B
B
R

둘 중에 더 많은 색이 있는 것으로 칠하고, 나머지 갯수만큼 더해주면 끝 아닌가 ?

"""

# deque로 하나씩 꺼내면서 확인해서 더하기
def paint(colors):

    if len(colors) == 1:
        return 1

    color_cnt_map = {'B' : 0,
                     'R': 0}

    colors = deque(colors)

    before = colors.popleft()
    while colors:
        now = colors.popleft()

        if before != now:
            color_cnt_map[before] += 1
            before = now
    # 마지막 색 더해주기
    color_cnt_map[now] += 1

    return 1 + (min(color_cnt_map.values()))


print(paint(colors))