'''
모든 숫자를 다른 숫자 여러개의 합으로 표현할 수 있다. 
예로는 
8 = 3 + 3 + 2
  = 2 + 2 + 2 + 2

  저 숫자들을 곱했을 때, 가장 최대가 되는 값은 ?

'''
a = int(input())

dp = [0, 1]

if a > 2:
    for i in range(2, a+1):
        dp.append(i-1)

print(dp)