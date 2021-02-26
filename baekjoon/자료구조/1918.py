import sys
input = sys.stdin.readline

tools = ['+', '-', '*', '/']
equation = input().rstrip()

q = []
Alphas = ''
calculs = ''
for i in equation:
    if i == '(':
        q.append(i)
        continue

    if i in tools:
        calculs += i
        continue

    if i == ')':
        q.pop()
        Alphas += calculs[-1]
        calculs = calculs[:-1]
        continue

    Alphas += i

for i in calculs[::-1]:
    Alphas += i

print(Alphas)

