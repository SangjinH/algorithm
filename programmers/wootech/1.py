from collections import defaultdict

def solution(arr):

    check = defaultdict(int)
    maxi = 0

    for i in arr:
        check[i] += 1
        if check[i] > maxi:
            maxi = check[i]

    answer = []
    for i in range(1, 4):
        answer.append(maxi-check[i])

    return answer


print(solution([2, 1, 3, 1, 2, 1]))
