# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answers = []

    for i in range(1,len(s)//2+1):
        answer = ""
        cnt = 1
        for j in range(0, len(s)-1, i):
            print(j)
            if s[j:j+i] == s[j+i:j+2*i] and j+2*i <= len(s):
                cnt += 1
                if j + 2 * i >= len(s):
                    if cnt == 1:
                        answer = answer + s[j:-1]
                        break
                    else:
                        answer = answer + str(cnt) + s[j:j+i]
                        break
            else:
                if cnt != 1:
                    answer = answer + str(cnt) + s[j:j+i]
                elif cnt == 1:
                    answer = answer + s[j:j+i]
                cnt = 1
        answers.append(answer)

    return answers


# s = "aabbaccc"
# print(solution(s))

s = "abcabcdede"
print(solution(s))
