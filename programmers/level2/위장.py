"""
동그란 안경, 긴 코트, 파란색 티셔츠
+ 청바지 , + 선글라스를 대체

headgear : y, g
eyewear : b

조합을 만드는데 있어
기본적으로

{'face': ['crow_mask', 'blue_sunglasses', 'smoky_makeup']}

{'headgear': ['yellow_hat', 'green_turban'],
 'eyewear': ['blue_sunglasses']}

 총 두가지를 가지고 만들 수 있는 경우의 수는
 headgear, eyewear 는
 총 2^2 - 1
"""

from collections import defaultdict


def solution(clothes):
    pairs = defaultdict(list)

    for cloth in clothes:
        pairs[cloth[1]].append(cloth[0])

    print(pairs)

    ans = 1

    for key, value in pairs.items():
        ans *= (len(value) + 1)

    return ans - 1