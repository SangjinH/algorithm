""" Quick Sort
분할정복, 재귀를 이용한 정렬알고리즘

기본 아이디어
1. 기준값은 Pivot을 정한다.
2. list를 선회하면서 Pivot 보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 이동
"""


def quick(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[len(num_list)//2]
    less_arr, equal_arr, great_arr = [], [], []

    for num in num_list:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            great_arr.append(num)
        else:
            equal_arr.append(num)

    return quick(less_arr) + equal_arr + quick(great_arr)


arr = [1, 3, 5, 2, 7, 3, 5]
# print(quick(arr))

# 위 내용은 이해하기는 쉬우나 메모리 사용측면에서 배우 비효율적이므로
# Version2. Quick


def quick2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    l = 1
    r = len(arr) - 1

    while l <= r:

        while l <= len(arr) - 1 and arr[l] < pivot:
            l += 1

        while r >= 0 and arr[r] > pivot:
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l = 1
            r = len(arr)-1
        else:
            break
    arr[0], arr[r] = arr[r], arr[0]

    return quick2(arr[:r]) + [pivot] + quick2(arr[r+1:])




arr = [3, 1, 5, 7, 2, 8, 10]
print(quick2(arr))
