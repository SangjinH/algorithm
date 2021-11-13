from collections import defaultdict
#
# def solution(S):
#     if len(S) == 1:
#         return []
#
#     for i in range(len(S)):
#         a = list(S[i])
#         for j in range(i+1, len(S)):
#             b = list(S[j])
#
#             for k in range(len(b)):
#                 if a[k] == b[k]:
#                     return [i, j, k]
#
#     return []


def solution(S):
    if len(S) == 1:
        return []

    check = defaultdict(list)

    for i in range(len(S)):
        for j in range(len(S[i])):
            if not check[S[i][j]]:
                check[S[i][j]] = [[] for _ in range(len(S[i]))]
                check[S[i][j]][j].append(i)
            else:
                if check[S[i][j]][j]:
                    return [check[S[i][j]][j][0], i, j]

    return []