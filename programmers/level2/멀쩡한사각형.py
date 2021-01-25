# https://programmers.co.kr/learn/courses/30/lessons/62048
import math
def solution(w,h):
    ans = w+h - math.gcd(w,h)
    res = w*h - ans
    return res