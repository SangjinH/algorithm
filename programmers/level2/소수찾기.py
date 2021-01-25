# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
import math

def solution(numbers):
    answer = 0
    nums = []
    for i in numbers:
        nums.append(int(i))
    # print(nums)
    per_lists = []
    for i in range(1, len(nums)+1):
        per_lists.append(list(permutations(nums, i)))

    num_list = []
    for i in per_lists:
        for j in i:
            s = ""
            for k in j:
                s = s + str(k)
            num_list.append(int(s))

    num_list = list(set(num_list))
    if 1 in num_list:
        num_list.remove(1)
    if 0 in num_list:
        num_list.remove(0)

    cnt = 0
    for i in num_list:
        check = True
        for j in range(2,i-1):
            if math.gcd(i,j) != 1:
                check = False
                break

        if check:
            cnt += 1

    return cnt


numbers = "011"
print(solution(numbers))