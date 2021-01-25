# https://www.acmicpc.net/problem/4796
# 백준 4796번, 그리디 알고리즘

import sys
input = sys.stdin.readline

case_list = []
while True:
    l, p , v = map(int, input().rstrip().split())
    if (l, p, v) == (0, 0, 0):
        break
    case_list.append([l,p,v])

# print(case_list)
for i in range(len(case_list)):
    l, p, v = case_list[i][0], case_list[i][1], case_list[i][2]
    use_days = 0
    use_days += (v//p) * l


    if v % p <= l:
        use_days += (v%p)
    else:
        use_days += l

    print("Case "+ str(i+1) + ": {}".format(use_days))
