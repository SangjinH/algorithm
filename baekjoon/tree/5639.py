def pre(start):

    if Left[Root.index(start)] != 0:
        pre(Left[Root.index(start)])

    if Right[Root.index(start)] != 0:
        pre(Right[Root.index(start)])

    print(start)


# 50 30 24 5 28 45 98 52 60

nums = []

import sys
while 1:
    try:
        a = input()
        nums.append(int(a))

    except:
        break


Root = [0] * len(nums)
Left = [0] * len(nums)
Right = [0] * len(nums)


roots = [100, 0]


for i in range(len(nums)):
    # Root 에다 모두 초기화
    Root[i] = nums[i]

    # 만약 기준값보다 더 큰 값이 들어오면
    if roots[-1] < nums[i]:
        while 1:
            if roots[-1] < nums[i]:
                node = roots.pop()
            else:
                break

        Right[Root.index(node)] = nums[i]
        roots.append(nums[i])

    # 더 작은 값이 들어오면
    else:
        Left[Root.index(roots[-1])] = nums[i]
        roots.append(nums[i])

pre(Root[0])