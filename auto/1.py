def dfs(idx, arr, arr1, arr2):

    if idx == len(arr):
        if arr1 and arr2:
            return abs(sum(arr1)-sum(arr2))
        return sum(arr)

    left = dfs(idx+1, arr, arr1+[arr[idx]], arr2)
    right = dfs(idx+1, arr, arr1, arr2+[arr[idx]])

    if left < right:
        return left
    elif left == right:
        return left
    else:
        return right

from itertools import combinations

def solution(arr):
    standard = sum(arr)
    answer = dfs(0, arr, [], [])

    # answer = 10 * len(arr)
    # for i in range(1, len(arr)):
    #     candidates = list(combinations(arr, i))
    #     for j in candidates:
    #
    #         sum1 = sum(j)
    #         sum2 = standard - sum1
    #         temp = abs(sum2 - sum1)
    #         if temp < answer:
    #             answer = temp
    #             print(arr, j, "answer", answer)
                # print(j)

    return answer




    # return answer


print(solution([-2, -1, 1, 2]))
print(solution([10, -9, 3, 1, 10, -2, -5, 13]))
print(solution([0, 2, 4, 1, -5, -10, 2, 5, 7]))
print(solution([6, 5, -4, -5]))
