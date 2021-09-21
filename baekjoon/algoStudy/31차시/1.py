import sys
input = sys.stdin.readline
from collections import defaultdict


def operation(num1, num2, oper):
    if oper == '+':
        return num1+num2

    elif oper == '-':
        return num1-num2

    elif oper == '*':
        return num1*num2

    elif oper == '/':
        return num1/num2



N = int(input())
equations = input().rstrip()
match = defaultdict(int)

for i in equations:
    if i.isalpha():
        match[i] = 0

for k, v in match.items():
    match[k] = int(input())


stack = []
for i in equations:
    if i.isalpha():
        stack.append(i)
    else:
        if stack[-1] in match.keys():
            num2 = match[stack.pop()]
        else:
            num2 = stack.pop()

        if stack[-1] in match.keys():
            num1 = match[stack.pop()]
        else:
            num1 = stack.pop()

        stack.append(operation(num1, num2, i))

print('{:.2f}'.format(stack[0]))