from collections import deque

def solution(startNumber, endNumber):
    result = []
    answer = deque()
    for _ in range(9):
        answer.append(0)

    answer.append(startNumber)
    if startNumber >= endNumber:
        change = -1
    else:
        change = 1

    while startNumber != endNumber:
        result.append("".join(map(str, answer)))

        startNumber += change
        answer.popleft()
        answer.append(startNumber)
    result.append("".join(map(str, answer)))

    return result


print(solution(2, 3))
print(solution(3, 3))