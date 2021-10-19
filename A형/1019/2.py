"""
타당도
(A+B)**2 + (C+D)**2
교차 불가
인접 노선 불가
인접한 두 역으로 도착 불가
1개에 여러개 불가

"""

from itertools import combinations


def make_road(N):
    numbers = [i for i in range(N)]

    routes = list(combinations(numbers, 2))
    candidates = list(combinations(routes, 2))
    return candidates


def validate(route_list, N):
    # print(route_list)

    s1, e1 = route_list[0]
    # print(s1, e1, "s1, e1")
    s2, e2 = route_list[1]
    # print(s2, e2, "s2, e2")

    if abs(s1-s2) <= 1 or abs(e1-e2) <= 1:
        return False

    if e2 >= e1 and e1 >= s2:
        return False

    if abs(e1-s2) <= 1:
        return False

    if abs(s1-e1) <= 1 or abs(s2-e2) <= 1:
        return False

    return True



def calculate(s1, e1, s2, e2, stations):
    return (stations[s1] + stations[e1])**2 + (stations[s2] + stations[e2])**2


T = int(input())

for t in range(1, T+1):
    N = int(input())

    stations = list(map(int,input().split()))

    # print(stations)

    maxi = 0
    candidates = make_road(N)
    # print(stations)

    for i in candidates:
        if validate(i, N):
            # print("True인 i", i)
            s1, e1 = i[0][0], i[0][1]
            s2, e2 = i[1][0], i[1][1]
            dist = calculate(s1,e1, s2, e2, stations)
            if dist > maxi:
                # print(i)
                maxi = dist

    print(f'#{t} {maxi}')

