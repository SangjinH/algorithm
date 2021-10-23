def solution(sortedArray, findValue):

    s = 0
    e = len(sortedArray)-1

    while s <= e:
        mid = (s + e) // 2

        if sortedArray[mid] == findValue:
            return mid

        elif sortedArray[mid] > findValue:
            e = mid - 1

        elif sortedArray[mid] < findValue:
            s = mid + 1

    return -1



print(solution([1, 2, 5, 7, 10, 15, 18, 20], 15))
print(solution([1, 2, 5, 7, 10, 15, 18, 20], 17))
print(solution([1,2,3,4], 5))