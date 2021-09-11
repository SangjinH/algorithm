"""
재구매율 = 재구매한 고객수 / 상품을 한번이상구매한 고객수  * 100

재구매율을 기준으로 내림차순
재구매율이 같다면 구매횟수 내림차순
구매횟수까지 같다면 아이디가 낮은 순

"""
from pprint import pprint

from collections import defaultdict

def solution(records, k, date):

    standard_date = date.split("-")
    # print(standard_date)


    investigate_list = defaultdict(list)

    for record in records:
        record = record.split()
        user = record[1]
        item = record[2]
        # print(record)
        day = record[0].split('-')

        # 월이 같다면
        if int(day[1]) == int(standard_date[1]):
            if 0<= int(standard_date[-1]) - int(day[-1]) < 10:
                # print(standard_date, day)
                investigate_list[item].append(user)
        # 월이 다르다면
        else:
            diff = standard_date
            if int(standard_date[-1])+30 - int(day[-1]) < 10:
                # print(day, standard_date)
                investigate_list[item].append(user)

    answer = []
    # print(investigate_list)
    for k, v in investigate_list.items():
        check_list = set(v)
        m = 0
        c = 0
        total = len(v)

        num = ""
        for i in k:
            if i.isdigit():
               num += i
        for i in check_list:
            temp = v.count(i)
            if temp >= 1:
                m += 1
                if temp >= 2:
                    c += 1
        answer.append([c/m, total, int(num), k])

    answer.sort(key=lambda x:[-x[0], -x[1], x[2]])

    # print(answer)
    if not answer:
        answer = ["no result"]
    else:
        temp = []
        for i in answer:
            temp.append(i[-1])
        answer = temp
    return answer


print(solution(["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"], 10, "2020-03-05"))
print(solution(["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"], 10, "2020-02-05"))
print(solution(["2020-01-01 uid1000 pid5000"], 10, "2020-01-11"))
