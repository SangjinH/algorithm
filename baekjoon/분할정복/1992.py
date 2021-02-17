import sys
input = sys.stdin.readline

def divide(x, y, standard):
	if standard == 1:
		print(arr[x][y], end='')
		return
	
	flag = True
	for i in range(x, x+standard):
		if not flag:
			break
		for j in range(y, y+standard):
			if arr[i][j] != arr[x][y]:
				flag = False
				break
	
	if flag:
		print(arr[x][y], end='')
	else:
		new_standard = standard // 2
		
		print('(', end='')
		divide(x, y, new_standard)
		divide(x, y+new_standard, new_standard)
		divide(x+new_standard, y, new_standard)
		divide(x+new_standard, y+new_standard, new_standard)
		print(')', end='')
		




N = int(input())
arr = [list(input()) for _ in range(N)]
divide(0, 0, N)

