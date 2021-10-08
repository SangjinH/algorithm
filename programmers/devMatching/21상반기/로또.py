# 알아볼 수 없는 번호 0,
# 최고 순위, 최저 순위를 찾아라

rank = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}


def solution(lottos, win_nums):
    answer = []

    possible = lottos.count(0)

    correct = 0
    for i in lottos:
        if i in win_nums:
            correct += 1

    answer.append(rank[correct + possible])
    if correct in rank.keys():
        answer.append(rank[correct])
    else:
        answer.append(6)

    return answer