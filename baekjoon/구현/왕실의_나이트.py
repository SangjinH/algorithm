# https://doodreamcode.tistory.com/27 출처

origin = input()
x, y = origin[0],origin[1]

row = [x for x in range(1,9)]
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# column = [x for x in range(1,9)]

x = column.index(x)
y = int(y)

result = 0


dx = [1, -1, -2, -2, -1, 1, 2, 2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue

    result += 1

print(result)