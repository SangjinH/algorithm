import sys
input = sys.stdin.readline

# 전위순회, 중위순회 ==> 후위순회
# 후위순회이기에 루트를 가장먼저 배출해야함
def doPostOrder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root_idx = inorder.index(preorder[0])

    left_in = inorder[0:root_idx]
    left_pre = preorder[1:1+len(left_in)]
    doPostOrder(left_pre, left_in)

    right_in = inorder[root_idx+1:]
    right_pre = preorder[len(left_pre)+1:]
    doPostOrder(right_pre, right_in)

    print(preorder[0], end=" ")

T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    doPostOrder(a, b)
