# https://www.acmicpc.net/problem/1541

input_list = input().split('-')
result = []

for i in input_list:
    result.append(sum(map(int, i.split('+'))))

total = result[0]
for i in result[1:]:
    total -= i

print(total)