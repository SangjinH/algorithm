def solution(L, x):
    low = 0
    high = len(L) - 1

    while low < high:
        middle = (low + high) // 2
        if high - low <= 1:
            return -1
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            low = middle
        else:
            high = middle

print(solution([2,5,7,9,11], 4))