"""
한 기업에 a 원 투자하기로 했다면
나머지기업은 N-a 원 투자

"""

from collections import defaultdict


N, M = map(int, input().split())
infos = defaultdict(list)
infos[0] = [[0, i] for i in range(1, M+1)]
for _ in range(N):
    profits = list(map(int, input().split()))
    for idx, value in enumerate(profits[1:]):
        infos[profits[0]].append([value, idx+1])

