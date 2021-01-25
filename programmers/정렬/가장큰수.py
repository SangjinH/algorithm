# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    cases = [[] for _ in range(10)]

    for i in numbers:
        cases[int((str(i)[0]))].append(i)

    cases.sort(reverse=True)

    result = ''
    for i in cases:
        if len(i) < 1:
            continue
        elif len(i) == 1:
            result = result + str(i.pop())
        elif len(i) > 1:
            for j in i.sort(reverse=True):
                if j/11 >= i[-1]:
                    result = result + str(j)
                    continue


