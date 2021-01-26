# https://www.acmicpc.net/problem/1107
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
usable_buttons = sorted(list(set(list(range(10))) - set(list(map(int, input().split())))))

print(usable_buttons)
ans = []

ans.append(abs(100-n))

result = []
cnt = 0
for word in str(n):
    if int(word) in usable_buttons:
        cnt += 1
        result.append(word)
    else:
        diff = 10
        for button in usable_buttons:
            if diff > abs(int(word) - button):
                diff = abs(int(word) - button)
                but = button
            else:
                diff = but
                cnt += 1
                break
        result.append(str(diff))

result = int(''.join(result))
print(result)
# print(cnt)
ans.append(abs(n-result) + cnt)
print(ans)