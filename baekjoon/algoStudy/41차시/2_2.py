import sys
input = sys.stdin.readline

letters = list(input().rstrip())

count = dict()
for i in letters:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1


def dfs(before, length):

    if length == len(letters):
        return 1

    answer = 0
    for key in count.keys():
        if before == key:
            continue
        if count[key] == 0:
            continue

        count[key] -= 1
        answer += dfs(key, length+1)
        count[key] += 1

    return answer

answer = dfs("", 0)
print(answer)
