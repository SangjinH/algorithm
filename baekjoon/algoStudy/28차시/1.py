import sys
input = sys.stdin.readline


w, h = map(int, (input().split()))
num_of_cuts = int(input())

horizons = []
verticals = []

for _ in range(num_of_cuts):
    flag, num = map(int, (input().split()))

    # 세로라면
    if flag:
        verticals.append(num)
    else:
        horizons.append(num)

horizons.sort()
verticals.sort()
horizons.append(h)
verticals.append(w)

h_min = 0
maxi_h = 0
for i in range(len(horizons)):

    if horizons[i] - h_min > maxi_h:
        maxi_h = horizons[i] - h_min
    h_min = horizons[i]

w_min = 0
maxi_m = 0
for i in range(len(verticals)):

    if verticals[i] - w_min > maxi_m:
        maxi_m = verticals[i] - w_min
    w_min = verticals[i]

print(maxi_h*maxi_m)