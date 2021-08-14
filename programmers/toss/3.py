def solution(amountText):
    answer = True

    for i in amountText:
        if not i.isdigit() and not i == ',':
            answer = False
            return answer

    if ',' in amountText:
        split_amountText = amountText.split(',')

        if len(split_amountText[0]) == 0 or len(split_amountText[0]) > 3:
            answer = False
            return answer

        for i in range(len(split_amountText)-1, 0, -1):
            if len(split_amountText[i]) != 3:
                answer = False
                return answer
        return answer

    else:
        if len(amountText) == 1:
            answer = True

        else:
            if int(amountText[0]) == 0:
                answer = False
            else:
                answer = True
        return answer

print(solution("10,000원"))
print(solution("24,999,99"))
print(solution(",999,000"))
print(solution("25,000,123"))
print(solution("0123000000,123"))