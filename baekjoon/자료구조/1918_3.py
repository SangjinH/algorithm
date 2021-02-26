import sys

input = sys.stdin.readline

notation = list(input().rstrip())
priority = {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 0,
            }

stack = []
result = ''

for i in notation:
    if i == '(':    # 여는괄호 무조건 append
        stack.append(i)
    elif 'A' <= i <= 'Z':   # 알파벳이면 바로 result += i
        result += i

    elif i == ')':
        while 1:
            pick = stack.pop()
            if pick == '(':
                break
            else:
                result += pick

    else:  # notation[i] 가 +,-,*,/ 일때
        if len(stack) == 0 or priority[i] > priority[stack[-1]]:  # 현재 우선순위가 높을때는 append
            stack.append(i)
        else:  # 우선순위가 stack 의 마지막보다 낮거나 같을때
            while 1:
                pick = stack.pop()
                result += pick
                if not stack:
                    break
                if priority[i] > priority[stack[-1]]:
                    break
            stack.append(i)

while stack:
    result += stack.pop()

print(result)