def solution(numbers):
    sums = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            sums.append(numbers[i] + numbers[j])
    sums.sort()

    answer = list(set(sums))
    answer.sort()
    return answer