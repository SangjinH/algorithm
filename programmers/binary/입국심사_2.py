"""
이분 탐색이 맞네요 ,,,,
설명을 보고 알았습니다. 

그 때, 그 떄의 상황을 생각하지않고 결과적인 부분을 먼저 생각합니다.

예로는, 실제로 어떠한 시간을 줬을때 심사할 수 있는 사람들을 확인하는 것입니다. 놀랍습니다 ,,

"""


n = 6
times = [7, 10]

def solution(n, times):

    answer = 0

    left = 1
    right = max(times) * n + 1

    while left <= right:
        mid = (left + right) // 2

        avail_person = 0
        for time in times:
            avail_person += (mid // time)
        
        if avail_person >= n:
            answer = mid
            right = mid - 1
        else:

            left = mid + 1
            
    return answer


print(solution(n, times))