import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, list(input().rstrip())))

maxi = nums[0]
idx = 0
for i in range(1, len(nums)):
    if maxi < nums[i]:
        maxi = nums[i]
        idx = i

left = nums[:idx]
right = nums[idx+1:]

print('left: ', left)
print('right: ', right)

cnt = 0

# 지워야하는 갯수가 왼쪽에 있는 갯수보다 작다면
if K < len(left):
    stack = [left[0]]
    flag = False

    for i in range(1, len(left)):
        if stack[-1] < left[i]:
            stack.pop()
            cnt += 1
            stack.append(left[i])

        if cnt == K:
            print([stack] + left[i:] + [maxi] + [right])
            flag = True
            break

    if not flag:
        print(left[:len(left)-cnt] + [maxi] + [right])
# 갯수가 같다면
elif K == len(left):
    print([maxi]+right)
# 지워야하는 갯수가 더 많다면
else:
    K -= len(left)
    flag = False
    # 오른쪽 첫번째 원소를 기준으로
    stack = [right[0]]
    # 오른쪽 부분을 돌면서
    for i in range(1, len(right)):
        # 저장되어 있는 값보다 크다면
        if stack[-1] < right[i]:
            stack.pop()
            cnt += 1
            stack.append(right[i])

        # cnt 와 K 가 같다면 break
        if cnt == K:
            temp = [maxi] + stack + right[:cnt+1]
            print(temp)
            flag = True
            break
    if flag:
        print(''.join(map(str,temp)))
    # 만약에 뒤의 숫자가 모두 같거나 작은숫자가 계속들어오면
    else:
        print(stack)
        print(cnt)
        temp = [maxi] + stack + right[len(stack):K-len(stack)]
        print(''.join(map(str,temp)))


# 5 3
# 19452


