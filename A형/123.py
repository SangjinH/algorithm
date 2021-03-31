from collections import deque


def solution(N, coffee_times):
    answer = []
    INF = int(1e9)
    if N == 1:
        return list(range(1, len(coffee_times) + 1))

    for idx, time in enumerate(coffee_times):
        coffee_times[idx] = [time, idx + 1]

    q = deque(coffee_times)

    stack = []
    while 1:

        if len(stack) < N and len(q) != 0:
            stack.append(q.popleft())
            continue

        if not stack:
            break

        mini = INF
        for i in stack:
            if i[0] < mini:
                mini = i[0]

        idx = 0
        tmp = []
        while 1:
            if idx == len(stack):
                break

            if stack[idx][0] == mini:
                tmp.append(stack.pop(idx)[1])
            else:
                stack[idx][0] -= mini
                idx += 1
        tmp.sort()
        if len(tmp) == 1:
            answer.append(tmp[0])
        else:
            for i in tmp:
                answer.append(i)

    return answer

print(solution(3, [4, 2, 2, 5, 3]))
print(solution(1, [100, 1, 50, 1, 1]))

# from collections import deque
#
# #
# # def solution(N, coffee_times):
# #     answer = []
# #
# #     if N == 1:
# #         return list(range(1, len(coffee_times) + 1))
# #
# #     for idx, time in enumerate(coffee_times):
# #         coffee_times[idx] = [time, idx + 1]
# #
# #     q = deque(coffee_times)
# #
# #     stack = []
# #     while 1:
# #
# #         if len(stack) < N and len(q) != 0:
# #             stack.append(q.popleft())
# #             continue
# #
# #         if not stack:
# #             break
# #
# #         stack.sort(key=lambda x: [x[0], x[1]])
# #
# #         mini = stack[0][0]
# #         for i in range(len(stack)):
# #             stack[i][0] -= mini
# #
# #         idx = 0
# #         while 1:
# #             if not stack:
# #                 break
# #             if stack[idx][0] == 0:
# #                 answer.append(stack.pop(0)[1])
# #                 continue
# #             break
# #
# #     return answer