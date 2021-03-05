# 재귀로 햄버거 구현
def dfs(idx, score, cal):
    global maxi
    # 문제 조건 : 칼로리가 제한이상이면 취소
    if cal > L:
        return

    # 인덱스가 마지막과 동일하면
    # 값비교를 통해 갱신
    if idx == N:
        if score > maxi:
            maxi = score
        return

    new_score = score + ingredients[idx][0]
    new_cal = cal + ingredients[idx][1]

    # 지금 식품을 사용한 것, 사용하지 않은 것. 두갈래로 나눠진행
    dfs(idx+1, score, cal)
    dfs(idx+1, new_score, new_cal)


T = int(input())
for tc in range(1, T+1):
    N, L = list(map(int, input().split()))
    ingredients = []
    for _ in range(N):
        ingredients.append(list(map(int, input().split())))

    maxi = 0
    dfs(0, 0, 0)
    print(f'#{tc} {maxi}')