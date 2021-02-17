import sys
input = sys.stdin.readline
from collections import deque


def bfs(person):
    q = deque([person])

    while q:
        know_person = q.popleft()

        for i in parties:
            if know_person in i:
                i.remove(know_person)
                for p in i:
                    q.append(p)
    return


N, M = list(map(int, input().split()))
True_persons = list(map(int, input().split()))[1:]
parties = []
cnt = 0
for i in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        cnt += 1
    else:
        parties.append(temp[1:])

for person in True_persons:
    bfs(person)

for party in parties:
    if party:
        cnt += 1

print(cnt)
