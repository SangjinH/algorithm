from curses import meta
import sys
input = sys.stdin.readline


n = int(input())

meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings = sorted(meetings, key= lambda x : (x[0], x[1]))


# TODO Greedy!
# 최대한 빠른 시간에, 짧은 회의를 한다면 성공할 것이다.

def find_best(meetings):

    cnt = 0

    start_now = 0
    end_now = 0

    for s, e in meetings:

        # 다음에 등장한 시작 시간이 현재 끝나는 시간보다, 뒤라면
        if s >= end_now:
            cnt += 1
            start_now = s
            end_now = e
        else:
            if e < end_now:
                start_now = s
                end_now = e
        
    return cnt 
    


print(find_best(meetings))