bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # print(truck_weights)
    # 미리 다리의 최대길이를 설정 해놓은 후
    on_bridge = [0] * bridge_length

    while len(on_bridge):
        answer += 1
        on_bridge.pop(0)

        # 아직 들어갈 트럭이 남아있다면
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return answer


print(solution(bridge_length, weight, truck_weights))
