"""
트럭의 길이는 1 이고,
다리의 길이 만큼 올라갈 수 있음
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):

    bridge = deque([])
    waiting_trucks = deque(truck_weights)
    # print(len(waiting_trucks))

    finish = []

    sec = 0
    bridge_weight = 0
    # 아직 모든 트럭이 통과하지 않았다면,
    while len(finish) != len(truck_weights):
        # print(finish)
        # 1초가 지난 상황을 연출.
        sec += 1

        # 모든 차량을 한 칸씩 이동
        for i in range(len(bridge)):
            bridge[i][0] += 1

        # print("bridge : ", bridge)
        # 다리의 길이보다 더 많이 갔다면 탈출
        if len(bridge):
            if bridge[0][0] > bridge_length:
                out = bridge.popleft()
                finish.append(out)
                bridge_weight -= out[1]

        # print("waiting truck :  ",waiting_trucks)
        # print("bridge_weight : ", bridge_weight)
        # 들어간 상황에 무게도 괜찮고 길이도 괜찮다면
        if waiting_trucks:
            if bridge_weight + waiting_trucks[0] <= weight and len(bridge) < bridge_length:
                bridge_weight += waiting_trucks.popleft()
                bridge.append([1, bridge_weight])

    return sec


# bridge_length = 2
# weight = 10
# truck_weight = [7, 4, 5, 6]

bridge_length = 100
weight = 100
truck_weight = [10]


print(solution(bridge_length, weight, truck_weight))