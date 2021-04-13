import sys
input = sys.stdin.readline

N = int(input())

items = [int(input()) for _ in range(N)]

items.sort()

result = 0
idx = len(items) % 3

if idx != 0: # 3의 배수의 갯수가 아니면
    result += sum(items[:idx])
    items = items[idx:]

for i in range(len(items)-1, -1, -3):
    result += items[i]
    result += items[i-1]

print(result)