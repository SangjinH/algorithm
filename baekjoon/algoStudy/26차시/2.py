import sys
input = sys.stdin.readline
from collections import deque

check = {
    ')': '(',
    ']': '['
}

number = {
    '(': 2,
    '[': 3
}

def bracket_stack():
    brackets = deque(input().rstrip())

    stack = []

    for i in brackets:

        # stack 이 비어있으면 무조건 추가
        if not stack:
            stack.append(i)

        # 여는 괄호라면
        elif i in number.keys():
            stack.append(i)

        # 닫는 괄호면서, 비어있지 않으면 이전에 들어간 괄호와 짝이 맞는지 확인
        else:
            # 이전의 들어간 괄호와 짝이 맞지 않는다면 0리턴
            if check[i] != stack[-1]:
                return 0

            # 마지막 원소가 숫자라면
            elif stack[-1].isdigit():
                # 길이가 1 이면 0을 반환
                if len(stack) == 1:
                    return 0
                # 길이가 1 이상이면
                else:



            # 짝이 맞는 괄호라면
            else:
                # 일단 짝에 맞는 숫자 삽입
                temp = number[stack.pop()]
                # 일단 숫자 뽑아놓고 전의 원소가 숫자인지 확인
                while 1:
                    if not stack:
                        break

                    else:
                        if stack[-1].isdigit():
                            temp += stack.pop()
                        else:
                            stack.append(temp)
                            break



                # 숫자가 근처에 있는지 확인
                pass



