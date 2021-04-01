import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    N = int(input())
    num_list = list(input())
    print(num_list)

    flag = True
    for i in p:
        if i == 'D':
            if not num_list:
                flag = False
                break

            num_list.pop(0)

        elif i == 'R':
            num_list = num_list[::-1]

    if flag:
        print(num_list)
    else:
        print('error')