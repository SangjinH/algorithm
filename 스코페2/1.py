import sys
input = sys.stdin.readline

def find_rev(t, h):
    if t == h:
        print('no')
        return
    else:
        if not graph[t]:
            print('no')
            return
        else:
            for i in graph[t]:
                if i==h:
                    print('yes')
                    return
                check = find_rev(i, h)
                if check == 'yes':
                    print('yes')
                    return



N, Q = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    head, tail = list(map(int, input().split()))
    graph[tail].append(head)

test = []
for _ in range(Q):
    head, tail = list(map(int, input().split()))
    test.append((tail, head))
    find_rev(tail, head)