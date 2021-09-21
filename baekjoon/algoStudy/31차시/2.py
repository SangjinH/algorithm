import sys
input = sys.stdin.readline
from collections import deque, defaultdict


lr_check = defaultdict(list)

saws = [[]]
for i in range(4):
    saws.append(deque(input().rstrip()))
    lr_check[i+1].append(saws[i+1][6])
    lr_check[i+1].append(saws[i+1][2])


def check_LR(idx, direction):
    if idx == 1:
        rotates = [idx]
        for i in range(idx, 4):
            if lr_check[i][1] != lr_check[i+1][0]:
                rotates.append(i+1)
            else:
                break

        for i in rotates:
            if direction == 1:
                saws[i].insert(0, saws[i].pop())
                direction *= -1
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]

            elif direction == -1:
                saws[i].append(saws[i].popleft())
                direction *= -1
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]

    elif idx == 4:
        rotates = [4]
        for i in range(4, 1, -1):
            if lr_check[i][0] != lr_check[i-1][1]:
                rotates.append(i-1)
            else:
                break

        for i in rotates:
            if direction == 1:
                saws[i].insert(0, saws[i].pop())
                direction *= -1
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]

            elif direction == -1:
                saws[i].append(saws[i].popleft())
                direction *= -1
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]

    else:
        rotates = [idx]
        for i in range(idx, 4):
            if lr_check[i][1] != lr_check[i+1][0]:
                rotates.append(i+1)
            else:
                break

        for i in range(idx, 1, -1):
            if lr_check[i][0] != lr_check[i-1][1]:
                rotates.insert(0, i-1)
            else:
                break

        for i in rotates:
            # 홀수만큼 차이나는 톱니바퀴면 다른 방향으로 회전
            if not int(abs((idx - i)))%2:
                rot_direction = direction
            else:
                rot_direction = direction * -1

            if rot_direction == 1:
                saws[i].insert(0, saws[i].pop())
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]

            elif rot_direction == -1:
                saws[i].append(saws[i].popleft())
                lr_check[i][0] = saws[i][6]
                lr_check[i][1] = saws[i][2]


K = int(input())
for _ in range(K):
    idx, direction, = map(int, input().split())
    check_LR(idx, direction)

result = 0
for i in range(1, len(saws)):
    if saws[i][0] == '1':
        result += 2**(i-1)

print(result)

defaultdict(list)

