# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    sum = brown + yellow

    for i in range(sum + 1, 1, -1):
        if sum % i == 0 and sum // i > 2:
            if ((sum // i) - 2) * (i - 2) == yellow:
                return [i, sum // i]