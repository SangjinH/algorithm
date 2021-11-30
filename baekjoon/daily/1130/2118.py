import sys
input = sys.stdin.readline

n = int(input())

roads = [0]

for _ in range(n):
    roads.append(int(input()))

for i in range(1, len(roads)):
    roads[i] += roads[i-1]

print(roads)

start = 1
end = 2

circle = roads[end]-roads[start]
re_circle = roads[-1] - circle


