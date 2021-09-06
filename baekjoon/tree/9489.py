import sys
input = sys.stdin.readline
from collections import defaultdict


# 두 노드의 부모는 다르지만, 두 부모가 형제일 때 두 노드를 사촌이라고함

n, k = map(int, input().split())
tree = defaultdict(list)
