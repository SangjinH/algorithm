"""


"""
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    check = defaultdict(int)

    for order in orders:
        str_order = list(order)
        for i in course:
            for j in combinations(str_order, i):
                temp = "".join(sorted(list(j)))

                if check[temp]:
                    check[temp] += 1
                else:
                    check[temp] = 1

    answer = defaultdict(list)

    for i in check.keys():
        if not answer[len(i)]:
            if check[i] >= 2:
                answer[len(i)].append((i, check[i]))
        else:
            if check[i] > answer[len(i)][0][1]:
                answer[len(i)] = [(i, check[i])]
            elif check[i] == answer[len(i)][0][1]:
                answer[len(i)].append((i, check[i]))

    result = []
    for i in answer.values():
        for j in i:
            result.append(j[0])

    result.sort()

    return result


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))