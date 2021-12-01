import sys
input = sys.stdin.readline

"""
프린터기, FIFO 먼저들어온 것을 처리하는 프린터
중요도 높은 문서
중요도가 같은 문서가 여러개 있을 수 있다.

최대값임을 확인하는 최대 힙큐 1개 +
현재 상태 확인할 큐 1개
"""
from collections import deque


def find(max_q, print_q, find_idx):

    cnt = 1

    while max_q:
        maxi = max_q.popleft()

        while print_q:

            now = print_q.popleft()

            if now[0] != maxi:
                print_q.append(now)
            # 만약에 숫자가 같다면
            else:
                # idx 까지 같은지 확인
                if now[1] == find_idx:
                    return cnt
                else:
                    cnt += 1
                    break


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))

    max_q = deque(sorted(documents, reverse=True))

    print_q = deque()
    for idx, val in enumerate(documents):
        print_q.append((val, idx))

    print(find(max_q, print_q, M))

