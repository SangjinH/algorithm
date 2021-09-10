"""

"""
from collections import defaultdict
import copy
import bisect


def solution(info, query):
    TF_case = []

    def find_TF_case(arr):

        if len(arr) == 4:
            TF_case.append(arr[:])
            return

        for i in [False, True]:
            arr.append(i)
            find_TF_case(arr)
            arr.pop()

    find_TF_case([])
    all_case = defaultdict(list)

    for i in info:
        i = i.split()
        value = i[-1]
        i = i[:-1]
        for j in TF_case:
            temp = copy.deepcopy(i)
            for k in range(len(temp)):
                if not j[k]:
                    temp[k] = "-"
            key = "".join(temp)
            all_case[key].append(int(value))

    answer = []
    for q in query:
        q = q.replace("and", "").split()

        standard = int(q[-1])
        key = "".join(q[:-1])

        lo_idx = bisect.bisect_left(sorted(all_case[key]), standard)
        answer.append(len(all_case[key])-lo_idx)

    return answer




print(
    solution(
        ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
        ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

