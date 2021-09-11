"""
info의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수입니다. ( i는 0~10 사이의 정수입니다.)
"""




def solution(n, info):

    cases = []
    for i in info:
        cases.append(i+1)

    maxi = 0
    check = [0] * 11

    def dfs(idx, total, n, cnt):
        if cnt > n:
            return
        elif cnt == n:
            print(total)
            print(cnt)
            print(check)
            return

        for i in range(idx, 11):
            if not check[idx]:
                check[idx] = cases[idx]
                print(check)
                dfs(idx + 1, total + (10 - idx) * cases[idx], n, cnt + cases[idx])
                check[idx] = 0

    dfs(0, 0, n, 0)
    # print(maxi)


    # print(info)
    # print(cases)


    answer = []
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
