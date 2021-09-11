"""
여러명 신고할 수 있고
한 명에게 여러번 신고할 수있으나 신고횟수는 1회로 처리

k번 이상 신고된 유저는 이용정지
해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
    게시판 이용이 정지된 유저도 불량 이용자를 신고할 수 있음

"""
from collections import defaultdict


def solution(id_list, report, k):

    # print(id_list)
    #
    # print(report)
    report_list = defaultdict(list)

    for r in report:
        pick, picked = r.split()
        report_list[picked].append(pick)

    # print(report_list)

    results = defaultdict(int)

    for key, value in report_list.items():
        temp = list(set(list(value)))
        # print(temp, "asdfsdfa")
        if len(temp) >= k:
            for person in temp:
                results[person] += 1

    answer = []
    for i in id_list:
        answer.append(results[i])

    return answer



print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
