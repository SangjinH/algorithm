import sys
input = sys.stdin.readline
from collections import deque

def make_tree(start):
    global idx

    # 들어온 숫자가 2**K 를 넘지 않으면
    if start < 2**K:
        make_tree(start*2)
        tree[start] = nums[idx]
        idx += 1
        make_tree(start*2 + 1)


K = int(input())
nums = list(map(int, input().split()))
tree = [0] * (2**K)
idx = 0
make_tree(1)
q = deque([1])
P_num = 1
while P_num < 2**K:
    temp = []
    for i in range(P_num):
        temp.append(q.popleft())

    for i in temp:
        print(tree[i], end=' ')

        if i*2 + 1 < 2**K:
            q.append(i*2)
            q.append(i*2+1)
            # print(q)
    P_num *= 2
    print()



