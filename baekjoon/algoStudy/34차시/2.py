import sys
input = sys.stdin.readline

"""
김지민 임한수 언제만나나

"""

N, kim, lim = map(int, input().split())

players = [i for i in range(1, N+1)]

players[kim-1] = 'kim'
players[lim-1] = 'lim'

# print(players)
stage = 0
flag = False
while len(players) > 1:
    stage += 1
    temp = []
    for i in range(0, len(players), 2):
        left = players[i]
        # 홀수일경우 대비
        right = False
        if i+1 < len(players):
            right = players[i+1]

        if not right:
            temp.append(left)

        else:
            if left in ['kim', 'lim'] and right in ['kim', 'lim']:
                flag = True
                break

            if left in ['kim', 'lim']:
                temp.append(left)
            elif right in ['kim', 'lim']:
                temp.append(right)
            else:
                temp.append(left)
    if flag:
        break
    players = temp

print(stage)