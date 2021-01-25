# https://www.acmicpc.net/problem/15904
import sys
input = sys.stdin.readline

word_list = list(input().split())

temp = ""
for i in word_list:
    temp += i

target = "UCPC"

results = []
for i in target:
    if i in temp:
        results.append(temp.index(i))
        temp = temp[temp.index(i):]

if len(results) == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')