import sys
input = sys.stdin.readline

# 스택을 이용한 알고리즘
# 같은 정수가 두 번 나오는 경우는 없음

def check_last(stack, number):

    # stack 이 비어있지않고
    if not stack:
        return False

    if stack[-1] == number:
        return True



n = int(input())

check = []

for _ in range(n):
    check.append(int(input()))

ans = []

minus_cnt = 0

stack = []
idx = 0
for i in range(1, n+1):
    # 먼저 stack 에 원소를 집어 넣는다.
    stack.append(i)
    ans.append('+')

    # 방금 집어넣은 원소와 출력해야할 원소가 같다면
    if stack[-1] == check[idx]:
        # pop 해주고 idx 이동
        stack.pop()
        idx += 1
        ans.append('-')
        minus_cnt += 1

        while 1:
            if stack and idx < n:
                if check_last(stack, check[idx]):
                    stack.pop()
                    idx += 1
                    ans.append('-')
                    minus_cnt += 1
                else:
                    break
            else:
                break

if minus_cnt != n:
    print('NO')
else:
    for i in range(len(ans)):
        print(ans[i])

