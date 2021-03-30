import sys
input = sys.stdin.readline

while 1:
    letters = input().rstrip()
    if letters == '0':
        break

    if letters == letters[::-1]:
        print('yes')
    else:
        print('no')