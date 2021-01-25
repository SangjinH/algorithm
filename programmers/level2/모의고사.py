# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    seq_1 = [1, 2, 3, 4, 5] * 2000
    seq_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    seq_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    for i in range(len(answers)):
        if answers[i] == seq_1[i]:
            cnt_1 += 1
        if answers[i] == seq_2[i]:
            cnt_2 += 1
        if answers[i] == seq_3[i]:
            cnt_3 += 1

    lists = [cnt_1, cnt_2, cnt_3]

    maximum = max(lists)

    answer = []

    for i in range(len(lists)):
        if lists[i] == maximum:
            answer.append(i + 1)
    answer.sort()

    return answer