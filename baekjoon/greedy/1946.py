# 백준 10162 번
t = int(input())
buttons = [300, 60, 10]
if t % 10 != 0:
    print(-1)
else:

    counts = [0] * 3
    for i in range(3):
        if t >= buttons[i]:
            counts[i] = counts[i] + t//buttons[i]
            t -= counts[i] * buttons[i]

        if t == 0:
            break
    for i in counts:
        print(i, end=' ')