"""
마침표는 처음과 끝에 사용할 수 없고, 연속으로 사용할 수 없음


"""


def solution(new_id):

    new_id = new_id.lower()
    # print(new_id)

    temp = ""
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            if not temp:
                temp += i

            else:
                if i == '.':
                    if temp[-1] == '.':
                        continue
                    else:
                        temp += i
                else:
                    temp += i

    # print("temp ", temp)
    # 앞뒤가 . 이라면 잘라내기
    temp = temp.rstrip(".")
    temp = temp.lstrip(".")

    # print("temp : ", temp)

    if not temp:
        temp += "a"

    if len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == ".":
            temp = temp.rstrip(".")

    if len(temp) <= 2:
        temp += (temp[-1] * (3-len(temp)))

    answer = temp
    return answer



print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))

