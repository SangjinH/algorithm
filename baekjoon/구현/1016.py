import sys
input = sys.stdin.readline
mini, maxi = list(map(int, input().split()))

isTrue = [True] * (maxi - mini + 1)

# 에라토스테네스의 체, 소수판별
# 제곱수의 처음인 2부터
N = 2
cnt_False = 0
while 1:
    square = N*N    # 제곱수 생성
    if square > maxi:   # 제곱수가 최대값보다 커지면 종료
        break
    i = mini // square

    while square * i <= maxi:
        idx = square * i - mini

        if idx >= 0 and isTrue[idx]:
            isTrue[idx] = False
            cnt_False += 1

        i += 1
    N += 1

print(len(isTrue) - cnt_False)