# 백준 2217

n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))
ropes.sort()

maximum = min(ropes)*n

for i in ropes[1:]:
    n -= 1
    if i * n > maximum:
        maximum = i*n

print(maximum)
