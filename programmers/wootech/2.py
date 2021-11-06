"""
공부를 시작하고 5분 이내로 중지하면 포함 X
공부를 시작하고 1H 45M이 넘어서 중지하면 1H 45M 만 인정

"""


def trans_time(time):
    H, M = time.split(':')
    return int(H)*60 + int(M)


def time_check(time):
    if time < 5:
        return 0

    if time >= 105:
        return 105

    return time


def change_time(total):
    H = total // 60
    M = total % 60

    if H < 10:
        H = '0' + str(H)
    else:
        H = str(H)

    if M < 10:
        M = '0' + str(M)
    else:
        M = str(M)

    return f'{H}:{M}'



def solution(log):

    total = 0
    for i in range(0, len(log), 2):
        start = trans_time(log[i])
        end = trans_time(log[i+1])

        total += time_check(end-start)

    answer = change_time(total)
    return answer




print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]	))
