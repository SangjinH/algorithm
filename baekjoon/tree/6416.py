import sys
input = sys.stdin.readline
from collections import defaultdict

def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

P = defaultdict(int)

while 1:
    