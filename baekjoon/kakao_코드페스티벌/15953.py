# https://www.a
# cmicpc.net/problem/15953
# 상금헌터
import sys
input = sys.stdin.readline


def price_2017(rank):
    if rank == 0:
        return 0
    if rank == 1:
        return 5000000
    elif rank < 4:
        return 3000000
    elif rank < 7:
        return 2000000
    elif rank < 11:
        return 500000
    elif rank < 16:
        return 300000
    elif rank < 22:
        return 10
    else:
        return 0
def price_2018(rank):
    if rank == 0:
        return 0
    if rank == 1:
        return 5120000
    elif rank < 4:
        return 2560000
    elif rank < 8:
        return 1280000
    elif rank < 16:
        return 640000
    elif rank < 32:
        return 320000
    else:
        return 0
ranks = []
n = int(input().rstrip())
for _ in range(n):
    ranks.append(list(map(int, input().rstrip().split())))

for i in ranks:
    print(price_2017(i[0])+price_2018(i[1]))