

k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

# k = 2
# num =[6, 9, 7, 5]
# links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]

import heapq

def solution(k, num, links):

    p = [i for i in range(len(num))]
    left = []
    right = []
    leaf = []

    for i in range(len(links)):
        left.append(links[i][0])
        right.append(links[i][1])

        cnt = 0
        if links[i][0] != -1:
            p[links[i][0]] = i
        else:
            cnt += 1

        if links[i][1] != -1:
            p[links[i][1]] = i
        else:
            cnt += 1

        # 끝 노드라면
        if cnt == 2:
            leaf.append(i)

    check = [False] * len(num)

    # 끝노드가 없으면
    while leaf:
        new_leaf = []
        for i in range(len(num)):
            # 끝노드가 달려있는 노드라면
            for j in [left[i], right[i]]:
                if j in leaf:
                    if not check[j]:
                        num[i] += num[j]
                        new_leaf.append(i)
                        check[j] = True
        leaf = new_leaf


    maxi = max(num)
    if k == 1:
        return maxi
    else:
        standard = maxi // k

    min_bet = 10000000
    st_idx = 0
    for i in range(len(num)):
        temp = abs(num[i] - standard)
        if temp < min_bet:
            min_bet = temp
            st_idx = i

    print(st_idx)
    for i in range(len(num)):
        # 왼쪽 오른쪽 확인하면서
        for j in [left[i], right[i]]:
            # 자르려고 하는 idx 를 자식으로 갖고있다면
            if j == st_idx:
                # num[i] -= num[st_idx]
                while j != p[j]:
                    print('j: ', j)
                    j = p[j]
                    num[j] -= num[st_idx]

    print(num)
    answer = 0
    return


print(solution(k,num,links))