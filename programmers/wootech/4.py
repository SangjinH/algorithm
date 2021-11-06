from collections import deque

def solution(s):

    s = deque(s)
    cnt = 0

    while 1:
        if cnt == len(s):
            break

        if s[0] == s[-1]:
            s.append(s.popleft())
            cnt += 1

        else:
            break

    answer = []

    standard = s.popleft()
    cnt = 1
    while s:
        now = s.popleft()
        if now == standard:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            standard = now

    answer.append(cnt)

    return sorted(answer)



print(solution("aaabbaaa"))
print(solution("wowwow"))