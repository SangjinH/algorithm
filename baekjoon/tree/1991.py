import sys
input = sys.stdin.readline


def find(num):

    print(Root[num], end='')
    if Left[num] != '.':
        find(Root.index(Left[num]))

    if Right[num] != '.':
        find(Root.index(Right[num]))

def find1(num):

    if Left[num] != '.':
        find1(Root.index(Left[num]))

    print(Root[num], end='')

    if Right[num] != '.':
        find1(Root.index(Right[num]))


def find2(num):

    if Left[num] != '.':
        find2(Root.index(Left[num]))

    if Right[num] != '.':
        find2(Root.index(Right[num]))

    print(Root[num], end='')


Root = []
Left = []
Right = []

N = int(input())
for _ in range(N):
    a, b, c = input().split()
    Root.append(a)
    Left.append(b)
    Right.append(c)

find(0)
print()
find1(0)
print()
find2(0)