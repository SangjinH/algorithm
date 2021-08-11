import sys
input = sys.stdin.readline

"""
중앙에 있던 발이 움직일 때, 2의 힘을 사용
다른 지점에서 인접한 지점으로 움직이면 3, 왼 -> 위, 아래
완전 반대편은 4
같은 것을 누른다면 1
"""


sequence = list(map(int, input().split()))
print(sequence)

locations = {
    '1': [-1, 0],
    '2': [0, -1],
    '3': [1, 0],
    '4': [0, 1]
}

costs = {
    '0': 1, # 움직임이 없을때,
    '11': 3, # 가로 1, 세로 1
    '2': 4, # 가로 2
    '20': 4, # 세로 2
}

pointer_1 = [0, 0]
pointer_2 = [0, 0]

pointers = [pointer_1, pointer_2]

ddr = [[0] * 3 for _ in range(3)]

# 처음 두 발 위치
ddr[1][1] = 2


for i in sequence:
    if i == 0:
        break

    # for p in range(len(pointers)):
