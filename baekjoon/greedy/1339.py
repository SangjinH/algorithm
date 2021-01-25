# 백준 1339 그리디 단어수학
import sys
from string import ascii_uppercase
input = sys.stdin.readline

n = int(input().rstrip())

alph = {}
for i in ascii_uppercase:
    alph[i] = 0

for _ in range(n):
    letter = input().rstrip()
    for i in range(len(letter)):
        alph[letter[i]] += 10**(len(letter)-i-1)

vals = sorted(list(alph.values()), reverse=True)

cnt = 9
result = 0
for i in vals:
    if i == 0:
        break
    result += i*cnt
    cnt -= 1

print(result)