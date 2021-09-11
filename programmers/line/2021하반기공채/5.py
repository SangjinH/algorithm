"""
닉네임과 이메일 주소가 모두 유사하면 동일한 유저
(a, b) 동일 (b, c) 동일 ==> (a, c) 동일

- 닉네임
    2개 이하의 문자를 삭제해 동일하게 만들면 두 닉네임은 유사
"""

from itertools import combinations

def nickname(nick1, nick2):
    # print(nick1, nick2)
    # 길이가 3이상 차이나면 return False
    if abs(len(nick1)-len(nick2)) >= 3:
        return False

    nick1 = list(nick1)
    nick2 = list(nick2)
    # 크기순으로 정렬, nick1이 같거나 긴 닉네임
    if len(nick1) < len(nick2):
        nick1, nick2 = nick2, nick1

    cnt = 0
    for i in range(len(nick2)):
        if nick2[i] in nick1:
            nick1.remove(nick2[i])
            nick2[i] = '.'

    if cnt + len(nick1) + len(nick2) - nick2.count('.') <= 2:
        return True
    else:
        return False


def email(email1, email2):
    email1 = email1.split('@')
    email2 = email2.split('@')

    # print(email1, email2)
    # 아이디가 같으면 True


    if len(email1[0]) < len(email2[0]):
        email1, email2 = email2, email1
        # print(email1, email2)

    if email1[0] == email2[0]:
        return True
    else:
        # 아이디는 다르지만 이메일 주소가 같다면
        if email1[-1] == email2[-1]:
            # print(email1, email2, "asdfadsfdas")

            email1[0] = list(email1[0])
            email2[0] = list(email2[0])

            cnt = 0
            for i in range(len(email2[0])):
                if email2[0][i] in email1[0]:
                    email1[0].remove(email2[0][i])
                    email2[0][i] = '.'
                else:
                    cnt += 1
            # print(email1[0], email2[0], 'asdfsdafsadfsdafsadfasdfs')
            if cnt + len(email1[0]) + len(email2[0]) - email2[0].count('.') <= 1:
                return True
            else:
                return False

        # 아이디는 다르고 이메일 주소도 다르다면
        else:
            return False


def solution(nicks, emails):
    check = [i for i in range(len(nicks))]

    for comb in combinations(list(range(len(nicks))), 2):
        # print(comb)
        # print(nickname(nicks[comb[0]], nicks[comb[1]]))
        # print(email(emails[comb[0]], emails[comb[1]]))
        if nickname(nicks[comb[0]], nicks[comb[1]]) and email(emails[comb[0]], emails[comb[1]]):
            check[comb[1]] = check[comb[0]]
            # print(check)



    # print(check)
    return len(set(check))



print(solution(["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"],
               ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]))

print(solution(["99police", "99poli44"], ["687ufq687@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"]))
print(solution(["99polico", "99policd"], ["687ufq687@aaa.xx.yyy", "587ufq687@aaa.xx.yyy"]))