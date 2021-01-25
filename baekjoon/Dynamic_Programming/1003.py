# 백준 1003 , 피보나치 수열
import sys
input = sys.stdin.readline

def dp_fibo(x):
    zero_count = [1, 0]
    one_count = [0, 1]
    if x <= 1:
        return

    for i in range(2,x+1):
        zero_count.append(zero_count[i-1]+zero_count[i-2])
        one_count.append(one_count[i-1]+one_count[i-2])

    return zero_count, one_count

n = int(input().rstrip())
zero_count, one_count = dp_fibo(40)

for _ in range(n):
    m = int(input().rstrip())
    print("{} {}".format(zero_count[m], one_count[m]))
