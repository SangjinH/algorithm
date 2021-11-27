"""
한 번에 한 개의 단어만 바꿀 수 있다.
words에 있는 단어로만 바꿀 수 있다.
최소 몇단계로 바꿀 수 있는지 ?
"""
from collections import defaultdict

def bfs(start, target, visited):
    if start == target:
        return

def solution(begin, target, words):

    visited = defaultdict(int)
    for word in words:
        visited[word] = 0

    print(visited)

    bfs(begin, target, visited)
    answer = 0
    return answer



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
