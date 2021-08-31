import sys
input = sys.stdin.readline
import heapq
import copy

k, n = map(int, input().split())

primes = list(map(int, input().split()))

nums = copy.deepcopy(primes)
heapq.heapify(nums)

for i in range(n):
    num = heapq.heappop(nums)
    for j in range(k):
        check = num * primes[j]
        heapq.heappush(nums, check)
