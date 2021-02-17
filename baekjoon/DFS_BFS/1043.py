import sys
input = sys.stdin.readline
from collections import deque


def bfs(knows):
    if type(knows) == int:
        q = deque([knows])
    else:
        q = deque(knows)

    while q:
        know_person = q.popleft()
        for i in parties:
            if know_person in i:
                i.remove(know_person)
                for person in i:
                    q.append(person)
    return



N, M = list(map(int, input().split()))
know_True_list = list(map(int, input().split()))[1:]
parties = []
people = [0] * 51
cnt = 0
for _ in range(M):
    temp = list(map(int, input().split()))[1:]
    if len(temp) == 0:
        cnt += 1
    else:
        parties.append(temp)


    for i in know_True_list:
        bfs(i)

for i in parties:
    if len(i):
        cnt += 1

print(cnt)