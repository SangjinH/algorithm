import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

stack_sum = [0]
for i in range(len(numbers)):
    stack_sum.append(stack_sum[-1]+numbers[i])

# print(stack_sum)
answer = int(1e9)
s = 0
e = 1
while s != N:

    if stack_sum[e] - stack_sum[s] >= S:
        if e - s < answer:
            answer = e - s
        s += 1

    else:
        if e != N:
            e += 1
        else:
            s += 1

if answer == int(1e9):
    print(0)
else:
    print(answer)


# print(numbers)

# for start in range(len(numbers)):
#
#     total_sum = 0
#     length = 0
#     end = start
#
#     while total_sum < S and end < len(numbers):
#         total_sum += numbers[end]
#         end += 1
#         length += 1
#
#     if total_sum >= S:
#         if length < answer:
#             answer = length
#
# if answer == int(1e9):
#     print(0)
# else:
#     print(answer)