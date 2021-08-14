import heapq


def solution(fruitWeights, k):
    answer = []
    for i in range(k, len(fruitWeights)+1):
        temp = max(fruitWeights[i-k:i])
        if temp not in answer:
            heapq.heappush(answer, temp)

    return answer[::-1]


fruitWeights= [30, 40, 10, 20, 30]
k= 3

print(solution(fruitWeights, k))