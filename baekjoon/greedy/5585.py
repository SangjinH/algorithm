# 백준 5535 번
change = 1000 - int(input())

moneys = [500, 100, 50, 10, 5, 1]

result = 0

for i in moneys:
    if change >= i:
        result += change//i
        change -= i*(change//i)

    if change == 0:
        break

print(result)
