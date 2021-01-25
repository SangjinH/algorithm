# 백준 1924 번

m, d = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = 0
for i in range(m-1):
    num += days[i]
num += d

yoil = ['MON','TUE','WED','THU','FRI','SAT','SUN']

print(yoil[(num%7)-1])