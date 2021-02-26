import sys

n = list(sys.stdin.readline().rstrip())

# 연산자의 우선순위를 dict형태로 저장
oper_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

postfix = []
stack = []
ans = ''
for i in n:
    # 알파벳이면 후위 표기 스택에 바로 넣는다
    if 'A' <= i <= 'Z':
        postfix.append(i)
    # 여는 괄호면 연산자 스택에 바로 넣는다
    elif i == '(':
        stack.append(i)
    elif i == ')':
        # 연산자 스택이 비거나 여는괄호를 만날 때 까지 pop
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        # 이 때의 pop은 여는 괄호이므로 후위 표기 스택에 저장하지 않는다
        stack.pop()
    else:
        # 현재 연산자가 스택의 top 연산자보다 우선순위가 높은 경우
        while stack and oper_dict[i] <= oper_dict[stack[-1]]:
            postfix.append(stack.pop())
        # 그렇지 않은 경우거나 낮은 우선순위를 가진 연산자를 모두 pop한 경우
        stack.append(i)

# 항상 연산자 스택에는 하나 이상의 연산자가 존재하므로 스택을 비워준다
while len(stack) != 0:
    postfix.append(stack.pop())

# 정답 출력
for i in postfix:
    ans += i
print(ans)