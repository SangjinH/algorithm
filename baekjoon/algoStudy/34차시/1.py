import sys
input = sys.stdin.readline
from itertools import combinations

"""
주어진 단어를 세 개의 더 작은 단어로 나누는 것
적어도 길이가 1 이상
"""

word = input().rstrip()

idxs = [i for i in range(1, len(word))]
# print(idxs)

# print(word)

cases = list(combinations(idxs, 2))
answer = []

for case in cases:
    # print(case)
    first = word[:case[0]]
    second = word[case[0]:case[1]]
    third = word[case[1]:]

    # print(first, second, third)

    answer.append(first[::-1] + second[::-1] + third[::-1])

print(min(answer))


