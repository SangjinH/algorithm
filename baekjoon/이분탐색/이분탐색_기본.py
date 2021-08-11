"""

이분 탐색의 기본 모형을 소개하고자
만든 파일입니다.

"""


def Binary(arr, val, low, high):
    # 종료조건
    if low > high:
        return False  # 해당 배열에 타겟 숫자 미존재

    mid = (low + high) // 2 # 위치 기반으로 찾는 것

    if arr[mid] > val: # 중간의 위치에 있는 값보다 찾는 값이 크다면
        Binary(arr, val, mid+1, high)

    elif arr[mid] < val: # 값이 더 작다면
        Binary(arr, val, low, mid-1)

    else: # 값을 찾았다면
        return True

