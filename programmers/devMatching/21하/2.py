check = {
    'MON': 5,
    'TUE': 4,
    'WED': 3,
    'THU': 2,
    'FRI': 1,
}


def solution(leave, day, holidays):
    if leave == 30:
        return 30

    if day not in ['SAT', 'SUN']:
        sat = 1 + check[day]
        sun = sat + 1
    elif day == 'SAT':
        sat = 1
        sun = 2

    elif day == 'SUN':
        sun = 1
        sat = 7

    holidays.append(sat)
    holidays.append(sun)
    sat += 7
    sun += 7

    while 1:
        if sat <= 30:
            holidays.append(sat)
            sat += 7
        else:
            break

    while 1:
        if sun <= 30:
            holidays.append(sun)
            sun += 7
        else:
            break

    holidays = list(set(sorted(holidays)))

    answer = 0
    cnt = 0
    total = 0
    for start in range(1, 30):
        e = start
        while cnt < leave and e <= 30:
            if e not in holidays:
                cnt += 1
            total += 1
            e += 1

        while e in holidays:
            total += 1
            e += 1

        if total > answer:
            answer = total
        total = 0
        cnt = 0

    return answer







print(solution(4,"FRI", [6, 21, 23, 27, 28]))
print(solution(3,"SUN",[2, 6, 17, 29]))
print(solution(30,"MON",[1, 2, 3, 4, 28, 29, 30]))