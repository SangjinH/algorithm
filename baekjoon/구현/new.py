# 모든 숫자는 홀수의 합으로 표현할 수 있다.
# 그렇다면 가장 많은 홀수를 사용하는 list를 반환해라
# 4
# [1, 3]
# 8
# [1, 7], [3, 5] 둘 중에 하나 return
# 15
# [1, 3, 11]
# 완탐 X, dp 
# 1, 2, 3, 4, 5, 6
# 18
# [1, 3, 5, 9]
# 가능한한 많은 홀수를 써야함 
# [1, 3, 5, 9]






























from collections import deque

# a = int(input())

result = []

def sol(num, num_list, target):
    global result


    if target == 2:
        result = [][:]
        return

    if target < 8:
        if target % 2 == 1:
            result = [target][:]
            return
        else:
            result = [1, target - 1][:]
            return


    if sum(num_list) == target:
        if len(result) < len(num_list):
            result = num_list[:]
            return
    # 1 3 5 //  15
    else:
        if sum(num_list) + num > target:
            print(num)
            print("over")
            return
        # sum(num_list) + num < target 이라면
        else:
            num_list.append(num)
            print(num_list)
            sol(num+2, num_list, target)

            check = num_list.pop()
            if check == 1:
                return
            print(num_list)
            sol(num+2, num_list, target)


# print(sol(1, [], a))
# print(result)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  100
# [1, 3, 5, 7, 9, 11, 13, 15, 35]      99
# [3, 5, 7, 9, 11, 13, 15, 17, 19]

# N^2 홀수의 합 ==> 100
# [] 10개 최대



# dp 차원 하나늘려서
# 8
# [1,7] [3,5]
# 9 ==> [1, 8] [1, 1, 7]
#       [1, 3, 5]

def sol(n):
    dp=[0]*(n+1)
    for i in range(2,n+1):
        temp = 0
        end_point = i//2
        for j in range(1,end_point+1):
            temp = max(max(i-j,dp[i-j])*max(j,dp[j]),temp)
        dp[i] = temp
    return dp[n]


print(sol(1))