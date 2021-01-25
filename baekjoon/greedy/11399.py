## ATM

n = int(input())
time_list = [int(i) for i in input().split()]
time_list.sort()
print(time_list)

total = 0
k = len(time_list)

for i in range(len(time_list)):
  total += int(time_list[i]) * k
  k -= 1
  print(total)

print(total)