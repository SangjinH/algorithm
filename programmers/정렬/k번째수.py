# https://programmers.co.kr/learn/courses/30/lessons/42748#

def solution(array, commands):
    answer = []
    for i in commands:
        temp_array = list(array[i[0] - 1:i[1]])
        temp_array.sort()
        answer.append(temp_array[i[2] - 1])

    return answer