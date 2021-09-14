"""

i번 강의와 j번 강의를 녹화하려면 i, j 사이의 모든 강의도 녹화해야함
블루레이의 갯수는 최소
블루레이는 같은크기

"""



import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# print(lectures)

total = sum(lectures)
l = max(lectures)
r = total

while l <= r:
    mid = (l+r)//2

    temp = 0
    cnt = 0
    for i in range(len(lectures)):
        if temp + lectures[i] > mid:
            cnt += 1
            temp = 0

        temp += lectures[i]

    else:
        if temp:
            cnt += 1

    if cnt > M:
        l = mid + 1
    else:
        r = mid - 1


print(l)
