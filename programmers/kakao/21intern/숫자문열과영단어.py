
"""

"""


def alpha_to_int(x):
    match = {"zero": 0,
             "one": 1,
             "two": 2,
             "three": 3,
             "four": 4,
             "five": 5,
             "six": 6,
             "seven": 7,
             "eight": 8,
             "nine": 9}
    return match[x]


def solution(s):
    match = {"zero": 0,
             "one": 1,
             "two": 2,
             "three": 3,
             "four": 4,
             "five": 5,
             "six": 6,
             "seven": 7,
             "eight": 8,
             "nine": 9}

    answer = ""

    temp = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if len(temp) >= 3 and temp in match.keys():
                answer += str(alpha_to_int(temp))
                temp = ""

    return int(answer)



print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
