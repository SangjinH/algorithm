def solution(a, b):
    yoil = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    d = 0
    if a == 1:
        d += b
        return yoil[d % 7]

    for i in range(a - 1):
        d += days[i]

    d += b

    return yoil[d % 7]