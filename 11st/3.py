
def solution(N):
    if N > 100000000:
        return -1

    nums = [0]*(10)

    for i in str(N):
        nums[int(i)] += 1

    result = ''
    for i in range(9, -1, -1):
        if nums[i]:
            result += str(i)*nums[i]

    return int(result)
