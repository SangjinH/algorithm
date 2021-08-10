import sys
input = sys.stdin.readline

n = int(input())


# nums = [True for i in range((10**n)-1)]
#
# for i in range(2, int(((10**n)-1)**(1/2))):
#     for j in range(i+i, (10**n)-1, i):
#         nums[j] = False
#
#
# first_num = [2, 3, 5, 7, 9]
# next_nums = [1, 2, 3, 5, 7, 9]
#
# ans = []
#
#
# def find_next(num_to_str):
#     if len(num_to_str) == n:
#         if nums[int(num_to_str)]:
#             print(num_to_str)
#         return
#
#     # 첫번째 원소가 없는 상태라면
#     if not num_to_str:
#         for i in first_num:
#             num_to_str += str(i)
#             if nums[int(num_to_str)]:
#                 find_next(num_to_str)
#
#             num_to_str = num_to_str[:-1]
#     # 첫번째 원소가 들어온 상태라면
#     else:
#         for i in next_nums:
#             num_to_str += str(i)
#             if nums[int(num_to_str)]:
#                 find_next(num_to_str)
#
#             num_to_str = num_to_str[:-1]
#
# find_next("")

start = ['2', '3', '5', '7']
next = ['1', '3', '7', '9']

def second(num_to_str):
    for i in range(2, int(int(num_to_str)**(0.5))+1):
        if int(num_to_str) % i == 0:
            return

    if len(num_to_str) == n:
        print(num_to_str)
        return

    for p in next:
        second(num_to_str+p)

for s in start:
    second(s)