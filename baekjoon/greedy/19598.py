num = int(input())
conf = []
Answer = []
for _ in range(num):
    conf.append(list(map(int, input().split())))

conf = sorted(conf, key=lambda x: (x[1], x[0]))

if num > 0:
    Answer.append(conf[0])

    for i in range(1, num):
        if conf[i][0] >= Answer[-1][1]:
            Answer.append(conf[i])


print(len(Answer))