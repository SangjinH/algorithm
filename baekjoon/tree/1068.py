import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

trees = {i:[] for i in range(50)}

nums = list(map(int, input().split()))

root = -1
for i in range(len(nums)):
    if nums[i] == -1:
        root = i
        continue
    trees[nums[i]].append(i)

point = int(input())



def cut_tree(trees, point):

    if point == root:
        return 0

    remove_list = deque([point])
    for key in trees.keys():
        if point in trees[key]:
            trees[key].remove(point)
            break
    
    while remove_list:
        parent = remove_list.popleft()

        if trees[parent]:
            for node in trees[parent]:
                remove_list.append(node)
            
            del trees[parent]
    print(trees)
    
    return trees

def find_leaf(trees, root):

    if trees == 0:
        return 0


    answer = 0    
    parents = deque([root])

    while parents:
        p = parents.popleft()

        # 자식들이 존재한다면,
        if trees[p]:
            for i in trees[p]:
                parents.append(i)
        else:
            if p != root:
                answer += 1
    
    return answer

cutting_tree = cut_tree(trees, point)
print(find_leaf(cutting_tree, root))