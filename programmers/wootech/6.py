def change_minutes(time):
    if time[-2:] == 'AM':
        return int(time[:-2])*60

    else:
        return (int(time[:-2])+12)*60

def solution(time, plans):

    check = {
        'mon': [13*60, 18*60],
        'fri': [9*60+30, 18*60]
    }

    time = int(time) * 60 + (time - int(time)) * 60
    answer = ''
    for p in plans:
        destination, take_off, land = p
        take_off = change_minutes(take_off)
        land = change_minutes(land)

        total = 0

        # 금요일 출근시간 전에 출발한다면
        if take_off <= check['fri'][0]:
            total += check['fri'][1] - check['fri'][0]
        else:
            temp = check['fri'][1] - take_off
            if temp > 0:
                total += temp

        # 월요일 퇴근시간보다 늦게 도착한다면
        if land >= check['mon'][1]:
            total += check['mon'][1] - check['mon'][0]
        else:
            temp = land - check['mon'][0]
            if temp > 0:
                total += temp

        if total <= time:
            answer = destination
            break

    return answer



print(solution(3.5, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]	))
print(solution(5, [['서울', "3PM", "7AM"],['부산', "2PM", "7AM"]]))