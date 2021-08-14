def solution(input):
    inputs = list(input.split('\n'))
    print(inputs)

    keys = ['SHOW', 'NEXT', 'EXIT', 'NEGATIVE']


    m, n = map(int, inputs[0].split())

    answer  = ''+str(m)+ ' '+str(n) + '\n'

    negative = False
    negative_days = 0

    total_show = 0
    days = 1

    days_show = [0] * 10000

    for i in inputs[1:]:
        if i not in keys:
            answer += "ERROR\n"
        elif i == "BYE":
            answer += "BYE"
            return answer

        elif i == "SHOW":
            if negative:
                answer += "0\n"
            else:
                if total_show < n:
                    answer += "1\n"
                    days_show[days] += 1
                    total_show += 1
                else:
                    answer += "0\n"

        elif i == "NEXT":

            answer += "-\n"
            days += 1
            if days > m:
                total_show -= days_show[days-m]

            if negative:
                negative_days += 1

                if negative_days > m:
                    negative_days = 0
                    negative = False


        elif i == "NEGATIVE":
            negative = True

    return str(answer)

print(solution("1 3\nSHOW\nNEXT\nEXIT"))