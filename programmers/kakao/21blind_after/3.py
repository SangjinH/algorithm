"""
기본요금 180분에 5000원

그 이후로 10분당 600 원
누적주차시간 계산

초과한 시간이 단위시간으로 나눠떨어지지 않으면 올림
"""

import math
from collections import defaultdict


def all_minutes(time):
    h, m, = time.split(":")
    return int(h)*60 + int(m)


def charge(time, fees):
    if time <= fees[0]:
        return fees[1]

    else:
        time -= fees[0]
        return fees[1] + math.ceil(time / fees[2]) * fees[-1]



def solution(fees, records):

    parking = defaultdict(list)

    for record in records:
        record = record.split()
        parking[record[1]].append(all_minutes(record[0]))

    answer = []
    for k, v in sorted(parking.items()):
        if len(v) % 2:
            v.append(all_minutes("23:59"))

        # print(v)
        total = 0
        for i in range(0, len(v), 2):
            total += (v[i+1] - v[i])

        # print(k, total, "k : total ")
        answer.append(charge(total, fees))

    return answer





print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
