from collections import deque

s= '23four5six7'

match = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def solution(s):
    match = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    result = ''
    stack_str = ''
    for i in s:
        # 숫자이고
        if i.isdigit():
            # stack str 에 글자가 있다면
            if stack_str:
                result += str(match[stack_str])
            # 초기화하고 숫자 그대로 더해주기
            stack_str = ''
            result += str(i)
        # 문자라면
        else:
            if stack_str in match.keys():
                result += str(match[stack_str])
                stack_str = ''
            stack_str += i

    if stack_str:
        result += str(match[stack_str])

    return result

print(solution(s))