import sys
input = sys.stdin.readline

STR1 = input().rstrip()
STR2 = input().rstrip()

if len(STR1) > len(STR2):
    STR1, STR2 = STR2, STR1


find_str = [[] for _ in range(len(STR1))]

print(find_str)

for i in range(len(STR1)):
    for j in range(len(STR2)):
        if STR1[i] == STR2[j]:
            find_str[i].append(j)

print(find_str)