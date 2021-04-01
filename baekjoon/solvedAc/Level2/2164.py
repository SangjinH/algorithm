import sys
input = sys.stdin.readline

N = int(input())
num_list = list(range(1, N+1))

while 1:
    if N == 1:
        print(1)
        break
    # 홀수 갯수라면
    if len(num_list) % 2 == 1:
        last = [num_list.pop()]
    else:
        last = []

    temp = []
    for i in range(1, len(num_list)+1, 2):
        temp.append(num_list[i])

    temp = last + temp

    if len(temp) == 1:
        print(*temp)
        break

    num_list = temp





