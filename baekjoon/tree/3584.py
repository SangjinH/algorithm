import sys
input = sys.stdin.readline

T = int(input())


def find_parents(node, root_node):
    temp = [node]
    while not node == root_node:
        temp.append(p[node])
        node = p[node]
    return temp


for _ in range(T):
    N = int(input())

    p = [i for i in range(N + 1)]

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        p[child] = parent

    root_node = 1
    for i in range(len(p)):
        if i == p[i]:
            root_node = i

    # print(root_node)

    node1, node2 = map(int, input().split())

    # print(p)
    # print(node1, node2)

    temps = find_parents(node1, root_node)
    temps2 = find_parents(node2, root_node)

    # print(temps)
    # print(temps2)

    for i in temps:
        if i in temps2:
            print(i)
            break
