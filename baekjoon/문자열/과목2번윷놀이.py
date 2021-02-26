# 1. A, B 순서정하기
# 2.순서를 돌면서 값이 같아지면 1로 초기화

start = input()
A_list = list(map(int, input().split()))  # [1, 2, 3]
B_list = list(map(int, input().split()))
AB_list = [A_list, B_list]

if start == 'A':
    seq_list = [0, 1]
else:
    seq_list = [1, 0]

distance = [1, 1]  # A, B = 1, 1

for i in range(10):  # i = 0
    check = False
    for j in seq_list:  # 1
        print(distance)
        distance[j] += AB_list[j][i]  # AB_list[j] = B_list[0]

        if distance[j] >= 20:
            if j == 1:
                winner = 'B'
                check = True
                break
            else:
                winner = 'A'
                check = True
                break

        if distance[j] == distance[j - 1]:
            distance[j - 1] = 1

    if check:
        break

if check:
    print(winner)
else:
    print('AB')