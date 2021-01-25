def solution(s):

    answers = []

    for i in range(1, len(s)//2 + 1):
        ans = ""
        cnt = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
                continue
            else:
                if cnt != 1:
                    ans = ans + str(cnt) + s[j:j+i]
                    cnt = 1
                else:
                    ans = ans + s[j:j+i]

        answers.append(len(ans))

    return min(answers)


s = "aabbaccc"
print(solution(s))

s = "abcabcdede"
print(solution(s))