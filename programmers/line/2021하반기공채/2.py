"""
연속된 n일 동안 최소 k 번 이상 검색되고
같은 n 일동안 총 2nk 번 검색되면 이슈검색어
여러번 이슈검색어가 된 검색어가 최고의 이슈검색어
    여러개일 경우 사전순으로 빠른 것

n 날짜
k 번
"""

from collections import defaultdict


def solution(research, n, k):

    issues = []

    cnt_dict = defaultdict(int)
    cnt_days = []
    # 전체 확인 범위
    for i in range(len(research)-n+1):
        # 연속된 날짜에서 확인
        for j in research[i:i+n]:
            for m in set(list(j)):
                num_cnts = list(j).count(m)
                if num_cnts >= k:
                    cnt_dict[m] += num_cnts
                    cnt_days.append(m)

        r = set(cnt_days)
        for l in r:
            if cnt_days.count(l) >= n and cnt_dict[l] >= 2*n*k:
               issues.append(l)

        cnt_dict = defaultdict(int)
        cnt_days = []

    issues.sort()
    check = sorted(list(set(issues)))

    answer = "None"
    maxi = 0

    for i in check:
        temp = issues.count(i)
        if temp > maxi:
            answer = i
            maxi = temp

    return answer


print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2))
print(solution(["yxxy","xxyyy"], 2, 1))
print(solution(["yxxy","xxyyy","yz"], 2, 1))
print(solution(["xy","xy"], 1, 1))
