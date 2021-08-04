import sys
input = sys.stdin.readline
from collections import defaultdict

a, p = map(int, input().split())

# 같은 숫자가 나오면 그 뒤로는 계속 반복되는 수열
# 같은 숫자가 나오는 위치 찾기


check = defaultdict(int)

idx = 0

d = [str(a)]
check[str(a)] = idx


def is_in(str_num, p):

    temp = 0
    for i in str_num:
        temp += int(i) ** p

    if str(temp) in check.keys():
        return True
    return False


while 1:

    temp = 0
    for i in d[-1]:
        temp += int(i) ** p

    if str(temp) in check.keys():
        print(check[str(temp)])
        break

    idx += 1
    d.append(str(temp))
    check[str(temp)] = idx